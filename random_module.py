import random

x = random.random()
# print(x)


x = random.randint(1,10)
print(x)
print(type(x))
# amount = 500
# total = amount - (amount*x)/100
# print(total)

x = random.randrange(1, 10, 2)
# print(x)
# print(type(x))

# names = ["rajat", "ashwini", "madhuri", "atul", "subham"]
# last_names = ["ajay","patil","bhosle","sharma"]
# domains = ["gmail.com","yahoo.com", "hotmail.com"]
#
# email = f"{random.choice(names)}.{random.choice(last_names)}@{random.choice(domains)}"
# print(email)


# list_data =[10,20,45,74,52,66]

# x =random.choice(list_data)
# print(x)
# print(type(x))

# data = random.choices(list_data,k = 3)
# print(data)

cards = ["H1","H2","H3","H4","H5","H6","H8",
         "S1","S2","S3",
         "D1","D2",
         "Q1","Q2","Q3","Q4"]

# random.shuffle(cards)
# print(cards)
#
# data = random.choices(cards,k=5)
# print(data)
#
# hand1 = random.choices(cards,k = 5)
# print(hand1)

list_data = [1,2,3,4,3]

list_data.append(10)

print(list_data)
if list_data.count(3) > 1:
    print("duplicated")














