 # NAMA : Mutia Risnawati 
 # NIM : 2603069

# Soal 1
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
buah[2]="cherry"
print(buah)

#  Soal 2    
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
nama_buah = input("Masukkan nama buah yang ingin ditambahkan: ")
index = int(input("Masukkan index buah yang ingin ditambahkan: "))
buah.insert(index, nama_buah)
print("daftar buah setelah ditambahkan:", buah)

# Soal 3
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
buah.sort()
print(buah)

# Soal 4
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga","kiwi"]
nama_buah = input("Masukkan nama buah yang ingin dihapus: ")
if nama_buah in buah:
    buah.remove(nama_buah)
    print("Daftar buah setelah dihapus:", buah)
else:
    print("Buah tidak ditemukan!")