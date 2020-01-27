'''INSERTION_SORT
Prinsip algoritma insertion sort pada dasarnya membagi data yang akan diurutkan menjadi dua bagian, satu bagian yang
belum diurutkan dan yang satunya lagi sudah diurutkan. Elemen pertama diambil dari bagian list yang belum diurutkan dan
kemudian diletakkan sesuai posisinya pada bagian lain dari list yang telah diurutkan. Langkah ini dilakukan secara
berulang hingga tidak ada lagi elemen yang tersisa pada bagian list yang belum diurutkan.

Langkahnya seperti di bawah ini :
1. Bandingkan data ke-2 dengan data ke-1, jika data ke-2 lebih kecil maka tukar posisinya, jika tidak biarkan aja.
2. Data ke-3 dibandingkan dengan data ke-1 dan ke-2, jika data ke-3 lebih kecil kemudian tukar lagi posisinya.
3. Data ke-4 dibandingkan dengan data ke-3, ke-2, dan ke-1, jika data ke-4 lebih kecil dari ketiganya maka letakkan
   data ke-4 ke posisi paling depan. Begitu seterusnya sampai tidak ada lagi data yang bisa dipindahkan.'''

data = [5,3,1,2]
max = len(data)-1
for x in range(1,max+1,1):
    print("proses" , x)
    for y in range(x,0,-1):
        if data[y] < data[y-1]:
            temp = data[y-1]
            data[y-1] = data[y]
            data[y] = temp
    print('hasilnya : ', data)