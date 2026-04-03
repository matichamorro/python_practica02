
def caesar_cipher():
    
    message = input("Ingrese su mensaje: ")
    num = int(input("Ingrese un valor entero de desplazamiento: "))
    ciphered_result = ""
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            ciphered_result += chr((ord(char) - start + num) % 26 + start)
        else:
            ciphered_result += char
        
    print(f"Mensaje cifrado: {ciphered_result}")
    
    deciphered_result = ""
    for char in ciphered_result:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            deciphered_result += chr((ord(char) - start - num) % 26 + start)
        else:
            deciphered_result += char
            
    print(f"Mensaje descifrado: {deciphered_result}")