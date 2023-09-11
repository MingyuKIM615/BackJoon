# 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
x = A * B * C
cnt_0 = 0
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0
cnt_5 = 0
cnt_6 = 0
cnt_7 = 0
cnt_8 = 0
cnt_9 = 0
while x >= 1:
    if x % 10 == 0:
        cnt_0 += 1
    elif x % 10 == 1:
        cnt_1 += 1
    elif x % 10 == 2:
        cnt_2 += 1
    elif x % 10 == 3:
        cnt_3 += 1
    elif x % 10 == 4:
        cnt_4 += 1
    elif x % 10 == 5:
        cnt_5 += 1
    elif x % 10 == 6:
        cnt_6 += 1
    elif x % 10 == 7:
        cnt_7 += 1
    elif x % 10 == 8:
        cnt_8 += 1
    else:
        cnt_9 += 1
    x = int(x / 10)

list = [cnt_0, cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, cnt_6, cnt_7, cnt_8, cnt_9]
for i in list:
    print(i)
