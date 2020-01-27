#INSERTION_SORT
data = [5,3,1,2]
max = len(data)
idproses = 1

for x in range (1,max,1):
    for y in range (x,0,-1):
        if data[y] < data [y-1] :
            temp = data[y-1]
            data[y-1] = data [y]
            data [y] = temp
            print ('Terjadi pertukaran data: ' +str(data))
        else :
            print('Tidak terjadi pertukaran data')
    print ('hasil pertukaran pada proses ke-' + str(idproses)+ ':' +str(data))
    idproses+=1
    print()
