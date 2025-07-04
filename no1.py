input_angka = int(input("Masukkan bilangan: "))

bilangan_ganjil_kelipatan_3 = []

for i in range(3, input_angka + 1, 3):
    
    bilangan_ganjil_kelipatan_3.append(i)

print("Bilangan ganjil berkelipatan 3 dari", input_angka, "adalah:")
for number in bilangan_ganjil_kelipatan_3:
    print(number, end =" ")