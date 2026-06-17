marks ={
       "bibha ": {
              "chemistry":33,
              "math":98,
              "physics":67,
       },
       "shweta":{
              "chemistry":45,
              "math":87,
              "physics":68,

       },
}


print(marks.get("shweta"))
print(marks.keys())
print()
print(marks.values())
print()
for key,value in marks .items():
       print(key,value)

print()
marks.update({"amrita":{"chemistry":87,"math":99,"physics":34}})
print(marks)
print()
print(marks.pop("shweta"))
print()
print(marks.popitem())
print()
print(marks.copy())
print()
print(marks.clear())