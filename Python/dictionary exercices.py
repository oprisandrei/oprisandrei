#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict = {"Ten":10,"Twenty":20,"Thirty":30}
print(dict)

#2
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

#3
sampleDict = {
    "class": {
        "student":
            { "name": "Mike",
              "marks": {
                  "physics": 70,
                  "history": 80
              }
              }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])

#4

sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

#Keys to extract
keys = ["name", "salary"]

new_dict={"name":sample_dict["name"],"salary":sample_dict["salary"]}
print(new_dict)

#5
sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york" }
# Keys to remove
keys = ["name", "salary"]

del(sample_dict["name"],sample_dict["salary"])
print(sample_dict)

#7
sample_dict = { "name": "Kelly", "age":25, "salary": 8000, "city": "New york" }

sample_dict["location"]=sample_dict.pop("city")
print(sample_dict)

#8
sample_dict = { 'emp1': {'name': 'Jhon', 'salary': 7500},
                'emp2': {'name': 'Emma', 'salary': 8000},
                'emp3': {'name': 'Brad', 'salary': 500} }
sample_dict["emp3"]["salary"]=8500
print(sample_dict)