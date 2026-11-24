# Rebuilds map.html from board.json and map.template.html.
import json
data = json.load(open('board.json', encoding='utf-8'))
tpl = open('map.template.html', encoding='utf-8').read()
open('map.html', 'w', encoding='utf-8').write(tpl.replace('__BOARD__', json.dumps(data, ensure_ascii=False)))
print('map.html rebuilt')
