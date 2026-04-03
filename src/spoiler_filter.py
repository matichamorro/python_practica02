review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""

def input_spoilers():
    """This function input spoilers and returns a list of them"""

    spoiler = input('Ingresar palabras que se consideren spoilers: ')
    spoiler_list = [s.upper().strip() for s in spoiler.split(',')]

    return spoiler_list

def replace_spoilers(review):
    spoilers = input_spoilers()
    review_without_spoilers = ""
    for word in review.split():
        if word.upper() in spoilers:
            review_without_spoilers += f"{'*' * len(word)} "
        else:
            review_without_spoilers += f"{word} "
    print(review_without_spoilers)
    
