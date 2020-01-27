print('===== Menghapus Array ======')
print()
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
    print('1. hapus dengan remove');
    print('2. hapus dengan pop')
    pilihan = int(input('pilih menu: '))
    if pilihan < 3:
        break
    else:
        print('maaf pilihan tidak ada')

print()
if pilihan == 1:
    temp = input('masukan yang ingin dihapus : ')
    mobil.remove(temp)
if pilihan == 2:
    mobil.pop()

print(mobil)
