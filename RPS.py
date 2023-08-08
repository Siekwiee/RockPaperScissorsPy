import random

Possibilities = ['rock', 'paper', 'scissors']
CpuChoice = random.choice(Possibilities)
print(f'Lets play RockPaperScissors!!!\nMake Your Choise')
PlayerChoice = input().lower()

if PlayerChoice == CpuChoice:
    print(f'The computer chose {CpuChoice}, so its a draw')

if PlayerChoice == 'rock' and CpuChoice == 'paper':
    print(f'You loose!  The computer chose: {CpuChoice}')

if PlayerChoice == 'rock' and CpuChoice == 'scissors':
    print(f'You win!  The computer chose: {CpuChoice}')

if PlayerChoice == 'paper' and CpuChoice == 'scissors':
    print(f'You loose!  The computer chose: {CpuChoice}')

if PlayerChoice == 'paper' and CpuChoice == 'rock':
    print(f'You win!  The computer chose: {CpuChoice}')

if PlayerChoice == 'scissors' and CpuChoice == 'rock':
    print(f'You loose!  The computer chose: {CpuChoice}')

if PlayerChoice == 'scissors' and CpuChoice == 'paper':
    print(f'You win!  The computer chose: {CpuChoice}')

