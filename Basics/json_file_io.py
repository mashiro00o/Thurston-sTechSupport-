import json

# Read from a json file
with open('data.json') as file: 
  content = json.load(file)  # Load JSON content from the file into a Python dictionary
  print(type(content), content)  # Print the type of content (should be dict) and the content itself

# Another way to read from the json file without consuming the content
with open('data.json') as file:
  content = json.load(file)  # Load content from the file into a Python dictionary
  for key, value in content.items():  # Iterate over each key-value pair in the dictionary
    print(key, value)  # Print each key-value pair

print(content)

# write to json
with open('output.json', 'w') as file: 
  content['age'] = 18
  print(content)
  json.dump(content, file) # method to convert python objects into json format and writing them to the file
  # print(type(content), content)
