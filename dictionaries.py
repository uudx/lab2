thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)# {'name': 'John', 'age': 36, 'country': 'Norway'}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)#Mustang


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)#dict_keys(['brand', 'model', 'year'])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
y = car.keys()
z = car.items()
print(x, "\n", y, "\n",z)
#dict_values(['Ford', 'Mustang', 1964])
#dict_keys(['brand', 'model', 'year'])
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#update items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#add items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#remove items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#Nested dictionary
#a dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#print the mane of child2
print(myfamily["child2"]["name"])#Tobias

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
