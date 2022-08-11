#наибольший общий простой делитель

#этот цикл проверяет условие

def kuku(n):
    count = 0
    for i in range(1, n+1):
        if n%(i)==0:
            count+=1
            if count==2 and i==n:
                return True

def main(k):
    for i in range(k+1, 1):
        if kuku(i):
            break
            return i


print(main(3))

