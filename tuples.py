#A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)#('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))#3

thistuple = ("apple",)
print(type(thistuple))#<class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))#<class 'str'>

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])#cherry

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)#("apple", "kiwi", "cherry")


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#apple
#banana
#['cherry', 'strawberry', 'raspberry']

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#apple
#banana
#cherry


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)#('a', 'b', 'c', 1, 2, 3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)#('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


