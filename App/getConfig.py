import json

def getConfig() -> json:
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print("File 'config.json' not found.")
    except json.JSONDecodeError as e:
        print(f"Error loading JSON configuration: {e}")
