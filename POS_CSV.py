import csv
import os

# Input data dan load
# pencarian
# Penjualan
# Stok

while True:
    menu = ['1. Data Barang','2. Pencarian Barang', '3. Penjualan', '4. Stok']
    submenu1 = ['1. List Barang', '2. Input Barang', '3. Buble Sorting', '4. Insertion Sorting', '5. Selection Sort',
                '6. Kembali']
    DATABASE_FILE = 'database.csv'
    database = []
    # Load data dari CSV
    with open(DATABASE_FILE) as db_file:
        csv_reader = csv.reader(db_file, delimiter=';')
        for row in csv_reader:
            database.append(row)

    id_barang = int(database[len(database)-1][0])+1
    os.system("clear")
    print('\t'.join(menu))
    aksi = input("Pilihan: ")
    os.system("clear")

    if aksi=='1':
        while True:
            print('\t'.join(submenu1))
            aksiMenu1 = input("Pilih: ")
            if aksiMenu1 == '1':
                # Menampilkan data dari Array database
                print("\n %2s \t %10s \t %10s" %("ID","Nama","Harga"))
                for row in database:
                    print("%2s \t %10s \t %10s" %(row[0],row[1], row[2]))
                print("")

            elif aksiMenu1=='2':
                with open(DATABASE_FILE, mode='a') as db_file:
                    csv_writer = csv.writer(db_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    while True:
                        nama_barang = input('Masukkan Nama: ')
                        if nama_barang=='=':
                            break
                        harga_barang = input('Masukkan Harga: ')
                        csv_writer.writerow([id_barang, nama_barang, harga_barang])
                        database.append([id_barang, nama_barang, harga_barang])
                        id_barang += 1
                        os.system("clear")
                        print("Barang Telah Ditambahkan\n")

            #buble sort
            elif aksiMenu1 == '3':
                for i in range(len(database)):
                    database[i][2] = int(database[i][2])
                max = len(database)-1
                for x in range(max, 0, -1):
                    for y in range(x):
                        if database[y][2] > database[y + 1][2]:
                            temp = database[y + 1]
                            database[y + 1] = database[y]
                            database[y] = temp
                print("%2s \t %10s \t %10s" % ("ID", "NAMA", "HARGA"))
                for row in database:
                    print("%2s \t %10s \t %10s" % (row[0], row[1], row[2]))

            #inserton sort
            elif aksiMenu1 == '4':
                for i in range(len(database)):
                    database[i][2] = int(database[i][2])
                max = len(database)
                for x in range(1,max,1):
                    for y in range(x,0,-1):
                        if database[y][2] < database[y - 1][2]:
                            temp = database[y - 1]
                            database[y - 1] = database[y]
                            database[y] = temp
                print("%2s \t %10s \t %10s" % ("ID", "NAMA", "HARGA"))
                for row in database:
                    print("%2s \t %10s \t %10s" % (row[0], row[1], row[2]))

            # selection sort
            elif aksiMenu1 == '5':
                for i in range(len(database)):
                    database[i][2] = int(database[i][2])
                max = len(database) - 1
                for i in range(max):
                    x = i
                    for j in range(i + 1, max + 1, 1):
                        if database[x][2] > database[j][2]:
                            x = j
                    temp = database[i]
                    database[i] = database[x]
                    database[x] = temp
                print("%2s \t %10s \t %10s" % ("ID", "NAMA", "HARGA"))
                for row in database:
                    print("%2s \t %10s \t %10s" % (row[0], row[1], row[2]))

            elif aksiMenu1 == '6':
                break

            else:
                print('salah input')

    #elif aksi =='2':
    #elif aksi =='3':
    else:
        print('inputan salah')