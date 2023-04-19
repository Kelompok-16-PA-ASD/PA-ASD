- DESKRIPSI PROGRAM
    Deskripsi program struktur data linked list dengan algoritma searching dan sorting pada toko tas dapat diartikan sebagai program komputer yang mengimplementasikan struktur data linked list, serta algoritma searching dan sorting, untuk mengelola data yang terkait dengan operasi toko tas.

    Struktur data linked list digunakan dalam program untuk menyimpan daftar tas yang dijual oleh toko. Setiap kali toko menambahkan atau menghapus tas, linked list akan diperbarui secara otomatis. Algoritma searching dapat digunakan untuk mencari tas tertentu berdasarkan nama/merk tas. Sementara itu, algoritma sorting dapat digunakan untuk mengurutkan tas berdasarkan harga tas tersebut.

    Dalam konteks toko tas, program ini dapat membantu mengoptimalkan proses manajemen persediaan dan penjualan tas, sehingga meningkatkan efisiensi dan keuntungan toko. Dengan adanya struktur data linked list dan algoritma searching dan sorting, program ini dapat mempermudah akses dan manipulasi data yang diperlukan dalam operasi sehari-hari toko tas.


- STRUKTUR PROJECT
    Program ini merupakan implementasi dari sistem inventaris sederhana untuk toko tas, dengan struktur sebagai berikut berikut:
    Program ini terstruktur dalam dua kelas, yaitu kelas Tas dan kelas TokoTas. Kelas Tas memiliki tiga atribut: nama (nama tas), harga (harga tas), dan next (referensi ke tas berikutnya dalam linked list). Kelas TokoTas memiliki dua atribut: head (referensi ke tas pertama dalam linked list) dan size (jumlah tas dalam inventaris).

    Metode CREATE (tambah_tas) menambahkan tas baru ke akhir linked list. Metode ini pertama-tama membuat objek Tas baru dengan nama dan harga yang diberikan, lalu menambahkannya ke akhir linked list.

    Metode READ (tampilkan_tas) menampilkan semua tas yang ada di inventaris. Metode ini memulai pencarian pada head linked list dan menelusurinya hingga akhir, kemudian mencetak nama dan harga setiap tas yang telah ditambahkan.

    Metode UPDATE (update_tas) mengubah harga suatu tas di inventaris. Metode ini memulai pencarian pada head linked list dan menelusurinya hingga menemukan tas dengan nama yang diberikan. Jika tas ditemukan, harga tas diubah menjadi harga baru yang diberikan. Jika nama tas tidak ditemukan, maka tas tidak ditemukan  dan menu admin terpanggil kembali.

    Metode DELETE (hapus_tas) menghapus tas dari inventaris. Metode ini memulai pencarian pada head linked list dan menelusurinya hingga menemukan tas dengan nama yang diberikan. Jika tas ditemukan, tas dihapus dari linked list. Jika tas tidak ditemukan, maka tas tidak ditemukan dan menu admin terpanggil kembali. 

    Metode SORT (quick_sort) mengurutkan tas di inventaris berdasarkan harga menggunakan algoritma Quick Sort. Metode ini memanggil metode bantu (_quick_sort) yang mengimplementasikan algoritma rekursif. Metode bantu ini mengambil head linked list sebagai input dan mengembalikan head baru dari linked list yang sudah terurut.

    Metode SEARCH (jump_search) mencari tas di inventaris menggunakan algoritma Jump Search. Metode ini mengambil nama tas yang akan dicari sebagai input dan mengembalikan objek tas jika ditemukan, atau None jika tidak ditemukan. Algoritma ini bekerja dengan membagi linked list menjadi blok-blok dengan ukuran sqrt(n) dan melompat ke blok yang mungkin berisi tas yang dicari. Lalu, algoritma secara linear mencari tas di dalam blok. Jika tas tidak ditemukan di dalam blok, algoritma melompat ke blok berikutnya dan mengulangi proses pencarian. Jika mencapai akhir linked list tanpa menemukan tas, algoritma mengembalikan None.

    Program ini juga memiliki fungsi menu() yang menampilkan menu pilihan kepada pengguna dan memanggil metode yang sesuai berdasarkan pilihan pengguna. 

