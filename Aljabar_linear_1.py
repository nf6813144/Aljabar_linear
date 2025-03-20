# Membuat List
print("_"*45)
cth_list = [5, "enam", 7,8,0,True]
print("ini adalah list:")
print(cth_list)
print("\n")
# Mengedintifikasi elemen list
print("elemen kedua dari list tersebut adalah ", cth_list [1])

# Membuat matriks list 
matriks_list = [[7,8,9],
                [10,11,12]]
print("ini adalah matriks dari list")
print(matriks_list)
print("elemen matriks baris kesatu kolom ke dua:",matriks_list[0][1])
print("\n")


import numpy as np
# Membuat Array
cth_array = np.array([7,8,9,10,11])
print("ini adalah array:")
print(cth_array)

# Membuar matriks menggunakan Array
matriks_array =np.array ([[-2,1,-1],
                  [-3,-1,2],
                  [-2,1,2]])
print("ini adalah matriks dari array")
print(matriks_array)
print("elemen matriks baris ketiga kolom kedua: ", matriks_array[2][1])
