import itertools

print('\n------------------\n\n G 0 B L ! N | WORDGENERATOR\n\n      ~ by: UndeadSec\n\n------------------\n')

escala = input('Please provide a size scale(i.e: "1 to 5" = 1:5) : ')
inicial = int(escala.split(':')[0])
final = int(escala.split(':')[1])

chrs = 'abcdefghijklmnopqrstuvwxyz'
chrs_up = chrs.upper()
chrs_especiais = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numericos = '1234567890'

arq_nome = input('Insert a name for your wordlist file: ')
arq = open(arq_nome, 'w')
if input('Do you want to use uppercase characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
if input('Do you want to use special characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_especiais])
if input('Do you want to use numeric characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_numericos])

for i in range(inicial, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()
