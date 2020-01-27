#SELECTION_SORT
data = [5,3,1,2] # mendeklarasikan array data
max = len(data)- 1 # variabel
for i in range(max): #menyataka jumlah proses(iterasi) sebanyak 3 kali ==> 0,1,2
    print (i)
    x = i
    print ('------')
    for j in range ((x+1), max+1,+1) : #mengecek data untuk setiap iterasi
        print(j)
        if data [x] > data[j]:
            x = j
    temp = data[x]
    data[x] =data[i]
    data[i] = temp
    print (data)