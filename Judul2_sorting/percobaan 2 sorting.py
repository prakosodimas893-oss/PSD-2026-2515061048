def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j][1] < arr[j + 1][1]:  
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah siswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan nama dan nilai siswa:")

    for i in range(n):
        nama = input("Nama: ")
        while True:
            try:
                nilai = int(input("Nilai: "))
                arr.append((nama, nilai))  # simpan tuple
                break
            except ValueError:
                print("Input nilai harus angka!")

    print("\nData sebelum diurutkan:")
    for data in arr:
        print(data[0], "-", data[1])

    bubble_sort(arr, n)

    print("\nData setelah diurutkan (berdasarkan nilai tertinggi):")
    for data in arr:
        print(data[0], "-", data[1])


if __name__ == "__main__":
    main()