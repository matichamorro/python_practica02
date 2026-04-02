from collections import Counter

posts = [
    "Arrancando el lunes con energía #Motivación #NuevaSemana",
    "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
    "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
    "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
    "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
    "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
    "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
    "Finde de lluvia, maratón de series #SerieAdicta #Relax",
    "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]

def analyse_hashtag(posts):
    unified_posts = ""
    for post in posts:
        unified_posts += f" {post}"

    filtered_words = list(filter(lambda word: word.startswith('#'),unified_posts.split()))

    hashtag_count = Counter(filtered_words)

    filtered_hashtags = list(filter(lambda hashtag: hashtag[1] > 1,hashtag_count.items()))
    filtered_hashtags = sorted(filtered_hashtags, key=lambda item: item[1], reverse=True)

    print("Hashtag trending (más de una aparición): ")
    for hashtag in filtered_hashtags:
        print(f"    {hashtag[0]}: {hashtag[1]}")
    

    
    
