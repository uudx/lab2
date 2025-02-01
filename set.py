#Set items are unchangeable, but you can remove items and add new items


thisset = {"apple", "banana", "cherry"}
print(thisset)#{'apple', 'banana', 'cherry'}


thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#apple
#banana
#cherry

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)#{'banana', 'orange', 'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #or thisset.discard("banana")
print(thisset)#{'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#cherry
#{'banana', 'apple'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)#{'b', 'c', 1, 2, 3, 'a'}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)#{'a', 1, 'c', 2, 3, 'b'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)#{3, cherry, 'b', 'a', Elena, John, banana, 'c', apple, 2, 1}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)#{'c', 'b', 3, 2, 'a', 1}


