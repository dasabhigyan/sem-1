# i = 1
# while i!=6:
#     print(i)
#     i = i +2
# print("Mid-sem is coming........")

# n = int(input())
# i = 1

# while i <=n:
#     print(i)
#     i = i+2
# print(i)

# while True:
#     cmd = input("cmd> ")
#     if cmd == "quit":
#             print("bye")
#             break
#     print("you said:", cmd)


# i = 0 
# while True:
#     print(i)
#     i =i+1
#     if i == 5:
#         break
#     print(i)
# print(i)

# while True:
#     password = input("")
#     if password == "open sesame":
#         print("Unlocked")
#         break
#     else:
#         print("Wrong Password, Try again")

i = 5
while i>=0:
    password = input()
    if password != "1332":
        i = i-1
        print("Wrong password attempts remainig", i)
        if i==0:
            break
    else:
        print("Unlocked")
        break