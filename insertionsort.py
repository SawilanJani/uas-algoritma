data = [12, 45, 5, 67, 32, 66, 78, 10, 17, 9]

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

print("Data sebelum diurutkan:")
print(data)

insertion_sort_desc(data)

print("Data setelah diurutkan (besar ke kecil):")
print(data)
