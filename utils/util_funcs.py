import json
import re

def get_json_from_api():
  with open("./api.json", "r") as json_file:
    json_data = json.load(json_file)
  return json_data

# function to convert camel case to snake case
def camel_to_snake(name):
  name = re.sub('(.)([A-Z][a-z]+|[0-9])', r'\1_\2', name)
  return re.sub('([a-z0-9])([A-Z]|[0-9])', r'\1_\2', name).upper()

def dash_to_snake_ignore_first(name):
  camel = name.replace('-', '_').upper()
  return '_'.join(x for x in camel.split('_')[1:]) 