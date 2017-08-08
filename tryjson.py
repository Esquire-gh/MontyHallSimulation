import json
import random
import threading

data = {}  
data['strategy_1'] = {}
data['strategy_1']['game_no'] = []
data['strategy_1']['outcome'] = []

data['strategy_2'] = {}
data['strategy_2']['game_no'] = []
data['strategy_2']['outcome'] = []

def store_data_1():
	for i in range(100):
		data['strategy_1']['game_no'].append(i)
		data['strategy_1']['outcome'].append(random.choice([0,1]))
		with open('data.json', 'w') as outfile:
			json.dump(data, outfile)


def store_data_2():
	for i in range(100):
		data['strategy_2']['game_no'].append(i)
		data['strategy_2']['outcome'].append(random.choice([0,1]))
		with open('data.json', 'w') as outfile:
			json.dump(data, outfile)


def Main():
	t1 = threading.Thread(target=store_data_1)
	t2 = threading.Thread(target=store_data_2)

	t1.start()
	t2.start()

if __name__=="__main__":
	Main()