import play_the_game
import json_reader

#THIS IS THE MAIN MENU#

if __name__ == '__main__':
    dare_list = json_reader.read_dare_json() # read dare list
    truth_list = json_reader.read_truth_json() # read truth list
    player_list = play_the_game.truth_dare_game(truth_list, dare_list) #its call the truth_dare_game function here.
    play_the_game.final_score(player_list) # its call the final score


