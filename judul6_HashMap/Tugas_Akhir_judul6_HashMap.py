class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return key % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state in [SlotState.EMPTY, SlotState.DELETED]:
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True

            elif self.table[i].key == key:
                self.table[i].value = value
                return True

        return False

    def search(self, key):
        idx = self.hash_function(key)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].key == key):
                return self.table[i]

        return None

    def display(self):
        print("\n=== DAFTAR INVENTARIS ===")

        for i in range(self.SIZE):
            if self.table[i].state == SlotState.OCCUPIED:
                barang = self.table[i].value

                print(f"""
Slot : {i}
Kode : {self.table[i].key}
Nama : {barang['nama']}
Stok : {barang['stok']}
-------------------------
""")


def main():
    inventaris = HashMapOpenAddressing(10)

    while True:
        print("\n=== MENU INVENTARIS GUDANG ===")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Cari Barang")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            kode = int(input("Kode Barang (angka): "))
            nama = input("Nama Barang: ")
            stok = int(input("Stok Barang: "))

            data_barang = {
                "nama": nama,
                "stok": stok
            }

            if inventaris.insert(kode, data_barang):
                print("Barang berhasil ditambahkan.")
            else:
                print("Hash Table penuh!")

        elif pilihan == "2":
            inventaris.display()

        elif pilihan == "3":
            kode = int(input("Masukkan kode barang: "))

            hasil = inventaris.search(kode)

            if hasil:
                barang = hasil.value

                print("\n=== DATA BARANG ===")
                print("Kode :", hasil.key)
                print("Nama :", barang["nama"])
                print("Stok :", barang["stok"])
            else:
                print("Barang tidak ditemukan.")

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()