import re
import random

def __main__():
	artist_list = open("artists.txt").readlines()
	album_list = open("album_names.txt").readlines()
	score = 0;

	print("Hello! Welcome to a guessing game! In this game, you'll be given the name of an album and you'll have to guess the artist.\n")
	size = (int(input("How many questions would you like to have? The maximum is 60. ")))
	
	#generate a list of numbers from 0 to 59, inclusive
	numbers = list(range(0, 60))
	#create a list of of the user-given size, containing non-repeating numbers from 0 to 59, inclusive
	k = random.sample(numbers, size)
	for i in range(0,len(k)):
		print(k)
		print(album_list[k[i]])
		user_answer = input("Whose album is this?\n")
		if (user_answer.lower() == (artist_list[k[i]].lower()).replace("\n", "")):
			score = score + 1	

	print("Congrats! You got %d out of %d correct!" % (score, size))


__main__()




