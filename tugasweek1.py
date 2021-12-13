"""
TUGAS 1
NAMA    : I KADEK RIZKY DWITAMA WIDIASA
NIM     : 1301204035
Kelas   : IF-44-06
"""

#1 Half Pyramid Pattern
print("Half Pyramid Pattern:\n")
a = 1
while a < 6:
    print("* " * a)
    a += 1
print()

#2 Half Inverted Pyramid Pattern
print("Half Inverted Pyramid Pattern:\n")
for b in range(5, 0, -1):
    print("* " * b)
print()

#3. Half Pyramid Pattern Mirrored
print("Half Pyramid Pattern Mirrored:\n")
d = 5
for c in range(1, d+1):
    print("  " * (d-c) + "* " * c)
print()

#4. Full Pyramid Pattern
print("Full Pyramid Pattern:\n")
f = 5
for e in range(1, f+1):
    print(" " * (f-e) + "* " * e)
print()

#5. Full pyramid pattern mirrored
print("Full pyramid pattern mirrored:\n")
h = 5
for g in range(h, 0, -1): 
    print(" " * (h - g) + "* " * g)
print()
