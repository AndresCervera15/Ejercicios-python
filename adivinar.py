
import random

def main():
	print
	limite = int(input('hasta que numero desea adivinar?'))
	number_found = False
	random_number  = random.randint(0,limite)

	while not number_found:
		number = int(input('Adivina el número (; ---> '))

		if number == random_number:
			print('Felicidades el numero era {}'.format(random_number))
			number_found = True

		elif number > random_number:
			print('El numero es mas pequeño')
		else:
			print('El numero es mas grande')




if __name__ == '__main__':
	main()