using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

EnsureDataLoaded();

string path = Environment.GetEnvironmentVariable("FALLENLEAF_LANG_PATH") ?? "";
if (string.IsNullOrWhiteSpace(path))
    path = PromptLoadFile(
        "",
        "JSON language files (*.json)|*.json|All files (*.*)|*.*");
if (string.IsNullOrWhiteSpace(path))
    throw new ScriptCancelledException("未选择语言文件。");

JsonElement root = JsonSerializer.Deserialize<JsonElement>(File.ReadAllText(path));
if (!root.TryGetProperty("entries", out JsonElement entries) || entries.ValueKind != JsonValueKind.Array)
    throw new ScriptException("语言文件缺少 entries 数组。");

var pending = new List<Tuple<int, string>>();
var mismatches = new List<string>();
var seen = new HashSet<int>();
int emptyTargets = 0;

foreach (JsonElement entry in entries.EnumerateArray())
{
    int index = entry.GetProperty("index").GetInt32();
    string source = entry.GetProperty("source").GetString() ?? "";
    string target = entry.GetProperty("target").GetString() ?? "";

    if (index < 0 || index >= Data.Strings.Count)
    {
        mismatches.Add("索引越界：" + index);
        continue;
    }
    if (!seen.Add(index))
    {
        mismatches.Add("重复索引：" + index);
        continue;
    }
    if (!string.Equals(Data.Strings[index].Content, source, StringComparison.Ordinal))
    {
        mismatches.Add("原文不匹配：" + index);
        continue;
    }
    if (string.IsNullOrEmpty(target))
    {
        emptyTargets++;
        continue;
    }
    pending.Add(Tuple.Create(index, target));
}

if (mismatches.Count > 0)
{
    string preview = string.Join("\n", mismatches.GetRange(0, Math.Min(20, mismatches.Count)));
    throw new ScriptException(
        "导入已取消：发现 " + mismatches.Count + " 个版本或结构不匹配项。\n" + preview);
}

foreach (var item in pending)
    Data.Strings[item.Item1].Content = item.Item2;

ScriptMessage(
    "导入完成。\n已替换：" + pending.Count +
    "\n空译文跳过：" + emptyTargets +
    "\n请另存为新的 data.win，不要直接覆盖唯一原版备份。");
