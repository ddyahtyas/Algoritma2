#Mendapatkan index melalui value dan sebaliknya
print('masukan nilai array, dan akan berhenti jika ada tanda (=)')
mobil = []
while True:
    temp = input()
    if temp == '=':
        break
    else:
        mobil.append(temp)
print(mobil)
print()
while True:
    print()
    print('1. mecari value dg index');
    print('2. mencari index dengan value ')
    pilihan= int(input('pilih menu: '))
    if pilihan == 1:
        temp = int(input("Masukan index yang ingin dicari : "))
        print("valuenya adalah : ", mobil[temp])
    elif pilihan == 2:
        temp = input("masukan value yg ingin dicari : ")
        #index = mobil.index(temp)
        #print("indeknya pada : ", index)
        for x in range(len(mobil)):
            if(mobil[x])==temp :
                print("ketemu")
                print("data ditemukan pada index ", x)
                break
            elif(x==(len(mobil)-1)):
                print("data tidak ditemukan ")
    else:
        break
