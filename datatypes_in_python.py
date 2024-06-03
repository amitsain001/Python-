#Strings

a = " Hello World"
print(a.lower())
print(a.upper())
print(len(a))
print(a.count("l"))
print(a.split("  "))
print(a.rstrip())
print(a.lstrip())

b = "UpFlairs"
print(b[1:4])
print(b[:4])
print(b[0:])
print(b[-4:-1])

c = "hello"
d = "world"
e = c + "  " + d
print(e)
print("my name is \"Mohit\"")

age = 19
name = f"My name is Mohit. I am {age} years old."
print(name)

# Data Types
# build-in data types(lists,tuple,sets,dictionary)

#lists
lst = [19,"Mohit",23.45,False]
print(lst)

print(len(lst))
lst[1] = "Apple"
print(lst)

lst[1:3] = ["orange",3.14]
print(lst)

lst[1:2] = ["pear",25.67]
print(lst)
lst[1:3] = ["banana"]
print(lst)

lst.insert(1,"a")
print(lst)
lst.append("guava")
print(lst)

lst1 = ["apple","kiwi","banana","litchi"]
lst2 = ["cycle","bike","rail","plane"]
lst3 = lst1 + lst2
print(lst3)

lst1.extend(lst2)
print(lst1)

lst1.remove("banana")
print(lst1)

#lst1.pop("apple")
#print(lst1)

lst1.clear()
print(lst1)

lst4 = ["a","Z","h","D","m"]
lst4.sort()
print(lst4)

lst4.sort(reverse = True)
print(lst4)

lst4.sort(key = str.lower)
print(lst4)

lst4.reverse()
print(lst4)

#tuple( unchanceable value, denoted by())

tpl = ("apple","banana","cherry")
print(tpl)
print(type(tpl))
print(len(tpl))

tpl =("apple") #string
print(tpl)
print(type(tpl))

tpl =("apple",) #tuple
print(type(tpl))

x = ("apple","banana","cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print(type(x))

y=list(y)
y.append("orange")
x=tuple(y)
print(x)

x = ("apple","banana","cherry")
y = ("orange",)
x += y
print(x)

y = list(x)
y.remove("banana")
x = tuple(y)
print(x)

fruits = ("apple","banana","cherry")
f = fruits*2
print(f)

# sets(non-dublicate, denoted by{}, index free)

fruits = {"apple","banana","cherry",True,1}
print(fruits)
print(len(fruits))

#dictionary ()

dt = {
    "name" : "Mohit",
    "branch" : "CSE",
    "year" : 1,
    "year" : 2,
    "lst1" : ["apple","kiwi","banana","litchi"],
    "tpl" : ("apple","banana","cherry")
    
    }
print(dt)
print(type(dt))
print(len(dt))

thisdt = dict(name = "Amit", section = "CSE", year = 1)
print(thisdt)
print(type(thisdt))

# Displaying individual items in a dictionary


dit = {
    "name" : "mohit",
    "age" : 19,
    "branch" : "CSE",
    "year" : 2024
}
print(dit["age"])
print(dit.get("branch"))                            #get keyword
print(dit.keys())                                   #keys keyword
print(dit.values())

# Update item in a dictionary

dit = {
    "name" : "Amit",
    "age" : 19,
    "branch" : "CSE",
    "year" : 2024
}
print(dit.items())
a = dit.update({"year":2023})
print(dit)

# Removing item in a dictionary

dit = {
    "name" : "Amit",
    "age" : 19,
    "branch" : "CSE",
    "year" : 2024
}
print(dit.pop("branch"))
print(dit)

dit = {
    "dit1" : {"name" : "Amit"},
    "dit2" : {"month" : "may"},
    "dit3" : {"year" : 1990}
}
print(dit["dit2"])


