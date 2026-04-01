rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7,
            'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 8,
            'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 8},
            'Santiago': {'judge_1': 6, 'judge_2': 7,
            'judge_3': 6},
            'Lucía': {'judge_1': 8, 'judge_2': 8,
            'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 8},
            'Mateo': {'judge_1': 8, 'judge_2': 7,
            'judge_3': 9},
            'Camila': {'judge_1': 7, 'judge_2': 6,
            'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 8,
            'judge_3': 8},
            'Lucía': {'judge_1': 7, 'judge_2': 8,
            'judge_3': 7},
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8,
            'judge_3': 7},
            'Mateo': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 8},
            'Camila': {'judge_1': 8, 'judge_2': 7,
            'judge_3': 9},
            'Santiago': {'judge_1': 7, 'judge_2': 7,
            'judge_3': 6},
            'Lucía': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9,
            'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 6,
            'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 8,
            'judge_3': 8},
            'Santiago': {'judge_1': 8, 'judge_2': 9,
            'judge_3': 7},
            'Lucía': {'judge_1': 7, 'judge_2': 7,
            'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8,
            'judge_3': 9},
            'Mateo': {'judge_1': 8, 'judge_2': 9,
            'judge_3': 8},
            'Camila': {'judge_1': 7, 'judge_2': 7,
            'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 9,
            'judge_3': 9},
            'Lucía': {'judge_1': 8, 'judge_2': 8,
            'judge_3': 7},
        }
    }
]

# retorna un dict con formato "nombre: puntaje_total" ordenado de mayor a menor 
def rank_round(round):
    scores = round['scores']
    # generar un dict con formato "nombre: puntaje_total"
    p_score = {participant: sum(score.values()) for participant, score in scores.items()}
    # reordenar el dict separando en items (0: nombre, 1: puntaje_total), buscando en [1] y de mayor a menor (reverse=true)
    p_score = sorted(p_score.items(), key=lambda item: item[1], reverse=True)
    return p_score

def generate_ranking(rounds):
    # iniciar un marcador global de los datos a guardar
    global_scoreboard = {name: {'total': 0,
                            'r_won': 0,
                            'best_round': 0
                            } 
                        for name in rounds[0]['scores'].keys()}
    
    
    for i, round in enumerate(rounds, 1):
        
        # mostrar el ranking de cada ronda junto con el titulo
        print(f"Ronda {i} - {round['theme']}:")
    
        current_round = rank_round(round)
        current_winner = current_round[0]
        
        print(f"    Ganador/a: {current_winner[0]} ({current_winner[1]} pts)")
        index_current_round = list(enumerate(current_round, 1))
        for i in range(1,5):
            print(f"    {i}. {current_round[i][0]} ({current_round[i][1]} pts)")
        
        # usar el valor de retorno de la funcion para aumentar los marcadores globales
        global_scoreboard[current_winner[0]]['r_won'] += 1
        for name, total in current_round:
            global_scoreboard[name]['total'] += total
            if total > global_scoreboard[name]['best_round']:
                global_scoreboard[name]['best_round'] = total

        print()


    print('Tabla de posiciones final:')
    print("Cocinero     Puntaje     Rondas ganadas     Mejor ronda     Promedio")
    print("--------------------------------------------------------------------")
    for name in global_scoreboard:
        values =  global_scoreboard[name]
        print(f"{name:<9}      {values['total']:<9}       {values['r_won']:<11}   {values['best_round']:^8}      {values['total'] / len(rounds):^10}")
    print("--------------------------------------------------------------------")

# Por si se quiere probar a ejecutarlo desde este archivo
if __name__ == "__main__":
    generate_ranking(rounds)

    