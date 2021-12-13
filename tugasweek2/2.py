"""
NAMA    : I KADEK RIZKY DWITAMA WIDIASA
NIM     : 1301204035
Kelas   : IF-44-06
"""

def menghitungTarget(arr, n, target):
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return arr[i-1], arr[j-1]
arr = [1, 2, 3, 4, 6] #silahkan input array
n = len(arr)
target = 6 #silahkan input target
print(menghitungTarget(arr, n, target))

