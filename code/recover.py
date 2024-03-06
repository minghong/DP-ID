#压缩：个数+比特信息
with open("D:\\1.txt", 'r') as file:
    for line in file:
        line = line.strip()
        data = line.split(" ")


#编码
count=0
str=""
with open("D:\\result2.txt", 'r') as file:
    for line in file:
        line = line.strip()
        tmp = line.split(" ")
        for i in range(int(tmp[0])):
            binary_str = bin(int(data[count+i]))[2:]
            binary_str = '0' * (int(tmp[1]) - len(binary_str)) + binary_str
            
            str+=binary_str
        count+=int(tmp[0])

count=0
d=[]
#信息恢复
with open("D:\\result2.txt", 'r') as file:
    for line in file:
        line = line.strip()
        tmp = line.split(" ")
        a=int(tmp[0]);b=int(tmp[1])
        for i in range(a):
            d.append(int(str[count+i*b:count+(i+1)*b],2))
        
        count+=(a*b)
    print(a,b)
    
'''
matrix = [[0 for _ in range(256)] for _ in range(256)]
col=256;row=256;kk=0
for i in range(col):
    if(i%2==0):
        for j in range(row):
            matrix[i][j]=d[kk] 
            kk+=1
            
    else:
        for j in range(row-1,-1,-1):
            matrix[i][j]=d[kk] 
            kk+=1
'''        

