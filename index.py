import json
import os

DB_FILE = 'projects.json'

def load():
    if os.path.exists(DB_FILE):
        with open(DB_FILE) as f:
            return json.load(f)
    return []

def save(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_project(name, purpose, location, last_change):
    data = load()
    data.append({'name': name, 'purpose': purpose, 'location': location, 'last_change': last_change})
    save(data)
    print('Added project', name)

if __name__ == '__main__':
    # Example
    add_project('Main Repo', 'Core product', '/path/to/repo', '2026-05-14')