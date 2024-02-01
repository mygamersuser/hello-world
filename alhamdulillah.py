fileData=open('nilai.txt')
o=list()

for data in fileData:
    data=data.replace('\n','')
    data=int(data)
    o.append(data)
print(o)
for i in range (1,len(o)):
    index1=o[i]
    for j in range(i):
        print(index1,"<",o[i-1])
        if i>0 and o[i-1]>index1:
            o[i]=o[i-1]
            i=i-1
            o[i]=index1
    print(o)
