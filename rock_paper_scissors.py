#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self, current_round):
        return 'rock'

    def learn(self, p1, p2):
        self.p1_move = p1
        self.p2_move = p2


class RandomPlayer(Player):
    def move(self, current_round):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self, current_round):
        while True:
            move = input("Rock, Paper or Scissors?\n").lower()
            if move in moves:
                return move
            print("That's not a valid option. Please try again.")


class ReflectPlayer(Player):
    def move(self, current_round):
        if current_round == 0:
            return random.choice(moves)
        return self.p2_move


class CyclePlayer(Player):
    def move(self, current_round):
        if current_round == 0:
            return random.choice(moves)
        if self.p1_move == "rock":
            return "paper"
        if self.p1_move == "paper":
            return "scissors"
        return super().move(current_round)


def beats(one, two):
    return (one == 'rock' and two == 'scissors' or
            one == 'scissors' and two == 'paper' or
            one == 'paper' and two == 'rock')


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.current_round = 0

    def play_round(self):
        p1_move = self.p1.move(self.current_round)
        p2_move = self.p2.move(self.current_round)
        print(f"Player 1: {p1_move} -- Player 2: {p2_move}")
        if beats(p1_move, p2_move):
            print("Player 1 has won!")
            self.p1_score += 1
        elif beats(p2_move, p1_move):
            print("Player 2 has won!")
            self.p2_score += 1
        else:
            print("It's a tie!")
        print(f"Score: {self.p1_score} : {self.p2_score}\n")
        self.p1.learn(p1_move, p2_move)
        self.p2.learn(p2_move, p1_move)
        self.current_round += 1

    def play_game(self):
        print("Game start!\n")
        total_rounds = input_int("How many rounds would you like to play? ")
        for current_round in range(total_rounds):
            print(f"Round {current_round + 1}:")
            self.play_round()
        print("Game over!")
        if self.p2_score > self.p1_score:
            print("Player 2 has won the game. Congratulations!")
        elif self.p2_score < self.p1_score:
            print("Player 1 has won the game. Congratulations!")
        else:
            print("It was a tied game.")


class PlayerException(Exception):
    pass


class PlayerFactory:
    def get_player(self, player_id):
        if player_id == 1:
            return Player()
        if player_id == 2:
            return RandomPlayer()
        if player_id == 3:
            return CyclePlayer()
        if player_id == 4:
            return ReflectPlayer()
        raise PlayerException("That's not a valid player. Try again.\n")


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


if __name__ == '__main__':
    print("Welcome to the game!")
    player1 = HumanPlayer()
    player_factory = PlayerFactory()

    while True:
        player_id = input_int("Select the type of player "
                              "you want to play against:\n"
                              "1 for Rock Player\n"
                              "2 for Random Player\n"
                              "3 for Cycle Player\n"
                              "4 for Reflect Player\n")
        try:
            player2 = player_factory.get_player(player_id)
            break
        except PlayerException as player_exception:
            print(player_exception)

    game = Game(player1, player2)
    game.play_game()
