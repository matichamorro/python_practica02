playlist = [
    {"title": "Bohemian Rhapsody", "duration": "5:55"},
    {"title": "Hotel California", "duration": "6:30"},
    {"title": "Stairway to Heaven", "duration": "8:02"},
    {"title": "Imagine", "duration": "3:07"},
    {"title": "Smells Like Teen Spirit", "duration": "5:01"},
    {"title": "Billie Jean", "duration": "4:54"},
    {"title": "Hey Jude", "duration": "7:11"},
    {"title": "Like a Rolling Stone", "duration": "6:13"},
]

def total_duration(playlist):
    total_minutes = 0
    total_seconds = 0
    
    # convertir la duración a un int y almacenarlo en minutos y segundos totales
    for song in playlist:
        song_dur = song['duration'].split(':')
        total_minutes += int(song_dur[0])
        total_seconds += int(song_dur[1])
        
    # conversión de 60 segundos a 1 minuto
    aux_minutes, aux_seconds = divmod(total_seconds, 60)
    total_seconds = aux_seconds
    total_minutes += aux_minutes
    
    return f'{total_minutes}m {total_seconds}s'
        

def longest_and_shortest_song(playlist):
    # generar una lista de las duraciones de cada canción
    durations = [song['duration'].split(':') for song in playlist]
    
    # generar un índice para cada elemento
    durations = list(enumerate(durations))
    
    # ordenar la lista segun su duración de mayor a menor
    durations = sorted(durations, key=lambda item: item[1], reverse=True)
    
    longest_song = durations[0][0]
    shortest_song = durations[len(durations) - 1][0]
    
    return longest_song, shortest_song
   
def playlist_durations(playlist):
    total_dur = total_duration(playlist)
    print(total_dur)

    max_song, min_song = longest_and_shortest_song(playlist)

    print(f'Canción más larga: "{playlist[max_song]['title']}" ({playlist[max_song]['duration']})')
    print(f'Canción más corta: "{playlist[min_song]['title']}" ({playlist[min_song]['duration']})')

