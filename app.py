"""
print("Hello World")
phrase = "Giraffe Academy"
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(len(phrase))
print(phrase.upper().isupper())
print(phrase[0])
print(phrase.index("G"))
print(phrase.replace("Giraffe","Elephant"))

my_num=5
print(str(my_num)+ " my favourite number ")
print(abs(my_num))
print(ceil(3.7))
print(floor(3.7))
print(sqrt(36))
print(max(4,6))
print(min(4,6))
print(round(3.2))
print(pow(3,2))
#user input
name = input("your name is : ")
age = input("your age is : ")
print("Hello " + name + " ! you are " + age)

#basic calculator
num1 = input("Enter a number : ")
num2 = input("Enter another number : ")
result = float(num1)+float(num2)
print(result)

#mad libs game
color = input("enter a color : ")
plural_noun = input("enter a plural_noun : ")
celebrity = input("enter a celebrity : ")
print("Roses are " + color)
print(plural_noun + "are blue")
print("I love" + celebrity)


#List
lucky_numbers = [3,7,4,8,10,34,78,89]
friends = ["tia","mia","sia","tara","juhi"]
friends.extend(lucky_numbers)
friends.append("chia")
friends.insert(1,"nia")
friends.remove("nia")
friends.pop()
print(friends.index("mia"))
print(friends.count("juhi"))
lucky_numbers.sort()
friends.reverse()
friends2 = friends.copy()
print(friends)
print(lucky_numbers)


#tuples
coordinates = [(2,3),(6,7),(7,8)]
print(coordinates[2])

#functions
def say_hi(name,age):
    print("Hello" + name)
    print("your age " + str(age))
say_hi(" swat ",24)

#return statement
def cube(num):
    return num*num*num
print(cube(3))"""
def max_sum(num1, num2, num3):
    if num1 >= num2 or num1 >= num3:
        return num1
    elif num2 >= num1 or num2 >= num3:
        return num2
    else:
        return num3
print(max_sum(10, 40, 70))
