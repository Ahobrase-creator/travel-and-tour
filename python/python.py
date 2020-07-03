print ("Hello Africa")
print ("My name is Ahobrase")
myName = "Ahobrase"
myOccupation = "Data scientist"
age =29
isEmployed =True
isNotFromAfrica = False
print("My name is ", myName)

print ("my name is %s, I am a %s" % ( myName, myOccupation))
print(type(myName))

dataTypeOfName = type(myName)

print("The name variable is of %s data type" % (dataTypeOfName))
print(type(age))
print(type(isEmployed))
print(type(isNotFromAfrica))


def subtract (first, second):
    subtract = first - second
    print(subtract)

def sum (first, second):
    sum = first + second
    print(sum)

def multiplication (first, second):
    multiplication = 15 * 15
    print (multiplication)


subtract(15,15)
sum (15,15)
multiplication (15,15)

def add(first, second):
    addition = first + second;
    return addition

total =add(10,5)
total = add(total,20)
total = add(total,30)
total = add(total,50)
print (total)

def calculate (action, firstNumber, secondNumber) :
    if action =="add":
       result = firstNumber + secondNumber
       return result

    if action == "subtract":
        result = firstNumber - secondNumber
        return result

    elif action =="multiply":
        result = firstNumber * secondNumber
        return result
    

calcResult = calculate("add",10, 5)
calcResult = calculate("subtract",10, 5)
calcResult = calculate("multiply", 10, 5)



print (calcResult)

number = 1
while number <= 20 :
    print("number: ", number)
    number =number + 1


for number in range (10) :
    print("number: ", number)

print("our loop is done")


names = ["David", "Lartey", "John"]
for name in names:
    print("Name is:", name)