using System;
using System.IO;
using System.Text;

EnsureDataLoaded();

string path = Environment.GetEnvironmentVariable("FALLENLEAF_LANG_OUT") ?? "";
if (string.IsNullOrWhiteSpace(path))
    path = PromptSaveFile(
        ".json",
        "JSON language files (*.json)|*.json|All files (*.*)|*.*");
if (string.IsNullOrWhiteSpace(path))
    return;

var json = new StringBuilder();
json.Append("{\n");
json.Append("  \"format\": \"UTMT_Bilingual_StringTable_v1\",\n");
json.Append("  \"entries\": [\n");
for (int i = 0; i < Data.Strings.Count; i++)
{
    json.Append("    {\"index\": ");
    json.Append(i);
    json.Append(", \"source\": ");
    json.Append(Jsonify(Data.Strings[i].Content));
    json.Append(", \"target\": \"\"}");
    if (i + 1 < Data.Strings.Count)
        json.Append(',');
    json.Append('\n');
}
json.Append("  ]\n");
json.Append("}\n");

File.WriteAllText(path, json.ToString(), new UTF8Encoding(false));
ScriptMessage("已导出 " + Data.Strings.Count + " 条字符串：\n" + path);

string Jsonify(string value)
{
    var result = new StringBuilder("\"");
    foreach (char ch in value)
    {
        switch (ch)
        {
            case '\"': result.Append("\\\""); break;
            case '\\': result.Append("\\\\"); break;
            case '\b': result.Append("\\b"); break;
            case '\f': result.Append("\\f"); break;
            case '\n': result.Append("\\n"); break;
            case '\r': result.Append("\\r"); break;
            case '\t': result.Append("\\t"); break;
            default:
                if (char.IsControl(ch))
                    result.Append("\\u" + ((int)ch).ToString("x4"));
                else
                    result.Append(ch);
                break;
        }
    }
    result.Append('\"');
    return result.ToString();
}
