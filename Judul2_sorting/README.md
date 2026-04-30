PENGURUTAN NILAI SISWA 
Kode ini adalah program Python untuk mengurutkan data siswa berdasarkan nilai menggunakan metode Bubble Sort. Program dimulai dengan fungsi tukar yang berfungsi menukar posisi dua elemen dalam array. Data siswa disimpan dalam bentuk tuple (nama, nilai) di dalam list arr. Pada fungsi main, user diminta memasukkan jumlah siswa, lalu memasukkan nama dan nilai masing-masing siswa. Input nilai dilindungi dengan try-except agar hanya menerima angka. Setelah semua data masuk, program menampilkan data sebelum diurutkan.

Proses pengurutan dilakukan oleh fungsi bubble_sort, yang membandingkan nilai dari setiap pasangan data menggunakan arr[j][1]. Jika nilai lebih kecil dari elemen berikutnya, maka ditukar, sehingga hasil akhirnya adalah urutan dari nilai terbesar ke terkecil (descending). Setelah proses sorting selesai, program menampilkan kembali data siswa yang sudah diurutkan berdasarkan nilai tertinggi. Struktur ini menunjukkan bagaimana array bisa menyimpan data kompleks dan bagaimana algoritma sorting diterapkan pada data tersebut.
def tukar(arr, i, j)
ini digunakan untuk membuat fungsi menukar dua data dalam array
tampilan1.png

temp = arr[i]
ini digunakan untuk menyimpan nilai index i sementara

arr[i] = arr[j]
ini digunakan untuk mengganti nilai index i dengan nilai index j

arr[j] = temp
ini digunakan untuk mengisi index j dengan nilai lama dari i

def bubble_sort(arr, n)
ini digunakan untuk membuat fungsi pengurutan bubble sort

for i in range(n - 1)
ini digunakan untuk perulangan tahap pengurutan sebanyak n-1

for j in range(n - i - 1)
ini digunakan untuk membandingkan elemen yang belum terurut

if arr[j][1] < arr[j + 1][1]
ini digunakan untuk membandingkan nilai (index ke-1), jika lebih kecil maka ditukar (descending)

tukar(arr, j, j + 1)
ini digunakan untuk menukar posisi data

def main()
ini digunakan untuk membuat fungsi utama program

try
ini digunakan untuk mencoba input agar tidak error

n = int(input("Masukkan jumlah siswa: "))
ini digunakan untuk memasukkan jumlah siswa

except ValueError
ini digunakan untuk menangani error jika input bukan angka

print("Input tidak valid!")
ini digunakan untuk menampilkan pesan error

return
ini digunakan untuk menghentikan program

arr = []
ini digunakan untuk membuat list kosong

print("Masukkan nama dan nilai siswa:")
ini digunakan untuk menampilkan instruksi

for i in range(n)
ini digunakan untuk perulangan input data

nama = input("Nama: ")
ini digunakan untuk memasukkan nama siswa

while True
ini digunakan untuk memastikan input nilai valid

try
ini digunakan untuk mencoba input nilai

nilai = int(input("Nilai: "))
ini digunakan untuk memasukkan nilai siswa

arr.append((nama, nilai))
ini digunakan untuk menyimpan data nama dan nilai ke dalam list

break
ini digunakan untuk keluar dari perulangan jika berhasil

except ValueError
ini digunakan untuk menangani error input nilai

print("Input nilai harus angka!")
ini digunakan untuk menampilkan pesan error

print("\nData sebelum diurutkan:")
ini digunakan untuk menampilkan data sebelum sorting

for data in arr
ini digunakan untuk membaca setiap data

print(data[0], "-", data[1])
ini digunakan untuk menampilkan nama dan nilai

bubble_sort(arr, n)
ini digunakan untuk memanggil fungsi sorting

print("\nData setelah diurutkan (berdasarkan nilai tertinggi):")
ini digunakan untuk menampilkan hasil setelah sorting

for data in arr
ini digunakan untuk menampilkan data hasil sorting

print(data[0], "-", data[1])
ini digunakan untuk menampilkan nama dan nilai setelah diurutkan

if **name** == "**main**"
ini digunakan untuk memastikan program dijalankan langsung

main()
ini digunakan untuk menjalankan program utama

tampilan2.png
Output dari program ini adalah menampilkan data siswa sebelum dan sesudah diurutkan berdasarkan nilai.

Saat program dijalankan, pengguna diminta memasukkan jumlah siswa, lalu memasukkan nama dan nilai masing-masing siswa. Data yang dimasukkan akan disimpan dalam bentuk pasangan (nama, nilai).

Program kemudian menampilkan data sebelum diurutkan, yaitu sesuai dengan urutan saat input. Setelah itu, program melakukan proses pengurutan menggunakan metode bubble sort dengan membandingkan nilai setiap siswa.

Hasil akhir yang ditampilkan adalah data siswa yang sudah diurutkan dari nilai tertinggi ke nilai terendah (descending). Jika kondisi perbandingan diubah, maka urutan bisa menjadi dari nilai terendah ke tertinggi (ascending).

https://youtu.be/uGXpBRV_Yyg
