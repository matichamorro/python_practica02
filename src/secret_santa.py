import random
from collections import Counter

def mix_up_list():
    participants = input("Ingrese los participantes (separados por coma): ").split(',')
    participants = [participant.strip().capitalize() for participant in participants]
    participants = list(Counter(participants).keys())

    random_list = random.sample(participants,len(participants))
    
    pairs = {}
    for p in participants:
        pair = random.choice(random_list)
        while (pair == p):
            pair = random.choice(random_list)
        pairs[p] = pair
        random_list.remove(pair)
    
    print("Sorteo de amigo invisible: ")
    for p in participants:
        print(f"    {p} -> {pairs[p]}")
