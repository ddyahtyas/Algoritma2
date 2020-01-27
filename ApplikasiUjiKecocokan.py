import random
import datetime

print("Selamat Datang di Aplikasi Uji Kecocokan")
while True :
    print("===========================================")
    print("silahkan pilih menu")
    print("1. Quis Cinta")
    print("2. Uji CInta dengan Nama")
    print("3. Uji Cinta dengan Tanggal")
    print("4. Keluar")
    print()
    pilihan = int(input("pilihan : "))
    if pilihan == 1:
        print("QUIS CINTA ")
        nama1 = input("Masukan Nama Anda : ")
        nama2 = input("Masukkan Nama pasangan Anda : ")
        print("===========================================")
        print("Mulai")
        soal1 = int(input("Apakah punya uisa yang sama ? \n 1. Ya \n 2. beda 1-3 tahun \n 3. Beda sangat jauh"
                          " \n pilihan : "))
        soal2 = int(input("Apakah "+ nama2 + " merasa sedih saat tidak bersamamu ? \n 1. Tentu \n "
                                             "2. Mungkin \n 3. Tidak \n pilihan : "))
        soal3 = int(input("Apakah " + nama2 + " pernah menyatakan cinta kepadamu ? \n 1.Pernah \n "
                                              "2. Mungkin \n 3. Belum \n pilihan : "))
        soal4 = int(input("Tahukah Anda apa yang membuat dia bahagia ? \n 1. Tahu dong \n 2. kadang - kadang "
                          "\n 3. Tidak \n pilihan : "))
        print()
        print("HASILNYA ADALAH ")
        hasil = soal1 + soal2 + soal3 + soal4
        if hasil <= 5 :
            print("Kalian sangat serasi")
        elif hasil <= 8:
            print("pertahankan!! ")
        elif hasil <= 12 :
            print("cobalah pengertian kepadanya")
        elif hasil <= 16:
            print("yakin masih mau sama dia??")

    elif pilihan == 2 :
        loop = True
        while loop == True :
            print("UJI CINTA DENGAN NAMA")
            print("Semua nama memiliki makna. Mari kita tentukan potensi cinta diantara kamu.")
            print("=============================================================================")
            pria = input("Masukan nama pria : ")
            wanita = input("Masukan nama wanita : ")
            print("=================================")
            print("nama pria = ", pria)
            print("nama wanita ", wanita)
            confirm =input("Apakah nama yang dimasukkan sudah benar ? y/n : ")
            print()
            if confirm == "y" :
                loop = False

        match = random.randrange(0,100)
        print("HASILNYA ")
        print("akurasi kejodohan ", match , "%")

        if match > 80 :
            print("Ndang rabi !!!")
        elif match > 60 :
            print("pikir - pikir dulu")
        elif match > 40 :
            print("yakin mau nerusin ? ")
        elif match > 20 :
            print("cari lagi aja!!")
        else:
            print("Kalian tidak berjodoh")

    elif pilihan == 3:
        print("UJI CINTA DENGAN TGL LAHIR")
        print("Masukkan Tanggal lahir Anda")
        for i in range(2) :
            if i == 1 :
                print("Masukkan Tanggal lahir pasangan Anda")

            hari = int(input("Masukkan tanggal (dd) : "))
            bulan = int(input("MAsukan bulan (mm) : "))
            tahun = int(input("Masukan Tahun (yyyy) : "))

            x = datetime.datetime(tahun,bulan,hari)
            print("lahir pada : \n "+(x.strftime("%D")))

        match = random.randrange(0, 100)
        print("HASILNYA ")
        print("akurasi kejodohan ", match, "%")

    elif pilihan == 4 :
        break
    else:
        print("pilihan yang anda masukkan salah !! Ulangi lagi")