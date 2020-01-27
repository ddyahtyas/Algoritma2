print ('====== Menambah Elemen Array =====')
fruits = ['mangga', 'salak', 'apel', 'jeruk']
sayur = []
while True:
    temp = input()
    if temp == '=':
       break
    else:
       sayur.append(temp)

fruits.extend(sayur)
print(fruits)
