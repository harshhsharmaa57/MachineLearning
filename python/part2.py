# Conditional Statements - Example 1
age = int(input("enter age: "))

if age >= 18:           # if true/false, entire block of code is executed
    print("you can vote")
    print("you can drive")
else:
    print("you can't vote")
    print("you can't drive")


# Example 2 - Traffic Lights
color = input("enter color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Look")
elif color == "green":
    print("Go")
else:
    print("wrong color")

# Example 3
age = int(input("enter age: "))

if age < 13:
    print("child")
elif (age >= 13 and age < 18):
    print("teenager")
else:
    print("adult")


# Example 4 - Login System
username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("login successful!")
elif username != "admin":
    print("wrong username, try again.")
else:
    print("wrong password, try again.")


# Example 5 - num multiple of 5 or not
num = int(input("enter number: "))

if num % 5 == 0:
    print("multiple of 5")
else:
    print("NOT a multiple of 5")


# Example 6 - Odd or Even
num = int(input("enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Login system Same as Example 4

username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("login successful!")
else:
    if username != "admin":        # Nesting
        print("wrong username, try again.")
    else:
        print("wrong password, try again.")



color = input("enter color: ")

match color:                    # match-case statement (Python 3.10+)
    case "red":
        print("Stop")
    case "yellow":
        print("Look")
    case "green":
        print("Go")
    case _:                    # default case uses underscore
        print("wrong color")


# Example 2 - print 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 3 - print 5 to 1
i = 5
while i > 0:
    print(i)    
    i -= 1

# Multiplication table of N
n = int(input("enter n: "))
i = 1

while i <= 10:
    print(i * n)     
    i += 1



# Break & Continue

# Break for multiple of 6
i = 1

while i <= 10:
    if(i % 6 == 0):
        break
    print(i)           # 1, 2, 3, 4, 5, break
    i += 1

# Skip multiples of 3
i = 0

while(i < 10):
    i += 1
    if(i % 3 == 0):
        continue;      # 1, 2, continue, 4, 5, continue, 7, 8, continue, 10
    print(i)

# Print odd nums from 1 to 10 using continue
i = 0

while(i < 10):
    i += 1
    if(i % 2 == 0):
        continue;      # 1, 3, 5, 7, 9
    print(i)



# for Loop - Example 1

for i in range(5):     # 0, 1, 2, 3, 4
    print(i)


# Membership Operator

# Chars of a string
word = "Prime"

for ch in word:
    print(ch)

# Check if char 'i' exists in word
if 'i' in word:
    print("letter exists")



# Example 2 - count number of i's in word

word = "artificial intelligence"
count = 0

for ch in word:
    if ch == 'i':
        count += 1

print(f"i occurs {count} times.")

# Example 3 - count vowels in word
for ch in word:
    if (ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a'):
        count += 1

print(f"vowel count = {count}")





# range()

# 0, 1, 2, 3, 4 
for i in range(5):
    print(i)

# 1, 2, 3, 4 , 5
for i in range(1, 6):
    print(i)

# 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)



