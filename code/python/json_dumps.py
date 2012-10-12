import json
print json.dumps({"one":1, "two":'the man said, "cool!"'})
#--> {"two": "the man said, \"cool!\"", "one": 1}
