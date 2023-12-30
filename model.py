import json

def update_database():
    with open('raw.txt', 'r') as file:
        raw = file.read().split('\n')
        entries = []
        for line in raw:
            date = line[:10]
            time = line[13:21]
            event = line[22:]
            entry = {
                'date': date,
                'time': time,
                'event': event
            }
            entries.append(entry)
        json_data = json.dumps(entries, indent=2)
        with open('database.json', 'w') as f:
            f.write(json_data)
            print('success')