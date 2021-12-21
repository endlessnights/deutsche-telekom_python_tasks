import json

with open('ne-data.txt', 'r') as json_file:
    data = json.load(json_file)

with open('result.txt', 'w') as f:
    result = ''
    for interface in data['task_result']['content']['network-element'][0]['interface']:
        if interface['admin-status'] == 'up':
            result += f'{interface["name"]}, {interface["admin-status"]}, {interface["id"]}\n'
    f.write(result)  # в цикле каждая запись с новой строки
    f.close()
