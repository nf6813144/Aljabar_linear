# Membuat matriks list 
matriks_list = [[7,8,9],
                [10,11,12]]
print("ini adalah matriks dari list")
print(matriks_list)
print("elemen matriks baris kesatu kolom ke dua:",matriks_list[0][1])
print("\n")


import numpy as np
#Membuat Array
cth_array = np.array([7,8,9,10,11])
print("ini adalah array:")
print(cth_array)

# Membuar matriks menggunakan Array
matriks_array =np.array ([[-2,1,-1],
                  [-3,-1,2],
                  [-2,1,2]])
print("ini adalah matriks dari array")
print(matriks_array)
print("\n")
print("Elemen baris pertama kolom pertama dari matriks tersebut adalah : ",matriks_array[0][0])
print("Elemen baris kedua   kolom pertama dari matriks tersebut adalah :", matriks_array[1][0])
print("Elemen baris keriga  kolom pertama dari matriks tersebut adalah :", matriks_array[2][0])
print("\n")
print("Elemen baris pertama kolom kedua   dari matriks tersebut adalah : ",matriks_array[0][1])
print("Elemen baris kedua   kolom kedua   dari matriks tersebut adalah :", matriks_array[1][1])
print("Elemen baris ketiga  kolom kedua   dari matriks tersebut adalah : ",matriks_array[2][1])
print("\n")
print("Elemen baris kedua   kolom ketiga  dari matriks tersebut adalah : ",matriks_array[1][2])
print("Elemen baris ketiga  kolom ketiga  dari matriks tersebut adalah : ",matriks_array[2][2])
print("Elemen baris pertama kolom ketiga  dari matriks tersebut adalah :", matriks_array[0][2])
