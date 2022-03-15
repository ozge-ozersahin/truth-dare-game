# Truth or Dare
# Team 3:
# Rose Gruebner
# Ozge Donmez
# Paola Chicaiza

import Gamer
import random


def truth_dare_game(truth_list, dare_list):  ### create function. this function initialize the game.

    print("Welcome to Truth or Dare")
    print("How many players are you?: ")
    number_players = int(input()) #this is for the get "how many players will play" output.And the output return integer
    player_list = []                                     # created a player list. its include the player names and gamer classes
    for player in range(number_players):
        player_name = input("Insert your name: ")                    #for the player names output
        player = Gamer.Gamer(player_name, 0)                 #### add to gamer class for the keep the score and player name at the same time
        player_list.append(player)                         #appending the class at the player list. the class return list.

    for player in player_list:
        print("Players: ", player.name)

    rounds = 20                                  ### should be 20 rounds.
    for round in range(rounds):
        print("Round:", round + 1)
        player = random.choice(player_list)       ### add random.choice from player list and this is get the player name
        print("Your Turn : ", player.name)
        truth_dare = input("Truth or Dare?: ")

        if truth_dare == "truth":

            random_truth = random.choice(truth_list)  ####  add random.choice from truth list for the truth question
            print("Your Truth Question is:")
            print(random_truth)
            completed = input("Complete? y/n:")

            if completed == "y":
                player.score = player.score + 1         # if the player complete the question, score adding +1
            elif completed == "n":                      # if the player doesn't complete the question than score  adding nothing
                player.score = player.score + 0

        if truth_dare == "dare":
            random_dare = random.choice(dare_list)  #### add random choice from dare list for the dare questions
            print("Your Dare is:")
            print(random_dare)
            completed = input("Complete? y/n:")

            if completed == "y":
                player.score = player.score + 1
            elif completed == "n":
                player.score = player.score + 0

    return player_list ##


def final_score(player_list): # created the final score function. this is show us player name with the score result
    for i in player_list:
        print(i.name, ": ", i.score)

