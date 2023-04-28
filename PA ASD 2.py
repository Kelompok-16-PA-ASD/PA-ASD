from prettytable import PrettyTable
newTable = PrettyTable(["Nama", "Harga"])

class Tas:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.next = None

class TokoTas:
    def __init__(self):
        self.head = None
        self.size = 0

    # CREATE
    def tambah_tas(self, nama, harga):
        tas_baru = Tas(nama, harga)
        if not self.head:
            self.head = tas_baru
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = tas_baru
        print()
        print(f"Tas {nama} berhasil ditambahkan dengan harga {harga}")

    # READ
    def tampilkan_tas(self):
        if not self.head:
            print()
            print("===== Toko tas masih kosong =====")
        else:
            curr = self.head
            print()
            print('========== LIST TAS ==========')
            newTable.clear_rows()
            while curr:
                newTable.add_row([curr.nama, curr.harga])
                curr = curr.next
            print(newTable)

    # UPDATE
    def update_tas(self, nama, harga_baru):
        if not self.head:
            print()
            print("===== Toko tas masih kosong =====")
        else:
            curr = self.head
            while curr:
                if curr.nama == nama:
                    curr.harga = harga_baru
                    print()
                    print(f"Harga tas {nama} berhasil diubah menjadi {harga_baru}")
                    return
                curr = curr.next
            else:
                print()
                print(f"Tas {nama} tidak ditemukan")

    # DELETE
    def hapus_tas(self, nama):
        if not self.head:
            print()
            print("===== Toko tas masih kosong ====")
            print()
        elif self.head.nama == nama:
            self.head = self.head.next
            print()
            print(f"===== Tas {nama} berhasil dihapus =====")
        else:
            curr = self.head
            while curr.next:
                if curr.next.nama == nama:
                    curr.next = curr.next.next
                    print(f"Tas {nama} berhasil dihapus")
                    return
                curr = curr.next
            print(f"Tas {nama} tidak ditemukan")
    
    # QUICK SORT
    def quick_sort(self):
        self.head = self._quick_sort(self.head)
    
    def _quick_sort(self, node):
        if not node or not node.next:
            return node
        
        pivot = node
        node = node.next
        
        left_head = left_tail = None
        right_head = right_tail = None
        
        while node:
            next_node = node.next
            node.next = None
            
            if node.harga < pivot.harga:
                if not left_head:
                    left_head = left_tail = node
                else:
                    left_tail.next = node
                    left_tail = node
            else:
                if not right_head:
                    right_head = right_tail = node
                else:
                    right_tail.next = node
                    right_tail = node
                    
            node = next_node
        
        left_head = self._quick_sort(left_head)
        right_head = self._quick_sort(right_head)
        
        if left_tail:
            left_tail.next = pivot
            pivot.next = right_head
            return left_head
        else:
            pivot.next = right_head
            return pivot

    # JUMP SEARCH
    def jump_search(self, nama):
        if not self.head:
            print("Toko tas masih kosong")
            return None

        jump = int(self.size ** 0.5)
        curr = self.head
        prev = None

        while curr and curr.nama < nama:
            for i in range(jump):
                prev = curr
                curr = curr.next
                if not curr:
                    break
                if curr.nama == nama:
                    return curr

            if curr and curr.nama < nama:
                prev = curr
                curr = curr.next

        if curr and curr.nama == nama:
            return curr
        elif prev and prev.nama == nama:
            return prev
        else:
            print()
            print(f"Tas {nama} tidak ditemukan")
            return None

toko_tas = TokoTas()

# ========================================================================================================================== #
# ================================================== MENU ADMIN ============================================================ #
# ========================================================================================================================== #

def menu():
    print()
    print("===============================================")
    print("                   TOKO TAS                    ")
    print("===============================================")
    print("1. Tambah tas")
    print("2. Tampilkan tas")
    print("3. Ubah harga tas")
    print("4. Hapus tas")
    print("5. Urutkan tas (berdasarkan harga)")
    print("6. Cari tas")
    print("0. Keluar")
    print("===============================================")

    try:
        pilihan = input("Masukkan pilihan: ")
        if pilihan == '1':
            try:
                name = input("Masukkan nama tas: ")
                price = int(input("Masukkan harga tas: "))
                toko_tas.tambah_tas(name, price)
                menu()
            except:
                print()
                print('===== Invalid =====')
                menu()
                
        elif pilihan == '2':
            toko_tas.tampilkan_tas()
            menu()

        elif pilihan == '3':
            try:
                nama = input("Masukkan nama tas yang ingin diubah harganya: ")
                harga_baru = int(input("Masukkan harga baru tas: "))
                toko_tas.update_tas(nama, harga_baru)
                menu()
            except:
                print()
                print('===== Invalid =====')
                menu()

        elif pilihan == '4':
            nama_tas = input("Masukkan nama tas yang ingin dihapus: ")
            toko_tas.hapus_tas(nama_tas)
            menu()

        elif pilihan == '5':
            toko_tas.quick_sort()
            print()
            print('===== Tas berhasil diurutkan =====')
            menu()

        elif pilihan == '6':
            cari = input("Masukkan nama tas yang ingin dicari: ")
            hasil_pencarian = toko_tas.jump_search(cari)
            if hasil_pencarian:
                print()
                print(f"Tas {hasil_pencarian.nama} ditemukan dengan harga {hasil_pencarian.harga}")
                menu()
            else:
                menu()

        elif pilihan == '0':
            print()
            print("===== Terima kasih =====")
            main()

        else:
            print()
            print("===== Pilihan tidak tersedia =====")
            menu()

    except:
        print()
        print()
        print("===== Invalid =====")
        menu()

