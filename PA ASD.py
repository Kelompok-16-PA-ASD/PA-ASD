class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data): # Untuk Menambah List Barang
        if self.head is None:
            self.head = Node(data)
        else:
            node_baru = Node(data)
            node_baru.next = self.head
            self.head = node_baru

    def hapus(self): # Untuk Menghapus List Barang
        if self.head is None:
            print("List Tas Kosong")
        else:
            self.head = self.head.next
  
    def tampilkan(self, page_size): 
        if not self.head: # Jika Tidak Ada Daftar Tas
            print("Data Tas Kosong")
            return
        
        count = 0
        daftar = self.head
        nomor = 1

        while daftar:
            count += 1
            # Awal Halaman
            if count % page_size == 1: 
                print("\nPage", (count-1)//page_size+1)
                print("-"*20)
            
            print(f"{nomor}. {daftar.data}")
            
            # Akhir Halaman
            if count % page_size == 0: 
                input("Tekan Enter untuk Lanjut...")
                
            daftar = daftar.next
            nomor += 1
        
        input("Daftar Akhir. Tekan Enter Untuk Kembali...")

    def tampil(self):
        if self.head is None:
            print("Linked List Kosong")
        else:
            n = self.head
            nomor = 1

            while n is not None:
                print(f"{nomor}. {n.data}")
                n = n.next
                nomor += 1

shoe_list = LinkedList()

# Untuk Menambah daftar list
shoe_list.tambah("Hermes Birkin")
shoe_list.tambah("Prada Galleria Bag")
shoe_list.tambah("Dior Lady Dior Bag")
shoe_list.tambah("Celine Luggage Tote")
shoe_list.tambah("Balenciaga City Bag")
shoe_list.tambah("Burberry Banner")
shoe_list.tambah("Hilde Palladino Gadino")
shoe_list.tambah("Hermes Himalaya Birkin Bag")
shoe_list.tambah("Chanel Grand Shopping Tote")


def menu_admin():
        print()
        print('='*5,"Menu Admin",'='*5)
        print('1.) Tampilkan Barang')
        print('2.) Tambah Barang')
        print('3.) Edit Barang')
        print('4.) Hapus Barang')
        print('0.) Kembali')  

        pilihan = input('Pilih Menu: ')
        if pilihan == "1" :
            show_tas()
        elif pilihan == "2" :
            add_tas()
        elif pilihan == "3" :
            edit_tas()
        elif pilihan == "4" :
            del_tas()
        elif pilihan == "0" :
            print()
            menu_awal()
        else :
            print()
            print('='*5,'Pilihan tidak tersedia','='*5)
            menu_admin()

def show_tas():
    shoe_list.tampilkan(page_size = 4)
    menu_admin()

def add_tas():
    add = input("Masukkan Nama Tas: ")
    shoe_list.tambah(add)
    print(f"{add} Telah Ditambahkan")
    menu_admin()
    return

def del_tas():
    delete = input("Masukkan Nama Tas Yang Ingin Dihapus: ")
    shoe_list.hapus(delete)
    return

def edit_tas():
    delete = input("Masukkan Nama Tas Yang Ingin Dihapus: ")
    shoe_list.hapus(delete)
    add = input("Masukkan Nama Tas: ")
    shoe_list.tambah(add)
    print(f"{add} Telah Ditambahkan")
    return


def menu_user():
    print()
    print("1.) Pemesanan")
    print("0.) Kembali")
    milih = input('Pilih Menu: ')
    if milih == "1":
        pesan()
    elif milih == "0":
        print()
        menu_awal()
    else:
        print()
        print('='*5,'Menu Tidak Ada','='*5)
        menu_user()

def pesan():
    print()
    print('='*5,"List Tas",'='*5)
    shoe_list.tampil()
    print()
    pesan_tas = input("Masukkan Nama Tas Yang Ingin Dipesan: ")
    jumlah = int(input("Jumlah Pesanan: "))
    harga = jumlah * 100000
    print()
    print("Pesanan =", pesan_tas)
    print("Jumlah Pesanan =", jumlah)
    print("Total Harga =", harga)
    print()
    invoice = input("Cetak Invoice(y/t)? : ")
    while True:
        if invoice == "y":
            filenya = "invoice PA.txt"
            f = open(filenya, "w")
            d = {
                "Nama Tas" :  pesan_tas,
                "Harga" : "Rp 100000",
                "Jumlah Pesanan" : jumlah,
                "Total Harga" : harga
            }
            for k, v, in d.items():
                f.write(str(k) + " = " + str(v) + "\n")
            
            f.close()
            print()
            print('='*5,"Invoice Anda Sudah Dicetak",'='*5)
            menu_user()
            break
        elif invoice == "t":
            print()
            print('='*5,"Terimakasih Sudah Memesan",'='*5)
            menu_user()
            break 
                    

def user_login():
    print()
    user = input("Masukkan Username: ")
    pass_user = input("Masukkan Password: ")
    if user == "user" and pass_user == "user":
        print()
        print('='*5,"Log In Berhasil",'='*5)
        menu_user()
    else:
        print('='*5,"Username atau Password Anda Salah",'='*5)
        print()
        menu_awal()

def admin_login():
    print()
    admin = input("Masukkan Username: ")
    pass_admin = input("Masukkan Password: ")
    if admin == "admin" and pass_admin == "admin":
        print()
        print('='*5,"Log In Berhasil",'='*5)
        menu_admin()
    else:
        print('='*5,"Username atau Password Anda Salah",'='*5)
        print()
        menu_awal()

def menu_awal():
    print('='*62)
    print('='*10,"Selamat Datang di Toko Tas SERBA 100.000",'='*10)
    print('='*62)
    print("1.) Admin")
    print("2.) User")
    print('0.) Keluar')
    pilih = input("Pilih Menu: ")
    if pilih == "1":
        admin_login()
    elif pilih == "2":
        user_login()
    elif pilih == "0":
        print('='*40)
        print('Terima Kasih'.center(40))
        print('='*40)
    else:
        print('='*5,"Menu Tidak Ada",'='*5)
        print()
        menu_awal()

menu_awal()
