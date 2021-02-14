list = []
while True:
    num = input("입력하세요")
    if num == "":
        break
    else:
        list.append(int(num))
list.sort()
print(list)

# 주말3문제풀기

num = int(input())

i = 1

while i <= num:
    print(i, i * i)
    i = i + 3
