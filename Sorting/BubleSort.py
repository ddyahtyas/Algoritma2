'''BUBLE_SORT
Langkahnya seperti di bawah ini :
1. Bandingkan nilai pada data ke-1 dengan data ke-2.
2. Jika nilai data ke-1 lebih besar dari data ke-2 maka tukar posisinya.
3. Kemudian data yang lebih besar tersebut dibandingkan lagi dengan data ke-3.
4. Jika data ke-3 lebih kecil dari data ke-2 maka tukar posisinya, dan begitu seterusnya sampai semua data yang ada jadi terurut'''

data = [5,3,1,2]
for x in range (len(data)-1,0,-1):
    print('---')
    for y in range(x):
        if data[y] > data[y+1]:
            temp = data[y+1]
            data[y+1]= data[y]
            data[y] = temp
        print(data)
print('hasilnya ', data)