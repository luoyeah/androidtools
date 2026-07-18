import json

with open(r'HMA_Config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

first_template = next(iter(data['templates']))

scope = {}
for template_name, template in data['templates'].items():
    for app in template['appList']:
        scope[app] = {
            "aggressiveFilter": False,
            "useWhitelist": True,
            "excludeSystemApps": True,
            "applyTemplates": [first_template],
            "extraAppList": []
        }

data['scope'] = scope

with open(r'HMA_Config.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"已为 {len(scope)} 个应用生成 scope 配置，使用模板: {first_template}")
