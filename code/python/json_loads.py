import json
json_string = '{"json":"string"}'
j = json.loads(json_string)
print j['json'] #--> string
