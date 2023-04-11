#9036 문자열
num=int(input())
for i in range(num):
    string=input()
    ans=string[0]+string[-1]
    print(ans.strip())