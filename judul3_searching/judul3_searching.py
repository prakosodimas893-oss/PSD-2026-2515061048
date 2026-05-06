def interpolation_search(data, n, target):
    low = 0
    high = n - 1

    while low <= high and target >= data[low]['harga'] and target <= data[high]['harga']:
        if data[high]['harga'] == data[low]['harga']:
            if data[low]['harga'] == target:
                return low
            break

        pos = low + int(((target - data[low]['harga']) / 
                        (data[high]['harga'] - data[low]['harga'])) * (high - low))

        print(f"Posisi barang ada di etalase nomer {pos}, dengan harga: {data[pos]['harga']}")

        if target > data[pos]['harga']:
            low = pos + 1
        elif target < data[pos]['harga']:
            high = pos - 1
        else:
            return pos

    if low < n and data[low]['harga'] == target:
        return low

    return -1


def main():
    # Data produk (HARUS sudah terurut berdasarkan harga)
    data = [
        {"nama": "Mouse", "harga": 50000},
        {"nama": "Keyboard", "harga": 100000},
        {"nama": "Headset", "harga": 150000},
        {"nama": "Flashdisk", "harga": 200000},
        {"nama": "SSD", "harga": 300000},
        {"nama": "Monitor", "harga": 500000},
        {"nama": "Printer", "harga": 700000},
        {"nama": "Laptop", "harga": 1000000}
    ]

    n = len(data)

    print("Daftar Produk (urut harga):")
    for item in data:
        print(f"{item['nama']} - Rp{item['harga']}")

    while True:
        try:
            target = int(input("\nMasukkan harga yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, masukkan angka!")

    pos = interpolation_search(data, n, target)

    if pos != -1:
        print(f"\nProduk ditemukan:")
        print(f"Nama: {data[pos]['nama']}")
        print(f"Harga: Rp{data[pos]['harga']}")
    else:
        print("\nProduk dengan harga tersebut tidak ditemukan")


if __name__ == "__main__":
    main()