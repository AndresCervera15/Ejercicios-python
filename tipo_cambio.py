#-*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
	mex_to_col_rate =0.051

	return mex_to_col_rate * ammount

def run():
	print('C A L C U L A D O R A  D E  D I V I S A S')
	print('convertir de mx a eu')
	print('')

	ammount = float(input('ingresa la cantidad de pesos mx'))

	result = foreign_exchange_calculator(ammount)

	print('${} pesos mexicanos son ${} dolares'.format(ammount, result))

if __name__ == '__main__':
	run()