# ========================================================================================================================== #
# ================================================== MENU USER ============================================================= #
# ========================================================================================================================== #

def menu_pembeli():
    print()
    print("===============================================")
    print("           SELAMAT DATANG DI TOKO TAS          ")
    print("===============================================")
    print("1. Lihat Barang")
    print("2. Beli Barang")
    print("0. Keluar")
    print("===============================================")
    
    try:
        pilihan = input("Masukkan pilihan Anda: ")
        if pilihan == "1":
            toko_tas.tampilkan_tas()
            menu_pembeli()

        elif pilihan == "2":
            nama_tas = input("Masukkan nama tas yang ingin dibeli: ")
            curr = toko_tas.head
            while curr:
                if curr.nama == nama_tas:
                    print(f"Tas {nama_tas} berhasil dibeli dengan harga {curr.harga}")
                    invoice = input("Cetak Invoice(y/t)? : ")
                    if invoice == "y":
                        filenya = "invoice PA.txt"
                        f = open(filenya, "w")
                        d = {
                            "Nama Tas" :  nama_tas,
                            "Harga" : curr.harga,
                            "Jumlah Pesanan" : '1',
                            "Total Harga" : curr.harga
                        }
                        for k, v, in d.items():
                            f.write(str(k) + " = " + str(v) + "\n")
                        
                        f.close()
                        print()
                        print("===== Invoice Anda Sudah Dicetak =====")
                        menu_pembeli()
                        break

                    elif invoice == "t":
                        print()
                        print("===== Terimakasih Sudah Memesan =====")
                        menu_pembeli()
                        break

                    else:
                        print()
                        print("===== Pilihan Tidak Valid =====")
                        menu_pembeli()
                        break
                curr = curr.next
            else:
                print()
                print(f"Tas {nama_tas} tidak ditemukan di toko")
                menu_pembeli()

        elif pilihan == "0":
            print()
            print("===== Terima kasih telah berbelanja di Toko Tas =====")
            main()

        else:
            print()
            print("===== Pilihan tidak valid =====")
            menu_pembeli()

    except:
        print()
        print()
        print("===== Invalid =====")
        menu_pembeli()


# ========================================================================================================================== #
# =================================================== MENU LOG IN ========================================================== #
# ========================================================================================================================== #

def user_login():
    print()
    user = input("Masukkan Username: ")
    pass_user = input("Masukkan Password: ")
    if user == "user" and pass_user == "user":
        print()
        print('='*5,"Log In Berhasil",'='*5)
        menu_pembeli()
    
    else:
        print()
        print('='*5,"Username atau Password Anda Salah",'='*5)
        main()

def admin_login():
    print()
    admin = input("Masukkan Username: ")
    pass_admin = input("Masukkan Password: ")
    if admin == "admin" and pass_admin == "admin":
        print()
        print('='*5,"Log In Berhasil",'='*5)
        menu()
    
    else:
        print()
        print('='*5,"Username atau Password Anda Salah",'='*5)
        main()

# ========================================================================================================================== #
# ================================================== MENU AWAL ============================================================= #
# ========================================================================================================================== #

def main():
    print()
    print("===============================================")
    print("                 SELAMAT DATANG                ")
    print("===============================================")
    print("1. Menu Admin")
    print("2. Menu Pembeli")
    print("0. Keluar")
    print("===============================================")
    try:
        pilihan_utama = input("Silakan masukkan pilihan Anda (0-2): ")

        if pilihan_utama == '1':
            admin_login()

        elif pilihan_utama == '2':
            user_login()

        elif pilihan_utama == '0':
            print()
            print('===== Terima Kasih =====')
        
        else:
            print()
            print("===== Pilihan tidak valid =====")
            main()

    except:
        print()
        print()
        print("===== Invalid =====")
        main()

main()