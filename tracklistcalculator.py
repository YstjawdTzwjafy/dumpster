a = int(input("Quantidade de músicas: "))
nome = [None] * a
dur = [None] * a
minu = [None] * a
for i in range(a):
    nome[i] = input("Nome da música: ",)
    dur[i] = (input("Duração da música: "))
    minu[i] = dur[i][dur[i].find(':')+1:]
    dur[i] = dur[i][:dur[i].find(':')]

for i in range(a):
    if(i==0): 
        res=0
        minutos=0
    else:
        res += int(dur[i-1])
        minutos += int(minu[i-1])
        if(minutos>=60):
            minutos-=60
            res+=1
    res1 = str(res)
    res2 = str(minutos)
    if(len(res1)<2): res1 = "0" + res1
    if(len(res2)<2): res2 = "0" + res2
    print("%s %s:%s"%(nome[i],res1,res2))
