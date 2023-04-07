# 2480 주사위 세 개
a, b, c = map(int, input().split())
money = 0

if a == b and b == c:  # 모두 같을 때
    money = 10000+a*1000

elif a == b or a == c:
    money = 1000+a*100
elif b == c:
    money = 1000+c*100
else:
    money = max(a, b, c)*100

print(money)
'''
나의 첫 풀이
a, b, c = map(int, input().split())
money = 0


if a == b and b == c:  # 모두 같을 때
    money = 10000+a*1000


elif a-b == 0:
    money = 1000+a*100
elif a-c == 0:
    money = 1000+a*100
elif c-b == 0:
    money = 1000+c*100

else:  # 모두 다를 때
    biggest_num = 0
    if a > b and a > c:
        biggest_num = a
    elif b > a and b > c:
        biggest_num = b
    else:
        biggest_num = c
    money = biggest_num * 100

print(money)
'''

# 숏코딩
# *_,a,b,c=sorted(input());print(['1'+b,c][a<b<c]+'000'[a<c:])
