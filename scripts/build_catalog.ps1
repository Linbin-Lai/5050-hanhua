param(
    [string]$PackageDirectory = 'E:\汉化\汉化包',
    [string]$RepositoryRoot = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem

$projects = [ordered]@{
    'Agent 64_简体中文新版在线兼容覆盖包.zip'                            = @('Agent-64-Spies-Never-Die', 'Agent 64: Spies Never Die', 'Unity（Steam BuildID 24687138）', 'published')
    'Backrooms The Multiverse_简体中文覆盖包.zip'          = @('Backrooms-The-Multiverse', 'Backrooms The Multiverse', 'Unreal Engine 5.7', 'published')
    'Bite Night Dine or Die_简体中文覆盖包.zip'            = @('Bite-Night-Dine-or-Die', 'Bite Night: Dine or Die', 'Unity 2022.3.20f1 Mono', 'published')
    'Bite Night_简体中文覆盖包.zip'                         = @('Bite-Night', 'Bite Night', 'Unity 2022.3.20f1 Mono', 'published')
    'Burger Bots Inc_简体中文覆盖包.zip'                    = @('Burger-Bots-Inc', 'Burger Bots Inc', 'Unity 2022.3.62f2 Mono', 'published')
    'CashGrab Refunded_简体中文覆盖包.zip'                   = @('CashGrab-Refunded', 'CashGrab Refunded', 'Unity 6000.2.9f1 Mono', 'published')
    'Endacopia_简体中文覆盖包.zip'                           = @('Endacopia', 'Endacopia', 'Adventure Game Studio 3.6.0.55', 'published')
    'Fallen Leaf_简体中文覆盖包.zip'                        = @('Fallen-Leaf', 'Fallen Leaf', 'GameMaker Studio 1.4', 'published')
    'FrogLegs_简体中文覆盖包.zip'                            = @('FrogLegs', 'FrogLegs', 'Unreal Engine 5.3', 'published')
    'Funnel Runners_简体中文覆盖包.zip'                     = @('Funnel-Runners', 'Funnel Runners', 'Unreal Engine 5.6', 'published')
    'GetOut_简体中文覆盖包.zip'                             = @('GetOut', 'デテイケ -GetOut-', 'Unreal Engine 5.3', 'published')
    'Hell of a Birthday_简体中文覆盖包.zip'                 = @('Hell-of-a-Birthday', 'Hell of a Birthday', 'Unity 2022.3.20f1 Mono', 'published')
    'Jeffrey Eggstein_简体中文覆盖包.zip'                   = @('Jeffrey-Eggstein', 'Jeffrey Eggstein', 'Unity 6000.5.0f1 Mono', 'published')
    'Mine of My Mind_简体中文覆盖包.zip'                    = @('Mine-of-My-Mind', 'Mine of My Mind', 'Unity 6000.0.59f2 IL2CPP', 'published')
    'NARIBIKIMURA_简体中文覆盖包.zip'                     = @('NARIBIKIMURA', '鳴蟇村（NARIBIKIMURA）', 'Unreal Engine IoStore（含 120 FPS 修改）', 'published')
    'OKUGAFUCHI_简体中文覆盖包.zip'                       = @('OKUGAFUCHI', 'OKUGAFUCHI', 'Unreal Engine IoStore（含 120 FPS 修改）', 'published')
    'Only Good Babysitters Go To Heaven_简体中文覆盖包.zip' = @('Only-Good-Babysitters-Go-To-Heaven', 'Only Good Babysitters Go To Heaven', 'Unity 2022.3.20f1 Mono', 'published')
    'Pih 2_简体中文覆盖包.zip'                               = @('Pih-2', 'Pih 2', 'Unreal Engine 5.3', 'published')
    'StrikersClub_简体中文覆盖包.zip'                       = @('StrikersClub', 'Strikers Club', 'Unreal Engine 5.6', 'published')
    'UNBEATABLE_简体中文覆盖包.zip'                          = @('UNBEATABLE', 'UNBEATABLE', 'Unity Mono x64', 'published')
}

$manifest = [System.Collections.Generic.List[object]]::new()

foreach ($pair in $projects.GetEnumerator()) {
    $file = Join-Path $PackageDirectory $pair.Key
    if (-not (Test-Path -LiteralPath $file)) {
        throw "Missing package: $file"
    }

    $slug, $title, $engine, $publicationStatus = $pair.Value
    $item = Get-Item -LiteralPath $file
    $sha256 = (Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash
    $zip = [IO.Compression.ZipFile]::OpenRead($file)
    try {
        $entries = @($zip.Entries | Where-Object { -not [string]::IsNullOrWhiteSpace($_.Name) })
        $docEntry = $entries | Where-Object { $_.FullName -match '(?i)(安装说明|readme).*\.(txt|md)$' } | Select-Object -First 1
        $instructions = '[覆盖包中未找到安装说明。]'
        if ($docEntry) {
            $stream = $docEntry.Open()
            try {
                $reader = [IO.StreamReader]::new($stream, [Text.Encoding]::UTF8, $true)
                try { $instructions = $reader.ReadToEnd().Trim() }
                finally { $reader.Dispose() }
            }
            finally { $stream.Dispose() }
        }

        $topLevel = @($entries | ForEach-Object {
            ($_.FullName -replace '\\', '/').Split('/')[0]
        } | Sort-Object -Unique)

        $manifest.Add([ordered]@{
            game = $title
            slug = $slug
            package = $pair.Key
            bytes = $item.Length
            sha256 = $sha256
            engine = $engine
            publication_status = $publicationStatus
            zip_entries = $entries.Count
            top_level = $topLevel
            last_modified = $item.LastWriteTime.ToString('yyyy-MM-ddTHH:mm:ssK')
        })

        $gameDir = Join-Path (Join-Path $RepositoryRoot 'games') $slug
        $checksumDir = Join-Path $gameDir 'checksums'
        New-Item -ItemType Directory -Force -Path $checksumDir | Out-Null

        $notice = switch ($publicationStatus) {
            'published' { '已公开发布。附件不能独立运行，必须配合用户从 Steam 合法取得的对应完整原版游戏使用；具体完成范围和已知问题以安装说明为准。' }
            default { '尚未发布；必须先完成附件、版本兼容性和安装说明复核。' }
        }

        $readme = @"
# $title 简体中文汉化

**汉化署名：5050 汉化组：Cokepoetry 汉化**

## 发布信息

- 引擎/架构：$engine
- Release 文件：``$($pair.Key)``
- 文件大小：$($item.Length) 字节
- ZIP SHA-256：``$sha256``
- ZIP 文件数：$($entries.Count)
- 发布审查状态：``$publicationStatus``

> $notice

## 安装说明

````text
$instructions
````

## 反馈要求

反馈时请提供游戏版本、补丁文件 SHA-256、问题截图、所在位置和前后流程。崩溃问题请附完整错误提示或日志。

## 验证声明

除非发布说明明确写明经过运行测试，否则构建过程仅完成静态解析、回读、哈希和文件结构检查；实际显示与流程由用户手动验证。
"@

        [IO.File]::WriteAllText((Join-Path $gameDir 'README.md'), $readme, [Text.UTF8Encoding]::new($false))
        [IO.File]::WriteAllText((Join-Path $checksumDir 'release.sha256'), "$sha256  $($pair.Key)`n", [Text.UTF8Encoding]::new($false))
    }
    finally {
        $zip.Dispose()
    }
}

$manifestPath = Join-Path (Join-Path $RepositoryRoot 'releases') 'manifest.json'
$json = $manifest | ConvertTo-Json -Depth 5
[IO.File]::WriteAllText($manifestPath, $json + "`n", [Text.UTF8Encoding]::new($false))
Write-Host "Catalog written: $($manifest.Count) projects"
