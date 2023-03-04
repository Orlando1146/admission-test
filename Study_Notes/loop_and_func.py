# str format
a = 5
str1 = f"a + 5 = {a + 5}"
print(str1)

# continue & break
for i in range(1, 10):
    if i == 5:
        continue
    elif i == 7:
        break
    print(f"i = {i}")
# 函式
def co(a, b):
    print(f"a + b = {a+b}")
co(3, 4)

# 從1加到100的和(用while)
a = 1
sum = 0
while a <= 100:
    sum += a
    a += 1

print(f"sum = {sum}")

for i in range(10):  #從0到9
    print(i)

for i in range(1, 11):  #從1到10
    print(i)

for i in range(0, 10, 2):  #從0到<10，每次+2
    print(i)

# 九九乘法表
for a in range(1, 10):
    for b in range(1, 10):
        print(f"{a} * {b} = {a * b}")

