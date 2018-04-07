import re
import random

def __main__():
	artist_list = open("artists.txt").readlines()
	album_list = open("album_names.txt").readlines()
	score = 0; 
	numbers = list(range(0, 12))

	print("Hello! Welcome to a guessing game! Guess the artist of an album!")
	
	k = random.sample(numbers, 12)
	for i in k:
		print(album_list[k[i]] + "\n")
		user_answer = input("Whose album is this?")
		if (user_answer.lower() == (artist_list[k[i]].lower()).replace("\n", "")):
			score = score + 1	

	print("Congrats! You got %d out of 12 correct!" % score)


__main__()




