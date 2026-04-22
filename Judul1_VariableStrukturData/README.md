# Program Playlist Lagu

Program ini merupakan implementasi struktur data list dalam bahasa Python dengan konsep playlist lagu. Program dibuat menggunakan sistem menu interaktif sehingga pengguna dapat memilih berbagai fitur yang tersedia, seperti menampilkan daftar lagu, melihat index lagu, serta menambahkan lagu ke dalam playlist.

Selain itu, program ini juga memiliki fitur pencarian lagu yang memungkinkan pengguna mencari lagu berdasarkan nama. Program akan mengecek setiap data dalam list, kemudian menampilkan index lagu jika ditemukan, atau memberikan pesan jika lagu tidak tersedia. Program ini bertujuan untuk membantu memahami konsep dasar list, perulangan (looping), percabangan (if-else), serta interaksi input dan output dalam Python.



  ![Tampilan](tampilan1.png)
  # Penjelasan Kode Program Playlist Lagu

Berikut adalah penjelasan setiap baris kode pada program playlist lagu:

## Fungsi Menu

def menu():
Digunakan untuk mendefinisikan fungsi menu yang akan menampilkan pilihan kepada pengguna.

print("1. Tampilkan semua lagu dalam playlist")
Menampilkan pilihan untuk melihat semua lagu dalam playlist.

print("2. Tampilkan index dan lagu")
Menampilkan pilihan untuk melihat index dan isi lagu.

print("3. Masukkan lagu ke dalam playlist")
Menampilkan pilihan untuk menambahkan lagu ke dalam playlist.

print("4. Cari lagu")
Menampilkan pilihan untuk mencari lagu dalam playlist.

print("5. Keluar")
Menampilkan pilihan untuk keluar dari program.

## Fungsi Utama

def main():
Mendefinisikan fungsi utama sebagai pusat jalannya program.

playlist = ["-" for _ in range(5)]
Membuat list dengan 5 elemen awal berupa "-" sebagai tanda kosong.

running = True
Variabel kontrol untuk menjalankan perulangan program.

while running:
Perulangan utama yang akan terus berjalan selama running bernilai True.

menu()
Memanggil fungsi menu untuk ditampilkan ke pengguna.

try:
Memulai blok penanganan error.

choice = int(input("Pilihan: "))
Menerima input dari pengguna dan mengubahnya menjadi integer.

except ValueError:
Menangkap error jika input bukan angka.

print("Masukkan angka yang valid!")
Menampilkan pesan kesalahan jika input tidak valid.

continue
Mengulang kembali ke awal perulangan.

## Menu 1

if choice == 1:
Memeriksa apakah pengguna memilih menu 1.

print("Playlist saat ini:")
Menampilkan judul output.

for lagu in playlist:
Perulangan untuk setiap lagu dalam playlist.

print(lagu)
Menampilkan isi lagu satu per satu.

## Menu 2

elif choice == 2:
Memeriksa apakah pengguna memilih menu 2.

print("Index dan lagu:")
Menampilkan judul output.

for i in range(len(playlist)):
Perulangan berdasarkan jumlah index.

print(f"Index {i}: {playlist[i]}")
Menampilkan index dan lagu.

## Menu 3

elif choice == 3:
Memeriksa apakah pengguna memilih menu 3.

print("Masukkan lagu ke dalam playlist:")
Menampilkan instruksi input.

for i in range(len(playlist)):
Perulangan untuk setiap posisi dalam playlist.

lagu = input(f"Lagu ke-{i}: ")
Mengambil input lagu dari pengguna.

playlist[i] = lagu
Menyimpan lagu ke dalam list.

print("Playlist berhasil diupdate!")
Menampilkan pesan berhasil.

## Menu 4

elif choice == 4:
Memeriksa apakah pengguna memilih menu 4.

cari = input("Masukkan nama lagu yang ingin dicari: ")
Mengambil input lagu yang ingin dicari.

ditemukan = False
Variabel penanda apakah lagu ditemukan atau tidak.

for i in range(len(playlist)):
Perulangan untuk mengecek semua data.

if playlist[i].lower() == cari.lower():
Membandingkan data tanpa memperhatikan huruf besar/kecil.

print(f"Lagu ditemukan di index {i}")
Menampilkan hasil pencarian.

ditemukan = True
Menandai bahwa lagu ditemukan.

if not ditemukan:
print("Lagu tidak ditemukan!")
Menampilkan pesan jika lagu tidak ada.

## Menu 5

elif choice == 5:
Memeriksa apakah pengguna memilih keluar.

running = False
Menghentikan perulangan.

print("Program selesai.")
Menampilkan pesan keluar.

## Pilihan Tidak Valid

else:
print("Pilihan tidak valid!")
Menampilkan pesan jika pilihan tidak tersedia.

## Menjalankan Program

if **name** == "**main**":
Memastikan program dijalankan langsung, bukan dari file lain.

main()
Memanggil fungsi utama untuk menjalankan program.

#output sekaligus penjelsasan
  ![Tampilan](tampilan2.png)
  Saat program dijalankan, pengguna akan melihat beberapa pilihan menu seperti menampilkan playlist, melihat index lagu, menambahkan lagu, mencari lagu, dan keluar dari program. Program akan terus berjalan dan menampilkan menu selama pengguna belum memilih opsi keluar.

Jika pengguna memilih menu untuk menampilkan playlist, maka program akan menampilkan semua isi list lagu yang tersedia. Pada awal program, isi playlist masih berupa tanda "-" sebagai penanda bahwa data masih kosong. Jika pengguna memilih untuk menampilkan index dan lagu, maka program akan menampilkan posisi index beserta isi lagu pada setiap slot dalam list.

Ketika pengguna memilih menu untuk memasukkan lagu, program akan meminta input lagu satu per satu sesuai jumlah slot yang tersedia, kemudian menampilkan hasil playlist yang sudah diperbarui. Jika pengguna memilih menu pencarian, program akan meminta nama lagu yang ingin dicari, lalu menampilkan index lagu tersebut jika ditemukan, atau menampilkan pesan bahwa lagu tidak ditemukan jika tidak ada dalam playlist.

Jika pengguna memilih menu keluar, maka program akan berhenti dan menampilkan pesan "Program selesai.". Apabila pengguna memasukkan pilihan yang tidak sesuai atau bukan angka, maka program akan menampilkan pesan kesalahan dan meminta input ulang.



  https://youtu.be/s572qth6l7M?si=Fo6SPhWJiyZ3bBL2



