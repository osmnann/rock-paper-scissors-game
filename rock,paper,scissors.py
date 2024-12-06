import random

def play():
    user=input("what is you choice? 'r' for rock 'p' for paper 's' for scissors \n ")
    computer=random.choice(['r','p','s'])

    if user == computer:
        return 'Tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    if is_win(computer, user):
        return 'You lost!'

def is_win(player, opponent):
#return if player wins
    #r > s, s > p, p > r
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') \
    or (player=='p' and opponent=='r'):
        return True 