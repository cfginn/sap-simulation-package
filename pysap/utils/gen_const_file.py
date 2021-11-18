# read animal_list.json and generate a constant file

import json
import re

with open("animal_list.json", "r") as json_file:
  json_data = json.load(json_file)

# function to convert camel case to snake case
def camel_to_snake(name):
  name = re.sub('(.)([A-Z][a-z]+|[0-9])', r'\1_\2', name)
  return re.sub('([a-z0-9])([A-Z]|[0-9])', r'\1_\2', name).upper()

def dash_to_snake_ignore_first(name):
  camel = name.replace('-', '_').upper()
  return '_'.join(x for x in camel.split('_')[1:]) 

with open("../constants.py", "w") as const_file:
  # get the unique list of animal names
  for animal, obj in json_data["pets"].items():
    if "StandardPack" in obj["packs"] and obj["tier"] != "Summoned":
      const_file.write("{} = \"{}\"\n".format(dash_to_snake_ignore_first(animal), animal))
  
  # seperate the summoned tier pets
  const_file.write("\n# summoned only pets\n")

  for animal, obj in json_data["pets"].items():
    if obj["tier"] == "Summoned":
      const_file.write("{} = \"{}\"\n".format(dash_to_snake_ignore_first(animal), animal))

  # get the animal names specific to the expansion pack 
  const_file.write("\n# expansion pets\n")
  for animal, obj in json_data["pets"].items():
    if "StandardPack" not in obj["packs"]:
      const_file.write("{} = \"{}\"\n".format(dash_to_snake_ignore_first(animal), animal))
      
  # get the unique foods names
  const_file.write("\n# foods\n")
  for foods, obj in json_data["foods"].items():
    const_file.write("{} = \"{}\"\n".format(dash_to_snake_ignore_first(foods), foods))
    
  # get the unique statuses
  const_file.write("\n# statuses\n")
  for status, obj in json_data["statuses"].items():
    const_file.write("{} = \"{}\"\n".format(dash_to_snake_ignore_first(status), status))
  
  # get the unique ability triggers
  triggers = []
  for animal, obj in json_data["pets"].items():
    if "level1Ability" in obj and obj["level1Ability"]["trigger"] not in triggers:
      triggers.append(obj["level1Ability"]["trigger"])
    if "level2Ability" in obj and obj["level2Ability"]["trigger"] not in triggers:
      triggers.append(obj["level2Ability"]["trigger"])
    if "level3Ability" in obj and obj["level3Ability"]["trigger"] not in triggers:
      triggers.append(obj["level3Ability"]["trigger"])
  
  for foods, obj in json_data["foods"].items():
    if "ability" in obj and obj["ability"]["trigger"] not in triggers:
      triggers.append(obj["ability"]["trigger"])
  
  for status, obj in json_data["statuses"].items():
    if "ability" in obj and obj["ability"]["trigger"] not in triggers:
      triggers.append(obj["ability"]["trigger"])
  
  const_file.write("\n# ability triggers\n")
  for trigger in triggers:
    const_file.write("{} = \"{}\"\n".format(camel_to_snake(trigger), trigger))
  
  # get the unique ability triggerBys

  triggerBys = []
  for animal, obj in json_data["pets"].items():
    if "level1Ability" in obj and obj["level1Ability"]["triggeredBy"]["kind"] not in triggerBys:
      triggerBys.append(obj["level1Ability"]["triggeredBy"]["kind"])
    if "level2Ability" in obj and obj["level2Ability"]["triggeredBy"]["kind"] not in triggerBys:
      triggerBys.append(obj["level1Ability"]["triggeredBy"]["kind"])
    if "level3Ability" in obj and obj["level3Ability"]["triggeredBy"]["kind"] not in triggerBys:
      triggerBys.append(obj["level1Ability"]["triggeredBy"]["kind"])
  
  for foods, obj in json_data["foods"].items():
    if "ability" in obj and obj["ability"]["triggeredBy"]["kind"] not in triggerBys:
      triggerBys.append(obj["ability"]["triggeredBy"]["kind"])

  for status, obj in json_data["statuses"].items():
    if "ability" in obj and obj["ability"]["triggeredBy"]["kind"] not in triggerBys:
      triggerBys.append(obj["ability"]["triggeredBy"]["kind"])
  
  const_file.write("\n# ability triggerBys\n")
  for triggerBy in triggerBys:
    const_file.write("{} = \"{}\"\n".format(camel_to_snake(triggerBy), triggerBy))

  triggerBys = []
  for animal, obj in json_data["pets"].items():
    if "level1Ability" in obj and obj["level1Ability"]["triggeredBy"] not in triggerBys:
      triggerBys.append(obj["level1Ability"]["triggeredBy"])
    if "level2Ability" in obj and obj["level2Ability"]["triggeredBy"] not in triggerBys:
      triggerBys.append(obj["level1Ability"]["triggeredBy"])
    if "level3Ability" in obj and obj["level3Ability"]["triggeredBy"] not in triggerBys:
      triggerBys.append(obj["level1Ability"]["triggeredBy"])
  
  for foods, obj in json_data["foods"].items():
    if "ability" in obj and obj["ability"]["triggeredBy"] not in triggerBys:
      triggerBys.append(obj["ability"]["triggeredBy"])

  for status, obj in json_data["statuses"].items():
    if "ability" in obj and obj["ability"]["triggeredBy"] not in triggerBys:
      triggerBys.append(obj["ability"]["triggeredBy"])
  
  for triggerBy in triggerBys:
    print(triggerBy)
  # get the unique ability effect kinds

  effectKinds = []
  for animal, obj in json_data["pets"].items():
    if "level1Ability" in obj and obj["level1Ability"]["effect"]["kind"] not in effectKinds:
      effectKinds.append(obj["level1Ability"]["effect"]["kind"])
    if "level2Ability" in obj and obj["level2Ability"]["effect"]["kind"] not in effectKinds:
      effectKinds.append(obj["level2Ability"]["effect"]["kind"])
    if "level3Ability" in obj and obj["level3Ability"]["effect"]["kind"] not in effectKinds:
      effectKinds.append(obj["level3Ability"]["effect"]["kind"])
    
  for foods, obj in json_data["foods"].items():
    if "ability" in obj and obj["ability"]["effect"]["kind"] not in effectKinds:
      effectKinds.append(obj["ability"]["effect"]["kind"])

  for status, obj in json_data["statuses"].items():
    if "ability" in obj and obj["ability"]["effect"]["kind"] not in effectKinds:
      effectKinds.append(obj["ability"]["effect"]["kind"])
    
  const_file.write("\n# ability effect kinds\n")
  for effectKind in effectKinds:
    const_file.write("{} = \"{}\"\n".format(camel_to_snake(effectKind), effectKind))

  # get the unique ability effect target kinds

  effectTargets = []
  for animal, obj in json_data["pets"].items():
    if "level1Ability" in obj and "target" in obj["level1Ability"]["effect"] and obj["level1Ability"]["effect"]["target"]["kind"] not in effectTargets:
      effectTargets.append(obj["level1Ability"]["effect"]["target"]["kind"])
    if "level2Ability" in obj and "target" in obj["level2Ability"]["effect"] and obj["level2Ability"]["effect"]["target"]["kind"] not in effectTargets:
      effectTargets.append(obj["level2Ability"]["effect"]["target"]["kind"])
    if "level3Ability" in obj and "target" in obj["level3Ability"]["effect"] and obj["level3Ability"]["effect"]["target"]["kind"] not in effectTargets:
      effectTargets.append(obj["level3Ability"]["effect"]["target"]["kind"])
  
  for foods, obj in json_data["foods"].items():
    if "ability" in obj and "target" in obj["ability"]["effect"] and obj["ability"]["effect"]["target"]["kind"] not in effectTargets:
      effectTargets.append(obj["ability"]["effect"]["target"]["kind"])

  const_file.write("\n# ability effect target kinds\n")
  for effectTarget in effectTargets:
    const_file.write("{} = \"{}\"\n".format(camel_to_snake(effectTarget), effectTarget))
  
  # get the unique probability kinds

  probKinds = []
  for animal, obj in json_data["pets"].items():
    if "probabilities" in obj:
      for prob in obj["probabilities"]:
        if prob["kind"] not in probKinds:
          probKinds.append(prob["kind"]) 

  const_file.write("\n# probability kinds\n")
  for probKind in probKinds:
    const_file.write("{} = \"{}\"\n".format(probKind.upper(), probKind))

  # get the unique turns 

  turns = []
  for animal, obj in json_data["pets"].items():
    if "probabilities" in obj:
      for prob in obj["probabilities"]:
        if prob["turn"] not in turns:
          turns.append(prob["turn"])

  const_file.write("\n# turns\n")
  for turn in turns:
    const_file.write("{} = \"{}\"\n".format(turn.upper().replace("-", "_"), turn)) 

  # get pack names

  const_file.write("\n# pack names\n")
  const_file.write("PACK_NAME_STANDARD = \"StandardPack\"\n")
  const_file.write("PACK_NAME_EXPANSION = \"ExpansionPack1\"\n")