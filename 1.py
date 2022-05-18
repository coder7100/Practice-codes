def rsa_alg(p:int,q:int,msg:str):

    n=p*q
    z=(p-1)*(q-1)

    e=find_e(z)
    d=find_d(e,z)

    #plain_test->cypher

    cypher=''
    for ch in msg:
        ch=ord(ch)
        cypher+=chr((ch**e)%n)

    #cypher ->plain

    plain=''

    for ch in cypher:
        ch=ord(ch)
        plain+=chr((ch**d)%n)
    return  cypher,plain

def find_e(z:int):
    e=2
    while e<z:
        if gcd(e,z)==1:
            return e
        e+=1

def find_d(e:int,z:int):
    d=2

    while d<z:
        if (e*d)%z==1:
            return d
        d+=1

def gcd(x:int,y:int):
    small,large=(x,y) if x<y else (y,z)

    while small != 0:
        temp=large%small
        large=small
        small=temp

    return large

if __name__=="__main__":
    p=int(input("Enter a prime Number : "))
    q = int(input("Enter another prime Number : "))
    msg=input("Enter the message")

    cypher,plain=rsa_alg(p,q,msg)

    print("encrypted data : ",cypher)
    print('decrypted data : ',plain)

