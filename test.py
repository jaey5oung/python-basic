num = int(input("인풋창"))

for i in range(1, num):
    if num % i == 0:
        print(i)


#range는 range(시작숫자,종료숫자)의 형태로 js에선 슬라이스와유사함.

#1.숫자타입으로 int=정수를 인풋창으로띄우고싶다
#2.반복문으로 i라는 변수에 1~num까지 range를 돌릴때
#3.만약 정수를 나눳을때 나머지가 0이되는것을 구한다
#4.마지막 i를 프린트로 출력한다


