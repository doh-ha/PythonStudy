# 성적이 낮은 순서로 학생 출력하기

# 입력:
# 2
# 홍길동 95
# 이순신 77

# 출력:
# 이순신 홍길동


n = int(input())
array = []
for i in range(n):
    input_data = input().split()  # 바로 리스트가 됨!
    print("이것은 리스트인가요?", input_data)

    isItTuple = (input_data[0], int(input_data[1]))
    print("이것은 튜플인가요?", isItTuple)

    array.append((input_data[0], int(input_data[1])))
    # append 의 인자는 하나여야 함. 그래서 괄호로 묶어줌

print(array)
