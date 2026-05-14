class Node:
    def __init__(self, nama_pasien):
        self.data = nama_pasien
        self.next = None


class AntrianRumahSakit:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, nama):
        new_node = Node(nama)

        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node

        print(f"Pasien {nama} berhasil masuk antrian")

    def dequeue(self):
        if self.is_empty():
            print("Antrian pasien kosong")
            return

        temp = self.front_ptr
        print(f"Pasien {temp.data} dipanggil dokter")

        self.front_ptr = self.front_ptr.next

        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Antrian pasien kosong")
            return

        print(f"Pasien berikutnya: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Antrian pasien kosong")
            return

        print("Daftar antrian pasien:")

        current = self.front_ptr
        nomor = 1

        while current is not None:
            print(f"{nomor}. {current.data}")
            current = current.next
            nomor += 1


def main():
    queue = AntrianRumahSakit()
    pilih = 0

    while pilih != 5:
        print("\n=== ANTRIAN RUMAH SAKIT ===")
        print("1. Tambah Pasien")
        print("2. Panggil Pasien")
        print("3. Lihat Pasien Berikutnya")
        print("4. Tampilkan Antrian")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Masukkan nama pasien: ")
            queue.enqueue(nama)

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()