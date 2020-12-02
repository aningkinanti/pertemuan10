# TUGAS PERTEMUAN 10 DAN PENJELASAN
## MODUL LABS 6
## SUB RUTIN / FUNGSI

**Nama	  : Aning Kinanti** <br>
**Nim	  : 312010364** <br>
**Kelas	  : TI.20.A2** <br>
**Matkul  : Bahasa Pemrograman** <br>


## TUGAS LATIHAN LABS 6
#### SOAL
![soal](ssLatihan/soal.PNG)

#### SYNTAX
berikut merupakan syntax untuk menampilkan program diatas

```python
#author aning kinanti

#mengubah def a(x): ke lambda
a = (lambda x: x ** 2)
print(a(5))

#mengunbah def b(x, y): ke lambda
b = (lambda x, y: x**2 + y**2)
print(b(3,6))

#mengubah def c(*args): ke lambda
c = (lambda *args: sum(args)/ len(args))
print(c(3)) 

#mengubah def d(s): ke lambda
d = (lambda s: "".join(set(s)))
print(d("abcde"))
```

#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas

![output](ssLatihan/output.PNG)

#### ANALISIS
•	Belum

## TUGAS PRAKTIKUM 

#### SOAL
![soal](ssPraktikum/soal.PNG)

#### SYNTAX DAN PENJELASAN
berikut merupakan syntax untuk menampilkan program diatas

•	Statement dibawah ini berfungsi untuk merangkap statement def. <br>
```python
#author aning kinanti

dataNilai = {}
loop = True
print(95*"=")
```

•	Statement `def tambahData(): ` berfungsi untuk membuat menu menambahkan data mahasiswa. <br>
```python
#tambahData
def tambahData():
    print(75*"-")
    print("TAMBAH DATA MAHASISWA")
    print(75*"-")
    nama = input("Nama        : ")
    nim = input("NIM         : ")
    nTugas = int(input("Nilai Tugas : "))
    nUts = int(input("Nilai UTS   : "))
    nUas = int(input("Nilai UAS   : "))
    nAkhir = float(nTugas)*30/100+(nUts)*35/100+(nUas)*35/100
    dataNilai[nama] = [nim, nTugas, nUts, nUas, nAkhir]
    print(f"DATA ANDA BERHASIL DISIMPAN!")
    print(75*"-")
print(95*"=")
```
•	Statement `def lihatData(): ` berfungsi untuk membuat menu melihat data mahasiswa. <br>
```python
#lihat data
def lihatData():
    print(102*"-")
    print("LIHAT DATA MAHASISWA")
    print(102*"-")
    print("Daftar Mahasiswa")
    if len(dataNilai) <= 0:  
        print("|{0:^69}|".format("DATA KOSONG! SILAHKAN TAMBAH DATA TERLEBIH DAHULU"))
    else:
        no = 0
        print("| {0:^2} | {1:^18} | {2:^12} | {3:^12} | {4:^12} | {5:^12} | {6:^7} |".format("NO", "NAMA", "NIM", "NILAI TUGAS", "NILAI UTS", "NILAI UAS", "NILAI AKHIR"))
        for data in dataNilai.items():
            no += 1 
            print(f"| {no:>2} | {data[0]:<18} | {data[1][0]:<12} | {data[1][1]:>12} | {data[1][2]:>12} | {data[1][3]:>12} | {data[1][4]:>11.2f} |")               
        print(102*"-")
```

•	Statement `def ubahData(): ` berfungsi untuk membuat menu mengubah data mahasiswa. <br>
```python
#ubah data
def ubahData():
    print(75*"-")
    print("UBAH DATA MAHASISWA [BERDASARKAN NAMA!]")
    print(75*"-")
    print("Daftar Mahasiswa")
    if len(dataNilai) <= 0:  
        print("|{0:^69}|".format("DATA ANDA TIDAK DITEMUKAN"))
    else:
        nama = input("Masukan Nama        : ") 
        if nama in dataNilai.keys():     
            print("DATA ANDA DITEMUKAN!")     
            print(f"Nama        : {nama}")
            print(f"Nim         : {dataNilai[nama][0]}")
            print(f"Nilai Tugas : {dataNilai[nama][1]}")
            print(f"Nilai UTS   : {dataNilai[nama][2]}")
            print(f"Nilai UAS   : {dataNilai[nama][3]}")
            print(75*"-")
            print("1. Nama\n2. NIM\n3. Nilai\n0. Kembali")
            ubah = int(input("Apa yang ingin diubah? [Masukan angka 1-3] : "))
            if ubah == 1:
                namaBaru = input("Masukan Nama Baru : ")
                dataNilai[namaBaru] = dataNilai.pop(nama)
                print("DATA ANDA BERHASIL DIUBAH! PILIH MENU 'L' UNTUK MELIHAT DATA BARU ANDA!")

            elif ubah == 2:
                nimBaru = input("Masukan Nim Baru : ")
                dataNilai[nama][0] = nimBaru
                print("DATA ANDA BERHASIL DIUBAH! PILIH MENU 'L' UNTUK MELIHAT DATA BARU ANDA!")

            elif ubah == 3:
                nTugasBaru = int(input("Masukan Nilai Tugas Baru : "))
                nUtsBaru = int(input("Masukan Nilai UTS Baru : "))
                nUasBaru = int(input("Masukan Nilai UAS Baru : "))
                nAkhirBaru = float(nTugasBaru)*30/100+(nUtsBaru)*35/100+(nUasBaru)*35/100
                dataNilai[nama][1:4] = nTugasBaru, nUtsBaru, nUasBaru, nAkhirBaru
                print("DATA ANDA BERHASIL DIUBAH! PILIH MENU 'L' UNTUK MELIHAT DATA BARU ANDA!")

            elif ubah == 0:
                pass
            
            else:
                print(f"Pilihan {ubah} tidak tersedia! [Masukan angka 1-3]")

        else:
            print(f"Data {nama} tidak ditemukan!") 
        print(75*"-")
```
•	Statement `def cariData(): ` berfungsi untuk membuat menu mencari data mahasiswa berdasarkan nama mahasiswa. <br>
```python
def cariData():
    print(75*"-")
    print("CARI DATA MAHASISWA [BERDASARKAN NAMA!]")
    print(75*"-")
    if len(dataNilai) <= 0:  
        print("|{0:^69}|".format("DATA ANDA TIDAK DITEMUKAN"))
    else:
        nama = input("Masukan Nama        : ") 
        if(nama in dataNilai):
            no = 1            
            print("DATA ANDA DITEMUKAN!")
            print(f"Nama        : {nama}")
            print(f"NIM         : {dataNilai[nama][0]}")
            print(f"Nilai Tugas : {dataNilai[nama][1]}")
            print(f"Nilai UTS   : {dataNilai[nama][2]}")
            print(f"Nilai UAS   : {dataNilai[nama][3]}") 
            print(f"Nilai Akhir : {dataNilai[nama][4]}")       
        else:
            print(f"Data {nama} tidak ditemukan!") 
        print(75*"-")
```
•	Statement `def hapusData(): ` berfungsi untuk membuat menu menghapus data mahasiswa berdasarkan nama mahasiswa. <br>
```python
def hapusData():
    print(75*"-")
    print("HAPUS DATA MAHASISWA [BERDASARKAN NAMA!]")
    print(75*"-")
    if len(dataNilai) <= 0:  
        print("|{0:^69}|".format("DATA ANDA TIDAK DITEMUKAN"))

    else:
        nama = input("Nama        : ") 
        if(nama in dataNilai):
            del dataNilai[nama]
            print(f"Data {nama} berhasil dihapus!")
        else:
            print(f"Data {nama} tidak ditemukan!") 
    print(75*"-")
```

