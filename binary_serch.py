#Binary Search adalah algoritma pencarian yang digunakan untuk menemukan elemen dalam 
# array atau daftar yang sudah diurutkan. Algoritma ini bekerja dengan prinsip divide 
# and conquer, di mana kita membagi daftar menjadi dua bagian, kemudian menentukan di 
# bagian mana elemen yang dicari berada, dan mengabaikan bagian lainnya. Proses ini
# diulangi sampai elemen yang dicari ditemukan atau sampai sub-list yang diperiksa habis.


#contoh


def binary_search (arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1



arr = [1,5,8,9,11,14,17,20,24]
result = binary_search(arr,24)

if result != -1:
    print(f"Elemen ditemukan di indeks {result}")
else:
    print("Elemen tidak ditemukan")