arr=[[None for i in range(5)] for j in range(5)]

print("Original Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()

arr[1][2]=16

print("Modified Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()
