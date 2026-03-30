text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way
to do it.
Although that way may not be obvious at first unless you're
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good
idea.
Namespaces are one honking great idea -- let's do more of
those!"""

def text_stats(text):
    lines = text.split('.\n')
    line_count= len(lines)
    word_count = len(text.split())
    # promediar la cantidad de palabras por linea y redondear el numero hasta 2 decimales
    average = round(word_count / line_count, 2)

    print(f'Total de líneas: {line_count}')
    print(f'Total de palabras: {word_count}')
    print(f'Promedio de palabras por línea: {average}\n')
    print(f'Líneas por encima del promedio ({average} palabras): ')

    # list comprehension para la lista de lineas que superan el promedio
    line_list = [line + f" ({len(line.split())} palabras)" 
        for line in lines 
        if len(line.split()) > average]
        
    for line in line_list:
        print(f' - {line}')
        
if __name__ == "__main__":
        text_stats(text)