- FITUR DAN FUNGSIONALITAS
    Program ini adalah implementasi dari sebuah toko tas yang menggunakan linked list sebagai struktur data.
    Fungsi-fungsi yang ada pada class TokoTas adalah:
    tambah_tas(nama, harga): untuk menambahkan tas baru dengan nama dan harga tertentu ke linked list. Tas baru akan menjadi tail pada linked list.
    tampilkan_tas(): untuk menampilkan semua tas yang ada pada linked list.
    update_tas(nama, harga_baru): untuk mengubah harga tas yang memiliki nama tertentu.
    hapus_tas(nama): untuk menghapus tas yang memiliki nama tertentu pada linked list.
    quick_sort(): untuk mengurutkan linked list dengan menggunakan algoritma quick sort berdasarkan harga tas.
    _quick_sort(node): merupakan fungsi rekursif yang digunakan oleh quick_sort() untuk mengurutkan linked list.
    jump_search(nama): untuk mencari tas yang memiliki nama tertentu pada linked list dengan menggunakan algoritma jump search.
    Menu admin digunakan untuk menjalankan program yang dapat melakukan operasi tambah, tampilkan, ubah harga, hapus, urutkan, dan cari tas.

    
- CARA PENGGUNAAN
    pada saat program dijalankan maka akan menampilan 3 pilihan menu yaitu menu admin, menu pembeli dan keluar
    jika user memilih 1 = user masuk sebagai admin
    jika user memilih 2 = user masuk sebagai pembeli
    jika user memilih 0 = maka user akan keluar dari program

    1. login admin
       user memilih 1 = user masuk sebagai admin, maka user akan diminta untuk memasukkan username dan password, pada program ini kami sudah menyiapkan username admin = admin dan password = admin, jadi user tinggal menginputkan username dan password yang sudah disiapkan. jika username dan password salah maka user tidak dapat masuk ke program.jika username dan password benar maka login sebagai admin berhasil dan tampilan menu admin akan muncul.
       admin memiliki 7 menu:
        a. jika admin memilih 1 = tambah tas, admin dapat menginputkan merk serta harga tas tersebut.
        b. jika admin memilih 2 = tampilkan tas, admin dapat melihat semua merk dan harga tas yang telah ditambahkan
        c. jika admin memilih 3 = ubah harga tas, admin dapat mengubah harga tas dengan memasukkan merk tas dan 
           menginputkan harga tas yang baru.
        d. jika admin memilih 4 = hapus tas, admin dapat menghapus tas dengan memasukkan merk tas tersebut.
        e. jika admin memilih 5 = urutkan tas (berdasarkan harga), maka daftar merk tas beserta harga yang sudah di
           tambahkan tadi akan terurut berdasarkan harga dari yang terkecil ke harga yang palin besar.
        f. jika admin memilih 6 = cari tas, admin dapat mencari tas dengan cara menginputkan nama tas, jika nama 
           tas yang diinputkan admin benar maka tas tersebut akan ditemukan dengan cara menampilkan harga tas tersebut.
        g. jika admin memilih 0 = keluar, maka admin akan keluar dari program.

    2. login pembeli
       user memilih 2 = masuk sebagai pembeli, dan user akan diminta untuk memasukkan username dan password, pada program ini kami telah menyiapkan username pembeli = user dan password = user jadi user tinggal menginputkan username dan password yang sudah disiapkan. jika username dan password salah maka user tidak dapat masuk ke program. jika username dan password benar maka login sebagai pembeli berhasil dan tampilan menu pembeli akan muncul.
       pembeli memiliki 3 menu:
        a. jika user memilih 1 = lihat barang, user dapat melihat semua barang yang telah diinputkan oleh admin
        b. jika user memilih 2 = beli barang, user melakukan transaksi pembelian tas dengan cara memasukkan merk 
           tas tersebut, jika transaksi berhasil kemudian program akan menanyakan apakah user ingin cetak invoice(y/t)? jika "y" maka invoice akan otomatis tercetak dimenu invoice PA.txt dan jika "t" maka invoice tidak akan dicetak transaksi pun telah selesai.
        c. jika user memilih 0 = keluar, maka user akan keluar dari program