•	Statement dibawah ini berfungsi untuk membuat perulangan program. Yang akan memproses fungsi tambahdata, lihatdata, caridata, dan hapus data <br>
```python
# Program
print(75*"-")
print("-----------------------PROGRAM INPUT NILAI MAHASISWA-----------------------")
print(75*"-")

while loop: 
    print()
    pilih = input("[(T)ambah, (L)ihat, (U)bah, (H)apus, (C)ari, (K)eluar] : ")
    print(75*"-")
    print()

    if pilih == 'T' or pilih == 't':
        tambahData()

    elif pilih == 'L' or pilih == 'l':
        lihatData()      

    elif pilih == "U" or pilih == "u":
        ubahData()

    elif pilih == "H" or pilih == "h":
        hapusData()

    elif pilih == "C" or pilih == "c":
        cariData()

    elif pilih == "K" or pilih == "k":
        print("Program selesai, Terima Kasih")
        loop = False 

    else:
        print(f"pilih '{pilih}' tidak ada! Silahkan masukan [T/L/U/H/C/K]")
```




#### OUTPUT
Dibawah ini merupakan hasil output dari syntax diatas:

##### OUTPUT MENU TAMBAH
![tambah](ssPraktikum/tambahdata.PNG) <br>
•	User akan diminta memilih menu, pertama silahkan pilih menu tambah (T)/(t). <br>
•	Maka program akan berjalan seperti pada gambar diatas. Disini saya mencoba menambahkan 2 data mahasiswa. <br>

##### OUTPUT MENU LIHAT
![lihat](ssPraktikum/lihatdata.PNG) <br>
•	User dapat melihat data yang telah ditambahkan, dengan memilih menu lihat (L)/(l). <br>
•	Maka program akan menampilkan data yang telah ditambahkan seperti pada gambar diatas. <br>

##### OUTPUT MENU UBAH
![ubah](ssPraktikum/ubahdata.PNG) <br>
•	User dapat mengubah data yang telah diinput, dengan memilih menu ubah (U)/(u). <br>
•	User akan diminta memasukan data nama mahasiswa yang akan diubah. <br>
•	Kemudian apabila data tersebut ditemukan, program akan menampilkan data lengkap mahasiswa tersebut. <br>
•	Lalu program akan memberikan pilihan kepada user data apa yang akan diubah. <br>
•	Maka program akan menampilkan data yang telah ditambahkan seperti pada gambar diatas. <br>
•	Seperti pada gambar diatas saya mencoba mengubah data Nama Kinan menjadi Kinanti. <br>
•	Lalu user dapat mengecek kembali data yang telah diubah dengan menu lihat. <br>

##### OUTPUT MENU CARI
![cari](ssPraktikum/caridata.PNG) <br>
•	User dapat mencari data mahasiswa berdasarkan nama, dengan memilih menu cari (C)/(c). <br>
•	User akan diminta memasukan data nama mahasiswa yang akan dicari. <br>
•	Kemudian apabila data tersebut ditemukan, program akan menampilkan data lengkap mahasiswa tersebut. <br>

##### OUTPUT MENU HAPUS
![output](ssPraktikum/hapusdata.PNG) <br>
•	User dapat menghapus data mahasiswa berdasarkan nama, dengan memilih menu hapus (H)/(h). <br>
•	User akan diminta memasukan data nama mahasiswa yang akan dihapus. <br>

## SEKIAN DAN TERIMAKASIH :)
