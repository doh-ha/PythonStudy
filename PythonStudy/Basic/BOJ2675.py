#2675 문자열 반복
num=int(input()) 
for i in range(num):
    r,s=input().split() 
    r=int(r)
    for j in range(len(s)):
        print(s[j]*r, end="")
    print()
                   
        