from game_data import data
from art import logo, vs
from replit import clear
import random

def format_data(data_dict):
	return f"{data_dict['name']}, a {data_dict['description']}, from {data_dict['country']}"

def generate(new_data):
	'''Take a list of dictionaries as input and returns a random dictionary'''
	new_key = random.choice(new_data)
	return new_key

def get_follower_count(data_dict):
	'''Takes a dictionary as input and returns the data associated to the follower_count'''
	return data_dict["follower_count"]

def is_correct(user_choice, a, b):
	'''Takes user_choice/guess, 2 random options from the dictionary as input and returns true if the user_choice is correct else return false'''
	a_followers = get_follower_count(a)
	b_followers = get_follower_count(b)
	if a_followers > b_followers:
		return user_choice == 'a'
	else:
		return user_choice == 'b'

print(logo)
score = 0
end_game = False
b = generate(data)
	
while not end_game:
	a = b
	while a == b:
		b = generate(data)
	if score != 0:
		print(f"You're right! Current Score: {score}.")
	print(f"Compare A: {format_data(a)}")
	print(vs)
	print(f"Against B: {format_data(b)}")
	guess = input("Who has highest followers? Type 'A' or 'B': ").lower()
	clear()
	print(logo)
	
	if is_correct(guess, a, b):
		score += 1
	else:
		print(f"Sorry, that's wrong. Final Score: {score}")
		end_game = True
