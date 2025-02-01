thislist = ["apple", "banana", "cherry"]
print(thislist)#['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
print(len(thislist))#3

list1 = ["abc", 34, True, 40, "male"]
print(type(mylist))#<class 'list'>

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])#cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)#['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)#['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)#['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)#['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)#['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)#['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist# delete the entire list

thislist = ["apple", "banana", "cherry"]
thislist.clear()#Clear the list content
print(thislist)#[]

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#apple
#banana
#cherry

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)#['apple', 'banana', 'mango']


#       THE SYNTAX
#   newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)#['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10) if x < 5]
print(newlist)#[0, 1, 2, 3, 4]

newlist = ['hello' for x in fruits]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)#[23, 50, 65, 82, 100]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)#['pineapple', 'orange', 'mango', 'kiwi', 'banana']

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)#[50, 65, 23, 82, 100]

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)#['cherry', 'Kiwi', 'Orange', 'banana']

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)#['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)#['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
