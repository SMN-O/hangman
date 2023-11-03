# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Implemented is a Hangman class which has 2 methods check_guess and ask_for_input

check_guess will set some rules to check the letter entered from the user once prompted from ask_for_input and compare it to the word from word_list

ask_for_input wil produce a loop to reiterate through guessing a letter and prompting the user if it's invalid or if it has been guessed. 

play_game sets the game outside of the class and sets the parameters to win and lose the game by taking in word_list and num_lives.
