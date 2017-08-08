import random
import json

class Simulation:
	'''
	
	This is code that simulates the monty hall problem
	Author: Code_X Group

	
	'''

	def __init__(self, strategy):
		self.option = [1,2,3]
		self.prize = ['goat', 'goat', 'car']
		self.host_options = []
		self.strategy = strategy
		print("Starting New Game: ")



	#method that shuffles the doors and the prizes behind them
	def get_choices(self):
		for i in range(len(self.option)):
			random.shuffle(self.option)
			random.shuffle(self.prize)	

		choices = {}
		for index in range(len(self.option)):
			choices[str(self.option[index])] = self.prize[index]

		return choices


	#Checking the door which has the main prize(car)
	def check_car_index(self, choices):
		for key,value in choices.items():
			if choices[str(key)] == 'car':
				prize = key
			else:
				pass
		return int(prize)

	# Ask the User for an Input
	def simulate_user_input(self):
		user_input = random.randrange(1,4)
		
		return user_input

	# Function that simulate the game host choosing a fake door
	def hosts_dummy_choice(self, user_input, car_index, choices):
		for key,value in choices.items():
			if int(key) == user_input or int(key) == car_index:
				pass
			else:
				self.host_options.append(int(key))

		for i in range(len(self.host_options)):
			return random.choice(self.host_options)
	
	def possible_options_left_for_user(self, user_input, host_choice):
		possible_options = []
		for door in self.option:
			if door == user_input or door == host_choice:
				pass
			else:
				possible_options.append(door)
				return possible_options


	# Get the final answer from the user
	def get_confirmation(self, user_input, options_left):
		if self.strategy == 1: #strategy 1 means the user maintains his first choice
			final_user_input = user_input
		
		elif self.strategy == 2:
			final_user_input = random.choice(options_left)
		
		else:
			print('Wrong Strategy input, Try Again!!!!') 

		return final_user_input


	#Check win/Lose method
	def check_results(self, final_answer, car_index):
		# Checking for winner or Loser 
		if final_answer == car_index:
			print("YOU WON!!!!!")
		else:
			print("YOU LOSE!!!!")



def main():
	
	#instance of newGame
	newGame = Simulation(2)

	#getting the choices of doors and prices through shuffling
	choices = newGame.get_choices()

	#tracking car_index
	car_index = newGame.check_car_index(choices)

	#simulating user input
	user_input = newGame.simulate_user_input()

	#make host open a fake door
	host_choice = newGame.hosts_dummy_choice(user_input, car_index, choices)

	#get user options left
	options_left = newGame.possible_options_left_for_user(user_input, host_choice)
	
	#asking for final answer
	final_answer = newGame.get_confirmation(user_input, options_left)

	#CHECKING FOR WIN/LOSE
	newGame.check_results(final_answer, car_index)


if __name__ == '__main__':
	main()