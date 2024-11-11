#Argumentos, variables en funciones

#el asterisco antes de nombres indica que la función puede aceptar un n° variable de argumentos
#los argumentos se agruparán en una tupla llamada nombres
def listarNombres(*nombres):
    for nombre in nombres:#se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'José', 'Claudia', 'Rosa')
