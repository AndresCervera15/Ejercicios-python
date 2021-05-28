

def suma(numero):
	if numero == 1:
		return 1

	return numero + suma(numero-1)
	


if __name__ == '__main__':
	
	numero = int(input('Escriba un numero: '))


	resultado = suma(numero)

	print(resultado)