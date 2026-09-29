# names = "Python"
# scores = [95, 87, 92]
# tags = {"Python", "AI", "Beginner"}
# print(names[1])
# print(scores[1])
# print(tags[1])

# print(type("hello"))
# print(type([1, 2, 3]))
# print(type({1, 2, 3}))

# print(type({})) 
# print(type(set()))

# s = {1, 2, 3}
# s.add(42)
# s.add("hello")
# s.add((10, 20))
# s.add([1, 2])
# print(s)

# print(hash((1, [2, 3])))

# mixed = [42, "hello", True, 3.14, [1, 2, 3]]
# print(len(mixed))
# print(type(mixed[0]))
# print(type(mixed[1]))
# print(type(mixed[4]))

# coords = {(0, 0), (1, 2), (3, 4), (1, 2)}
# print(coords)
# print(len(coords))

# a = input("Enter string")
# if len(a)%2 ==0:
#     b = len(a)//2
#     c = len(a)//2 - 1
#     print(a[:3]+ a[b]+a[c] +a[-3:-1])
# else:
#     b = len(a)//2
#     print(a[:3]+ a[b]+a[-3:-1])



# msg = "hello world"
# print(msg.replace("world", "Python"))
# print(msg.replace("l", "L"))
# print(msg)

# raw = " HELLO, world! "
# print(raw.strip().lower())

# print(ord('A'))
# print(ord('a'))
# print(ord('0'))
# print(chr(65))
# print(chr(97))
# print(chr(66))

# print(ord("""))

# print(chr(ord('A') + 3))
# print(chr(ord('z') - 25))

# t = ("Alice", 95, True, 3.14)
# print(t[0])
# print(t[-1])
# print(t[1:3])
# print(len(t))

# lst = [10, 20, 30]
# lst.append(40)
# lst.append(50)
# print(lst)

# lst = [10, 20, 30, 40, 50]
# x = lst.pop()
# print(x)
# print(lst)
# y = lst.pop(1)
# print(y)
# print(lst)

# lst = [10, 20, 30, 20, 40]
# lst.remove(20)
# print(lst)
# lst.remove(99)

# nums = [3, 1, 4, 1, 5, 9, 2]
# new = sorted(nums)
# print(new)
# print(nums)
# nums.sort()
# print(nums)

# nums = [3, 1, 4]
# result = nums.sort()
# print(result)
# print(nums)

# # Block A — string
# s = "hello"
# s[0] = "H"

# Block B — list
lst = [30, 10, 20]
lst[0] = 99
lst.sort()
print(lst)
