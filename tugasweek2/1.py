"""
NAMA    : I KADEK RIZKY DWITAMA WIDIASA
NIM     : 1301204035
Kelas   : IF-44-06
"""

def angkaMunculSekali(angka):
    list = []
    list.extend(angka)
    return [i for i in list if list.count(i) < 2]
    
angka = input()
print(angkaMunculSekali(angka))
