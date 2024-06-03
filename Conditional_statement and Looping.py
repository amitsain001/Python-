
                                    # CONDITIONAL STATEMENTS

#if_and_else
a = 20
b = 20
if b>a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")

else:
    print("a is greater than b")
    
x = 50
y = 10
if x>y: print("x is greater than y")    #short_hand if

m = 25
n = 35
print("m") if m>n else print("n")

c =330
d = 330
print("c") if c>d else print("equal") if c==d else print("d")
                                    
                                    # Bitwise Operator
#(& (and) | (o)r !) in if _else
a = 342
b = 234
c = 90

# Propgram of & (AND) operator

if a>b and a>c:
    print("a is greatest")
if b>a and b>c:
    print("b is greatest")

# Program of checking greater number 

x=41
if x>10:
    print("above 10")
    if x>20:
        pass
        #print("above 20")
    else:
        print("but not above 20")
        
x= input("Enter name: ")
y = input("Enter another name: ")
if x!=y:
    print("contition is not true")
else:
    print("condition is true.")
    
 # Program of checking vowel or not in a given string
 
w = input("Enter a character: ")
if w == ('a' or 'e' or 'i' or 'i' or 'i' or 'A' or 'E' or 'I' or 'O' or 'U'):
    print("Entered character is a vowel")
else:
    print("Entered character is consonent.")   
    
                                    # loops(for_and_while)

fruits = ("apple","banana","cherry")
for x in fruits:
    print(x)
    if x == "banana":
        break
    
    
for x in range(2,10):
        print(x)

for x in range(6):
    print(x)
else: 
    print("finished")
for x in range(6):
    
    if x==3:
        continue
    else:
        print(x)
else: 
    print("finished")    
        
    
                                        #loop in ditionary
dt = {
    "name" : "Mohit",
    "branch" : "CSE",
    "year" : 1,
    "year" : 2,
    "lst1" : ["apple","kiwi","banana","litchi"],
    "tpl" : ("apple","banana","cherry")
}
for x in dt:
    print(dt[x])
for x in dt.keys():
    print(x)
for x in dt.values():
   print(x)
    
for x,y in dt.items():
    print(x,y)

x = input("Enter a number: ")
for y in range(1,11):
    z = int(x)*y
    print(z)
    
    print(f"{x} * {y} = {z}" )
    
                                        # enumerate
fruits = ["apple", "banana","cherry"]
for index, fruits in enumerate(fruits):
    print(index, fruits)
    
        