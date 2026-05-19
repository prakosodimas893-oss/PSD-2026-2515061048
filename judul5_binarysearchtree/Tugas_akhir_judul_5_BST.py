class Node:
    def __init__(self, nama, skor):
        self.nama = nama
        self.skor = skor
        self.left = None
        self.right = None


class LeaderboardBST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nama, skor):
        if root is None:
            return Node(nama, skor)

        if skor < root.skor:
            root.left = self.insert_node(root.left, nama, skor)

        elif skor > root.skor:
            root.right = self.insert_node(root.right, nama, skor)

        return root

    def insert(self, nama, skor):
        self.root = self.insert_node(self.root, nama, skor)

    def search_score(self, root, skor):
        if root is None:
            return None

        if root.skor == skor:
            return root

        if skor < root.skor:
            return self.search_score(root.left, skor)

        return self.search_score(root.right, skor)

    def search(self, skor):
        return self.search_score(self.root, skor)

    def find_min_node(self, root):
        current = root

        while current is not None and current.left is not None:
            current = current.left

        return current

    def delete_node(self, root, skor):
        if root is None:
            return None

        if skor < root.skor:
            root.left = self.delete_node(root.left, skor)

        elif skor > root.skor:
            root.right = self.delete_node(root.right, skor)

        else:
            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                successor = self.find_min_node(root.right)

                root.nama = successor.nama
                root.skor = successor.skor

                root.right = self.delete_node(root.right, successor.skor)

        return root

    def delete(self, skor):
        self.root = self.delete_node(self.root, skor)

    def show_ranking_desc(self, root):
        if root is None:
            return

        self.show_ranking_desc(root.right)

        print(f"{root.nama} : {root.skor}")

        self.show_ranking_desc(root.left)

    def show_ranking_asc(self, root):
        if root is None:
            return

        self.show_ranking_asc(root.left)

        print(f"{root.nama} : {root.skor}")

        self.show_ranking_asc(root.right)

    def find_highest(self, root):
        if root is None:
            return None

        current = root

        while current.right is not None:
            current = current.right

        return current

    def find_lowest(self, root):
        if root is None:
            return None

        current = root

        while current.left is not None:
            current = current.left

        return current

    def count_player(self, root):
        if root is None:
            return 0

        return 1 + self.count_player(root.left) + self.count_player(root.right)


def main():
    bst = LeaderboardBST()

    pilih = 0

    while pilih != 8:
        print("\n=== Leaderboard BST ===")
        print("1. Tambah player")
        print("2. Hapus player")
        print("3. Cari skor")
        print("4. Ranking tertinggi")
        print("5. Ranking terendah")
        print("6. Skor tertinggi")
        print("7. Jumlah player")
        print("8. Keluar")

        try:
            pilih = int(input("Pilih: "))

        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                nama = input("Masukkan nama: ")
                skor = int(input("Masukkan skor: "))

                bst.insert(nama, skor)

                print("Player berhasil ditambahkan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                skor = int(input("Masukkan skor yang dihapus: "))

                bst.delete(skor)

                print("Player berhasil dihapus")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            try:
                skor = int(input("Cari skor: "))

                hasil = bst.search(skor)

                if hasil is not None:
                    print(f"Player ditemukan: {hasil.nama} : {hasil.skor}")

                else:
                    print("Skor tidak ditemukan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 4:
            print("\n=== Ranking Tertinggi ===")

            bst.show_ranking_desc(bst.root)

        elif pilih == 5:
            print("\n=== Ranking Terendah ===")

            bst.show_ranking_asc(bst.root)

        elif pilih == 6:
            highest = bst.find_highest(bst.root)

            if highest is not None:
                print(f"Skor tertinggi: {highest.nama} : {highest.skor}")

            else:
                print("Leaderboard kosong")

        elif pilih == 7:
            print(f"Jumlah player: {bst.count_player(bst.root)}")

        elif pilih == 8:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()