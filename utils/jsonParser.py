import json

def parse_json(file_path) -> dict:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    
def write_json(file_path, data) -> bool:
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False