#BUBLE_SORT
data=[5,3,1,2]
max=len(data)
print("Nilai array data awal:"+str(data))
idproses=1

for x in range(max-1,0,-1):
    print("x = "+str(x))
    for y in range(x):
        print("Ketika y = "+str(y))
        if data[y]>data[y+1]:
            temp=data[y+1]
            data[y+1]=data[y]
            data[y]=temp
            print("Terjadi pertukaran data:"+str(data))
        else:
            print("Tidak terjadi pertukaran data")

        print("Hasil pertukaran pada Proses ke "+str(idproses)+":"+str(data))
        idproses+=1
