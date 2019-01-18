handle = open("Perepis.txt", "r")
a=int(input())
b=int(input())



for line in handle:
    d=line.split('.')
    n=line.split(' ')
    if(a<=int(d[2])<=b):
        print(n[0],n[2],n[4])
    if(int(d[2])<1978):
        print(n[0])




handle.close()