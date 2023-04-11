
a, b, c = map(int, input().split())
array = []
array.append(a)
array.append(b)
array.append(c)


array.sort(reverse=True)


print(array[1])
