#author aning kinanti

dataNilai = {}
loop = True

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

#hapus data
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

#cari data
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