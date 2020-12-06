#!/usr/bin/env python3

'''Eight queen puzzle generator by Elderlybeginner'''

def validate_setup(q):
	queens = q[:]
	while queens:
		queen = queens.pop()
		mask = make_mask(queen)
		for left_queen in queens:
			if left_queen in mask:
				return False
	return True

def make_mask(queen):
	mask = set()
	div, mod = divmod(queen, width)
	row_start = div * width
	for i in range(width):
		mask.add(row_start + i)  # row mask
		mask.add(mod + i * width)  # column mask
	operations = ((1, 1), (-1, -1), (1, -1), (-1, 1))
	for i in range(min([width, height])):  # diagonal mask
		for operation in operations:
			cellx = mod + operation[0] * i
			celly = div + operation[1] * i
			if 0 <= cellx < width and 0 <= celly < height:
				mask.add(celly * width + cellx)
	return mask

def print_board(queens):
	board = ['\u25a1' if i % 2 else '\u25a0' for i in range(limit + 1)]
	for queen in queens:
		board[queen] = '\u2655'
	for e, cell in enumerate(board):
		if not (e + 1) % width:
			print(cell)
		else:
			print(cell, end='')

def find_position():
	result = validate_setup(queens)
	if not result:
		while queens[-1] == limit:
			queens.pop()
		queens[-1] += 1
		find_position()
	else:
		return True

def find_solution():
	while True:
		for i in range(queens[-1] + 1, limit + 1):
			queens.append(i)
			find_position()
			if len(queens) == pieces:
				return True
			break
		else:
			queens.pop()
			if not queens:
				return False
			queens[-1] += 1

width = 8
height = 8
pieces = 8
limit = width * height - 1
queens = [0]
counter = 0
solutions = dict()

welcome_message = "Eight queens puzzle\n"\
	"There are 92 distinct solutions and 12 fundamental ones\n"\
	"more in the subject: https://en.wikipedia.org/wiki/Eight_queens_puzzle\n"\
	"----------------------------------------------------------------------\n"\
	"The program generates all 92 distinctive solutions...\n"
print(welcome_message)

while True:
	result = find_solution()
	while not result:
		answer = input('\nWhich solution is to be printed? (1-92) (Enter = Exit) (all = all): ')
		if answer == '':
			exit()
		elif answer == 'all':
			print(*solutions.items(), sep='\n')
			print()
		else:
			try:
				answer = int(answer)
				print(solutions[answer])
				print_board(solutions[answer])
			except ValueError:
				print('Invalid input')
				exit()
			except:
				print('Out of range')
				exit()
	counter += 1
	print(end='.', flush=True)
	solutions[counter] = queens.copy()
	queens.pop()
	queens[-1] += 1
