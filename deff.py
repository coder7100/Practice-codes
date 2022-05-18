#the equation is g^a %p

p=int(input('enter the modulo(p) value'))
g=int(input('enter the value of g'))

alice=int(input('Enter the secret key of alice(a)'))
bob=int(input(('Enter the secret value of bob')))

key_A=pow(g,alice,p)
key_B=pow(g,bob,p)

#now exchanging the values

key_A_B=pow(key_A,bob,p)
key_B_A=pow(key_B,alice,p)

print(key_A_B)
print(key_B_A)

print('Hence the key matches and both bob and alice can share key')