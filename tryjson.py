import json
import random

data = {}  
data['strategy_1'] = {}
data['strategy_1']['game_no'] = []
data['strategy_1']['outcome'] = []

data['strategy_2'] = {}
data['strategy_2']['game_no'] = []
data['strategy_2']['outcome'] = []

for i in range(100):
	data['strategy_1']['game_no'].append(i)
	data['strategy_1']['outcome'].append(random.choice([0,1]))
	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)


with open('data.json', 'r') as infile:
	raw_data = json.load(infile)
