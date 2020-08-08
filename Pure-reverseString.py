string1 = 'hello'
#print(string1[::-1])

arr = list(string1)

j = len(arr) - 1
len_arr = len(arr) // 2
print(j)
for i in range(len_arr):
    arr[i], arr[j] = arr[j], arr[i]
    #temp = arr[i]
    #arr[i] = arr[j]
    #arr[j] = temp
    j -= 1
    
print(arr)
