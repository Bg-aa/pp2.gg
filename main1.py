import json
json_data = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print(data["age"])