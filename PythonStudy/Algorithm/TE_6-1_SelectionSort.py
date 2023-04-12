array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):  # 배열에서 가장 작은 수 찾는 과정
    min_index = i  # 가장 작은 원소의 인덱스. 처음에 0부터 시작.
    for j in range(i+1, len(array)):  # i 번째의 다음부터 하나씩 훑으면서
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # swap

    print(array)
