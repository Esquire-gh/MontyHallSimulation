import random


class MontyHallGame:
	'''
	
	This is code that simulates the monty hall problem
	Author: Esquire_gh

	
	'''

	def __init__(self):
		self.option = [1,2,3]
		self.prize = ['goat', 'goat', 'car']
		self.host_options = []
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
	def check_car_prize(self, choices):
		for key,value in choices.items():
			if choices[str(key)] == 'car':
				prize = key
			else:
				pass
		return int(prize)

	# Ask the User for an Input
	def take_input(self):
		user_input = int(input('Please Choose Btwn Doors 1, 2, and 3: '))
		if user_input < 0 or user_input > 3:
			print('Wrong Input')
			user_input = int(input('Please Choose Btwn Doors 1, 2, and 3: '))
		else:
			user_input = user_input

		return user_input

	# Function that simulate the game host choosing a fake door
	def hosts_dummy_choice(self, user_input, car_index, choices):
		for key,value in choices.items():
			if int(key) == user_input or int(key) == car_index:
				pass
			else:
				self.host_options.append(int(key))

		for i in range(len(self.host_options)):
			if self.host_options[i] == car_index:
				pass
			else:
				return self.host_options[i]

	# Get the final anser from the user
	def get_confirmation(self, user_input):
		confirm = str(input("Will you like to change your choice: (y/n)"))
		if confirm == 'n':
			final_user_input = user_input
		elif confirm == 'y':
			final_user_input = int(input("What input will you choose now: "))
		else:
			print("Wrong input, Play Again!")
		return final_user_input

	#Check win/Lose method
	def check_results(self, confirmation, car_index):
		# Checking for winner or Loser 
		if confirmation == car_index:
			print("YOU WON!!!!!")
		else:
			print("YOU LOSE!!!!")



def main():
	#instance of newGame
	newGame = MontyHallGame()

	#generating choices for user
	choices = newGame.get_choices()
	#print("you have the following choices: ")
	#print(choices)

	#tracking index of main prize(car)
	car_index = newGame.check_car_prize(choices)
	#print("the car is in door: ", car_index)

	#getting uer input
	user_input = newGame.take_input()
	print("You have chosen door: ", user_input)

	#host opens a dummy door
	host_option = newGame.hosts_dummy_choice(user_input, car_index, choices)
	print("The host opens door: ",host_option)

	#Host aks for user final confirmation
	confirmation = newGame.get_confirmation(user_input)
	print('Your final choise is: ', confirmation)

	newGame.check_results(confirmation, car_index)


if __name__ == '__main__':
	main()