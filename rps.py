import random

player = input('Enter your name: ')
print(f'Hello, {player}')

score = 0
rating = open('rating.txt')
for rate in rating:
    if player in rate:
        score = int(rate.split()[1])
rating.close()

winning_cases = {
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

option = input().split(',')
if len(option) == 1:
    option = ['scissors', 'paper', 'rock']
print("Okay, let's start")
while True:
    user = input()
    computer = random.choice(option)
    
    if user == '!rating':
        print(score)
        continue
    elif user == '!exit':
        print('Bye!')
        break
    elif user not in option:
        print(option)
        print('Invalid input')
        continue
        
    if user == computer:
        print('There is a draw ({})'.format(computer))
        score += 50
    elif computer in winning_cases[user]:
        print('Well done. The computer chose {} and failed'.format(computer))
        score += 100
    elif computer not in winning_cases[user]:
        print('Sorry, but the computer chose {}'.format(computer))
