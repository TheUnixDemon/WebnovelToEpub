import json
import re

def getConfig() -> json:
    try:
        with open("configs/config.json", "r") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print("File 'config.json' not found.")
    except json.JSONDecodeError as e:
        print(f"Error loading JSON configuration: {e}")

def getServerConfig(URL: str): # gets spezific server configuration
    config = getConfig()
    for i in range(0, len(config)):
        if re.search(str(config[i]["server"]), URL):
            return config[i]