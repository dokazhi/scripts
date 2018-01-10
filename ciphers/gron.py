A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2  # алфавит
def f(text, k, op):
    k *= len(text) // len(k)
    if len(text)%len(k)!=0:
    	k=k+''.join([k[i] for i in range(len(text)%len(k))])

    key=[]
    for w in k:
    	key+=[A.find(w)]
    b = list(enumerate(A))
    res=''
    i=0
    for w in text:
    	res+=A[A.index(w)+(key[i]*op)]
    	i+=1
    return res
def encrypt(message, key):
    return f(message, key, 1)
def decrypt(ciphertext, key):
    return f(ciphertext, key, -1)

print("""
	ВНИМАНИЕ!!!(ATTETION!!!)
ИСПОЛЬЗУЕТСЯ ЛАТИНИЦА!(LATIN ALPAHBET IS ON USE!)
ВВОДИТЕ ТЕКСТ И КЛЮЧ НА ЛАТИНИЦЕ!
	""")
op = input('Шифровать/Дешифровать? Enrypt/Decrypt?(0-enc,1-dec)')
if op=='0' or op=='1':
	text = input('Введите текст(Input text): ')
	key = input('Введите ключ(Input key): ')
	result = encrypt(text.upper(), key.upper()) if op=='0' else decrypt(text.upper(), key.upper())
	print('RESULT IS: '+result)  # расшифровывание
else:
	print('WRONG OPTION! Sorry and bye bye')

