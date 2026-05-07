                      PROGRAM PENCARIAN PRODUK E-COMMERCE MENGGUNAKAN INTERPOLATION SEARCH
Program ini merupakan program pencarian produk pada sistem e-commerce menggunakan algoritma interpolation search. Program menyimpan data produk berupa nama dan harga yang sudah diurutkan berdasarkan harga. Pengguna dapat memasukkan harga produk yang ingin dicari, kemudian program akan memperkirakan posisi data menggunakan perhitungan interpolation search agar proses pencarian menjadi lebih cepat dan efisien dibanding pencarian biasa.
Pada program ini, jika harga produk ditemukan maka sistem akan menampilkan nama produk beserta harganya. Namun jika harga yang dicari tidak tersedia, program akan menampilkan pesan bahwa produk tidak ditemukan. Program ini cocok digunakan dalam sistem e-commerce karena mampu membantu proses pencarian produk berdasarkan harga dengan lebih cepat pada data yang sudah terurut.
![GAMBAR](sscode.png)

def interpolation_search(data, n, target):
Baris ini digunakan untuk membuat fungsi interpolation search. Fungsi memiliki parameter data sebagai daftar produk, n sebagai jumlah data, dan target sebagai harga produk yang ingin dicari.

low = 0
Variabel low digunakan sebagai batas bawah pencarian dan dimulai dari indeks pertama array.

high = n - 1
Variabel high digunakan sebagai batas atas pencarian yaitu indeks terakhir array.

while low <= high and target >= data[low]['harga'] and target <= data[high]['harga']:
Perulangan akan berjalan selama batas pencarian masih valid dan target berada di antara harga terendah dan tertinggi.

if data[high]['harga'] == data[low]['harga']:
Kondisi ini digunakan untuk mencegah pembagian dengan nol ketika harga batas atas dan bawah sama.

if data[low]['harga'] == target:
Program mengecek apakah harga target sama dengan harga pada posisi low.

return low
Jika ditemukan, fungsi mengembalikan indeks data.

break
Jika harga tidak sama, perulangan dihentikan.

pos = low + int(((target - data[low]['harga']) / (data[high]['harga'] - data[low]['harga'])) * (high - low))
Baris ini digunakan untuk menghitung posisi estimasi data menggunakan rumus interpolation search. Program memperkirakan lokasi data berdasarkan nilai target.

print(f"Posisi estimasi: {pos}, harga: {data[pos]['harga']}")
Program menampilkan posisi hasil estimasi beserta harga pada posisi tersebut.

if target > data[pos]['harga']:
Program mengecek apakah target lebih besar dari harga pada posisi estimasi.

low = pos + 1
Jika target lebih besar, pencarian dipindahkan ke bagian kanan array.

elif target < data[pos]['harga']:
Program mengecek apakah target lebih kecil dari harga pada posisi estimasi.

high = pos - 1
Jika target lebih kecil, pencarian dipindahkan ke bagian kiri array.

else:
Jika kedua kondisi sebelumnya salah, berarti target ditemukan.

return pos
Program mengembalikan posisi data yang ditemukan.

if low < n and data[low]['harga'] == target:
Pengecekan tambahan untuk memastikan apakah target ditemukan pada posisi low.

return low
Jika ditemukan, indeks dikembalikan.

return -1
Jika data tidak ditemukan, fungsi mengembalikan -1.

def main():
Fungsi utama program dimulai dari sini.

data = [
Membuat list data produk.

{"nama": "Mouse", "harga": 50000},
Data produk pertama berisi nama produk dan harga.

{"nama": "Keyboard", "harga": 100000},
Data produk keyboard dengan harga 100000.

{"nama": "Headset", "harga": 150000},
Data produk headset dengan harga 150000.

{"nama": "Flashdisk", "harga": 200000},
Data produk flashdisk dengan harga 200000.

{"nama": "SSD", "harga": 300000},
Data produk SSD dengan harga 300000.

{"nama": "Monitor", "harga": 500000},
Data produk monitor dengan harga 500000.

{"nama": "Printer", "harga": 700000},
Data produk printer dengan harga 700000.

{"nama": "Laptop", "harga": 1000000}
Data produk laptop dengan harga 1000000.

]
Penutup list data produk.

n = len(data)
Menghitung jumlah seluruh data produk.

print("Daftar Produk (urut harga):")
Menampilkan judul daftar produk.

for item in data:
Perulangan untuk mengambil setiap data produk.

print(f"{item['nama']} - Rp{item['harga']}")
Menampilkan nama dan harga produk.

while True:
Perulangan digunakan agar input terus diminta sampai valid.

try:
Blok try digunakan untuk menangani error input.

target = int(input("\nMasukkan harga yang ingin dicari: "))
Pengguna memasukkan harga produk yang ingin dicari.

break
Jika input valid, perulangan dihentikan.

except ValueError:
Menangani error jika input bukan angka.

print("Input tidak valid, masukkan angka!")
Program menampilkan pesan kesalahan.

pos = interpolation_search(data, n, target)
Memanggil fungsi interpolation search untuk mencari harga produk.

if pos != -1:
Mengecek apakah data ditemukan.

print(f"\nProduk ditemukan:")
Menampilkan pesan bahwa produk ditemukan.

print(f"Nama: {data[pos]['nama']}")
Menampilkan nama produk.

print(f"Harga: Rp{data[pos]['harga']}")
Menampilkan harga produk.

else:
Jika produk tidak ditemukan.

print("\nProduk dengan harga tersebut tidak ditemukan")
Menampilkan pesan bahwa produk tidak tersedia.

if __name__ == "__main__":
Digunakan agar fungsi main() hanya berjalan jika file dijalankan langsung.

main()
Memanggil fungsi utama program.

![GAMBAR](ssoutput.png)

