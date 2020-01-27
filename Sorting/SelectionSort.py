'''SELECTION_SORT
Prinsip dari algoritma selection sort adalah memilih elemen dengan nilai paling rendah dan menukar elemen tersebut dengan elemen ke-i. Nilai dari i dimulai dari 1 ke n, dimana n adalah jumlah total elemen dikurangi 1.
Langkahnya seperti di bawah ini :
1. Pengecekan dimulai dari data ke-1 sampai dengan data ke n.
2. Tentukan bilangan dengan index terkecil dari data bilangan tersebut.
3. Tukar bilangan dengan index terkecil tersebut dengan bilangan pertama (i=1) dari data bilangan tersebut.
4. Lakukan langkah 2 dan 3 untuk bilangan berikutnya (i=i+1) sampai di dapatkan data yang sesuai.

jumlah proses = n-1 '''

data = [5,3,1,2]
max = len(data)-1
for i in range(max):
    x = i
    for j in range(i+1,max+1,1):
        print(j)
        if data[j] < data[x]:
            x = j
    temp = data[i]
    data[i] = data[x]
    data[x] = temp
print(data)