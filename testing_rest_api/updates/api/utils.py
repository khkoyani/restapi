import json

def json_data(data):
    try:
        return json.loads(data)
    except ValueError:
        return False
