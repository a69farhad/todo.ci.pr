import json, sys, os

DATA_FILE = "data/tasks.json"

def load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save(tasks):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)

def main():
    tasks = load()
    cmd = sys.argv[1:] if len(sys.argv) > 1 else []
    if not cmd: 
        print("Usage: add <task> | list | remove <id>")
        return
    if cmd[0] == "add":
        tasks.append(" ".join(cmd[1:]))
    elif cmd[0] == "list":
        for i, t in enumerate(tasks, 1): print(i, t)
    elif cmd[0] == "remove" and len(cmd) > 1:
        try: tasks.pop(int(cmd[1])-1)
        except: print("Invalid ID")
    else:
        print("Unknown command")
    save(tasks)

if __name__ == "__main__":
    main()
