"""
NAMA    : I KADEK RIZKY DWITAMA WIDIASA
NIM     : 1301204035
Kelas   : IF-44-06
"""

def totalKemunculan(List):
    return {item:List.count(item) for item in List}

List = ["danu", "danu", "alif", "indra", "indra", "kurniadi", "indra"]
print(totalKemunculan(List))
