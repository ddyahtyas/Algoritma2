import csv

while True:
        print("=== APLIKASI KONTAK ===")
        print("[1] Lihat Daftar Kontak")
        print("[2] Buat Kontak Baru")
        print("[3] Edit Kontak")
        print("[4] Hapus Kontak")
        print("[5] Cari Kontak")
        print("[6] Exit")
        print("------------------------")
        selected_menu = int(input("Pilih menu> "))

        if (selected_menu == 1):
            contacts = []
            with open('Data.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                for row in csv_reader:
                    contacts.append(row)

            if (len(contacts) > 0):
                labels = contacts.pop(0)
                print(f"{labels[0]} \t {labels[1]} \t {labels[2]}")
                print("-" * 34)
                for data in contacts:
                    print(f'{data[0]} \t {data[1]} \t {data[2]}')
            else:
                print("Tidak ada data!")

        elif (selected_menu == 2):
            with open('Data.csv', mode='a') as csv_file:
                fieldnames = ['NO', 'NAMA', 'TELEPON']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames) #jadi dictionary

                no = input("No urut: ")
                nama = input("Nama lengkap: ")
                telepon = input("No. Telepon: ")

                writer.writerow({'NO': no, 'NAMA': nama, 'TELEPON': telepon})
                print("Berhasil disimpan!")
                exit()

        elif (selected_menu == 3):
            contacts = []

            with open('Data.csv', mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    contacts.append(row)

            print("NO \t NAMA \t TELEPON")
            print("-" * 32)

            for data in contacts:
                print(f"{data['NO']} \t {data['NAMA']} \t {data['TELEPON']}")

            print("-----------------------")
            no = input("Pilih nomer kontak> ")
            nama = input("nama baru: ")
            telepon = input("nomer telepon baru: ")

            # mencari contact dan mengubah datanya
            # dengan data yang baru
            indeks = 0
            for data in contacts:
                if (data['NO'] == no):
                    contacts[indeks]['NAMA'] = nama
                    contacts[indeks]['TELEPON'] = telepon
                indeks = indeks + 1

            # Menulis data baru ke file CSV (tulis ulang)
            with open('Data.csv', mode="w") as csv_file:
                fieldnames = ['NO', 'NAMA', 'TELEPON']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in contacts:
                    writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['TELEPON']})

        elif (selected_menu == 4):
            contacts = []
            with open('Data.csv', mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    contacts.append(row)

            print("NO \t NAMA \t\t TELEPON")
            print("-" * 32)

            for data in contacts:
                print(f"{data['NO']} \t {data['NAMA']} \t {data['TELEPON']}")

            print("-----------------------")
            no = input("Hapus nomer> ")

            # mencari contact dan mengubah datanya
            # dengan data yang baru
            indeks = 0
            for data in contacts:
                if (data['NO'] == no):
                    contacts.remove(contacts[indeks])
                indeks = indeks + 1

            # Menulis data baru ke file CSV (tulis ulang)
            with open('Data.csv', mode="w") as csv_file:
                fieldnames = ['NO', 'NAMA', 'TELEPON']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for new_data in contacts:
                    writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['TELEPON']})

            print("Data sudah terhapus")
            #delete_contact()
        elif (selected_menu == 5):
            contacts = []

            with open('Data.csv', mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    contacts.append(row)

            no = input("Cari berdasrakan nomer urut> ")

            data_found = []

            # mencari contact
            indeks = 0
            for data in contacts:
                if (data['NO'] == no):
                    data_found = contacts[indeks]

                indeks = indeks + 1

            if len(data_found) > 0:
                print("DATA DITEMUKAN: ")
                print(f"Nama: {data_found['NAMA']}")
                print(f"Telepon: {data_found['TELEPON']}")
            else:
                print("Tidak ada data ditemukan")
            #search_contact()
        elif (selected_menu == 6):
            break
        else:
            print("Kamu memilih menu yang salah!")