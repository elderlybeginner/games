#!/usr/bin/env python3
'''Tic-Tac-Toe game.'''

import random
import sys


def create_board():
	board = ' ' * 9
	return board


def show_tips():
	print('\n\nUse 1-9 to play.')
	print('Just like Num keys')
	print('┌───┬───┬───┐' )
	print('│ 7 │ 8 │ 9 │')
	print('├───┼───┼───┤')
	print('│ 4 │ 5 │ 6 │')
	print('├───┼───┼───┤')
	print('│ 1 │ 2 │ 3 │')
	print('└───┴───┴───┘')


def ask_mark_type():
	while True:
		print('Do you prefer to play with X or with O?')
		mark = input('').upper()
		if mark == 'X':
			return 'X', 'O'
		elif mark == 'O':
			return 'O', 'X'
		print('Improper choice.')


def choose_player():
	if round(random.random()) == 1:
		return 'player'
	return 'computer'


def print_board(board):
	print('┌───┬───┬───┐' )
	print('│', board[6], '│', board[7], '│', board[8], '│')
	print('├───┼───┼───┤')
	print('│', board[3], '│', board[4], '│', board[5], '│')
	print('├───┼───┼───┤')
	print('│', board[0], '│', board[1], '│', board[2], '│')
	print('└───┴───┴───┘')


def ask_input():
	while True:
		choice = input('Please, enter valid position (1-9): ')
		if validate(choice) == 'correct':
			break
	return int(choice) - 1


def validate(choice):
	try:
		if choice in '1 2 3 4 5 6 7 8 9':
			if board[int(choice) - 1] != ' ':
				print('The position is already taken.')
				return 'incorrect'
			return 'correct'
		else:
			print('Improper choice.')
			return 'incorrect'
	except ValueError:
		print('Very improper choice.')
		return 'incorrect'


def make_move(board, mark, cmark):
	win_position = go_for_win(board, cmark)
	if win_position is not None:
		print('going for the win with:', win_position + 1)
		return win_position
	defend_position = go_for_win(board, mark)
	if defend_position is not None:
		print('defending with:', defend_position + 1)
		return defend_position
	# take middle in most cases
	if board != '         ':
		if board[4] == ' ':
			print('taking the middle')
			return 4
	# take an empty corner
	corners = random.choices([0, 2, 6, 8], k=4)
	for c in corners:
		if board[c] == ' ':
			print('taking a random corner')
			return c
	# take any
	leftover = [p for p, c in enumerate(board) if c == ' ']
	print('leftover taking')
	return random.choice(leftover)


def go_for_win(board, cmark):
	board_copy = board
	positions_to_check = [p for p, c in enumerate(board) if c == ' ']
	for p in positions_to_check:
		board_copy = board_copy[0:p] + cmark + board_copy[p + 1:]
		result = check_result(board_copy, cmark)
		if result == 'win':
			return p
		board_copy = board
	return None


def mark_board(who, choice, board):
	if who == 'computer':
		board = board[0:choice] + cmark + board[choice + 1:]
	else:
		board = board[0:choice] + mark + board[choice + 1:]
	print_board(board)
	return board


def check_result(board, mark):
	board_value = 0
	for i in range(9):
		if board[i] == mark:
			board_value += 2 ** i
	winning_board = [
		0b111000000,
		0b000111000,
		0b000000111,
		0b100100100,
		0b010010010,
		0b001001001,
		0b100010001,
		0b001010100]
	for b in winning_board:
		if b & board_value == b:
			return 'win'
	if ' ' in board:
		return 'not_finished'
	return 'draw'


def result_info(result, who):
	print('GAME FINISHED.')
	if result == 'draw':
		print('The resalut is: draw :(')
	else:
		print(f'{who.upper()} has won the game. Congratulations.')


board = create_board()
show_tips()
mark, cmark = ask_mark_type()
who = choose_player()
print(who)
print('Game starts now.')
print(f'You\'ve chose to play with {mark} and by coin toss {who} starts.')
print_board(board)
while True:
	if who == 'player':
		choice = ask_input()
		board = mark_board(who, choice, board)
		result = check_result(board, mark)
		if result == 'win' or result == 'draw':
			result_info(result, who)
			sys.exit()
		who = 'computer'
	else:
		choice = make_move(board, mark, cmark)
		board = mark_board(who, choice, board)
		result = check_result(board, cmark)
		if result == 'win' or result == 'draw':
			result_info(result, who)
			sys.exit()
		who = 'player'
