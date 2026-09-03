import json
'''
with open("data.json",'r') as file:
    data=json.load(file)
    print(data)

data["name"]="dheeraj"
data["age"]=21
data["language"].append("css")

with open("data.json",'w') as file:
    json.dump(data,file,indent=2)'''

student={
    "name":"dheeraj",
    "age":21,
    "course":"python full stack"
    }
json_data=json.dumps(student)
print(json_data)

student=json.loads(json_data)
print(student)
print(type(student))
