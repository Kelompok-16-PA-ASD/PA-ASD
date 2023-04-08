def fibMonaccianSearch(arr, x, n):
    fibMMm2 = 0  
    fibMMm1 = 1  
    fibM = fibMMm2 + fibMMm1  
    
    
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1
    while (fibM > 1):
        i = min(offset+fibMMm2, n-1)

        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i

    if(fibMMm1 and arr[n-1] == x):
        return n-1

    return -1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.nama = ''
        self.harga = 0
        self.head = None
        self.count = 0

    def addLast(self, nodeBaru):
        if self.head is None:
            self.head = Node(nodeBaru)
            self.count += 1
        else:
            nodeAkhir = self.head
            while nodeAkhir.next is not None:
                nodeAkhir = nodeAkhir.next
            nodeAkhir.next = Node(nodeBaru)
            self.count += 1

    def deleteNode(self,position):
        if self.head == None:
            return
        temp = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None 
            return 
        
        for i in range (position,-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None :
            return 
        
        if temp.next is None:
            return 
        
        next = temp.next.next 
        temp.next = None
        temp.next = next

    def addTas(self):
        try:
            self.nama = input('Masukkan Nama Tas: ')
            self.harga = 100000
            return True
        except ValueError:
            print('Masukkan Harga Dengan Benar')
            return False
        
    def cari(self, data):
        simpanNama = []
        print('='*40)
        if data != None:
            for i in data:
                simpanNama.append(i[0])
            carikan = input('Masukkan nama yang ingin dicari: ')
            this = fibMonaccianSearch(simpanNama, carikan, len(simpanNama))
            if this >= 0:
                print('Data ditemukan di: ', this + 1)
            else:
                print(carikan, 'tidak ditemukan')
        else:
            print('invalid')
        
    def __str__(self):
        return '\t'.join(str(x) for x in [self.nama, self.harga])
    

class Storage:
    def __init__(self):
        self.tas = []
    def addTas(self):
        bag = Linked()
        if bag.addTas() == True:
            self.tas.append(bag)
            print ()
            print('Data Tas Telah Dimasukkan')
            menu_admin()

    def view(self):
        print ('='*25)
        print('\t'.join(['ID','Nama', 'Harga']))
        for idx, bag in enumerate(self.tas) :
            print(idx , end='\t')
            print(bag)
        print ('='*25)


simpan = Storage()
nama_kendaraan = Linked()
jenis_kendaraan = Linked()


def menu_admin():
        print()
        print('='*5,"Menu Admin",'='*5)
        print('1.) Tampilkan Barang')
        print('2.) Tambah Barang')
        print('3.) Hapus Barang')
        print('4.) Update Barang')
        print('5.) Search Barang')
        print('6.) Sorting Barang')
        print('0.) Kembali')  

        pilihan = input('Pilih Menu: ')
        if pilihan == "1" :
            if len(simpan.tas) < 1:
                print('Data Tas Masih Kosong')
                menu_admin()
            else:
                simpan.view()
                menu_admin()
        elif pilihan == "2" :
            simpan.addTas()
        elif pilihan == "3" :
            if len(simpan.tas) < 1:
                print('Data Tas Di Masih Kosong')
                menu_admin()
            while True:
                try:
                    simpan.view()
                    item = int(input('Masukan ID Berapa Yang Ingin Dihapus: '))
                    break
                except ValueError:
                    print("Input Dengan Nomor ")
            if item + 1  > len(simpan.tas):
                print('Nomor invalid')
            else:
                simpan.tas.remove(simpan.tas[item])
                nama_kendaraan.deleteNode(item)
                jenis_kendaraan.deleteNode(item)
                print ()
                print('Tas Telah Dihapus')
                menu_admin()
        elif pilihan == "4" :
            if len(simpan.tas) < 1:
                print('Data Tas Masih Kosong')
                menu_admin()
            while True:
                try:
                    simpan.view()
                    item = int(input('Masukan Nomor Berapa Yang Ingin Diupdate: '))
                    break
                except ValueError:
                    print("Input Dengan Nomor ")
            if item + 1  > len(simpan.tas):
                print('Nomor invalid')
            else:
                Link = Linked()
                if Link.addTas() == True :
                    simpan.tas.remove(simpan.tas[item])
                    nama_kendaraan.deleteNode(item)
                    jenis_kendaraan.deleteNode(item)
                    simpan.tas.insert(item , Link)
                    print ()
                    print('Data Tas Telah Di Update')
                    menu_admin()
        elif pilihan == "5":
            cari = input("Masukkan Nama Tas Yang Ingin Dicari: ") 
        elif pilihan == "6":
            menu_admin()
        elif pilihan == "0" :
            print()
            menu_awal()
        else :
            print()
            print('='*5,'Pilihan tidak tersedia','='*5)
            menu_admin()

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
    if len(simpan.tas) < 1:
        print('Data Tas Masih Kosong')
        menu_admin()
    else:
        simpan.view()
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

def menu_awal():
    print('='*62)
    print('='*10,"Selamat Datang di Toko Tas SERBA 100.000",'='*10)
    print('='*62)
    print("1.) Admin")
    print("2.) User")
    print('0.) Keluar')
    pilih = input("Pilih Menu: ")
    if pilih == "1":
        menu_admin()
    elif pilih == "2":
        menu_user()
    elif pilih == "0":
        print('='*40)
        print('Terima Kasih'.center(40))
        print('='*40)
    else:
        print('='*5,"Menu Tidak Ada",'='*5)
        print()
        menu_awal()

menu_awal()
print()