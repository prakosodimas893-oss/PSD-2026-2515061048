#play list lagu
def menu():
    print("1. Tampilkan semua lagu dalam playlist")
    print("2. Tampilkan index dan lagu")
    print("3. Masukkan lagu ke dalam playlist")
    print("4. Cari lagu")
    print("5. Keluar")


def main():
    playlist = ["-" for _ in range(5)]  # playlist dengan 5 slot
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print("Playlist saat ini:")
            for lagu in playlist:
                print(lagu)

        elif choice == 2:
            print("Index dan lagu:")
            for i in range(len(playlist)):
                print(f"Index {i}: {playlist[i]}")

        elif choice == 3:
            print("Masukkan lagu ke dalam playlist:")
            for i in range(len(playlist)):
                lagu = input(f"Lagu ke-{i}: ")
                playlist[i] = lagu
            print("Playlist berhasil diupdate!")

        elif choice == 4:
            cari = input("Masukkan nama lagu yang ingin dicari: ")
            ditemukan = False
            for i in range(len(playlist)):
                if playlist[i].lower() == cari.lower():
                    print(f"Lagu ditemukan di index {i}")
                    ditemukan = True
            if not ditemukan:
                print("Lagu tidak ditemukan!")

        elif choice == 5:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()