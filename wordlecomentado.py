# definir las variables de la palabra secreta e intentos

palabra_secreta = 'pollo'
palabra_corregida = ''
intentos = 4

# solicitamos la palabra al usuario 

palabra_usuario = input('ingresa una palabra de 5 letras')

# comprobamos que el usuario haya ignresado una palabra de  letras 


while len(palabra_usuario) != 5 :
    palabra_usuario = input('ingresa una palabra de 5 letras por favor') 
# creamos el bucle que verifique los intentos disponibles
while intentos > 0:
    
    # verificamos si la palabra ingresada es la correcta (if) o no(else)
    if palabra_usuario != palabra_secreta:
        #verificamos si las letras(indece) en la palabra ingrresada se encuenatran en la palabra correcta con el for in 
        for indice in range(len(palabra_usuario)):
            if palabra_usuario[indice] in palabra_secreta:
                if palabra_usuario[indice] != palabra_secreta[indice]:
                    letra_corregida = '(' + palabra_usuario[indice] + ') '
                    palabra_corregida += letra_corregida
                elif palabra_usuario[indice] == palabra_secreta[indice]:
                    letra_corregida = '[' + palabra_usuario[indice] + '] '
                    palabra_corregida += letra_corregida
            else:
                letra_corregida = palabra_usuario[indice] + ' '
                palabra_corregida += letra_corregida
    # si la palabra ingresada es la correcta 
    else:
        
        print(f'adivinaste la palabra correcta es "{palabra_secreta}"')
    # para la ejecucion cuando ya no quedan intentos 
        break
    # imprime la palabra corregida si no es la correcta 
    print(palabra_corregida)
    #resta los intentos 
    intentos = intentos - 1 
    print('te quedan  ' , intentos , '  intentos')
    #vaciaba la variable para no pegar las respuestas 
    palabra_corregida = ''
    #sirve para volver a cargar con la nueva respuesta
    palabra_usuario = input('ingresa una palabra de 5 letras')
    # si la paplabra ingresada es incorreta por tener una cantidad de letras diferente a 5
    while len(palabra_usuario) != 5 :
        palabra_usuario = input('ingresa una palabra de 5 letras por favor') 
