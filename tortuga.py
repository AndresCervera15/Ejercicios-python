import turtle

def main():
	window = turtle.Screen()
	andres = turtle.Turtle()

	make_square(andres)
	turtle.mainloop()


def make_square(andres):
	length = int(input('Tamaño del cuadrado: '))

	for i in range(4):
		make_line_and_turn(andres, length)

def make_line_and_turn(andres, length):
	andres.forward(length)
	andres.left(90)


if __name__ == '__main__':
	main()