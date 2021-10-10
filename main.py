def funcion(transiciones, cadena, caracteres_validos, edo):  # Recibimos parametros
    edo = validar(transiciones, cadena, edo, 0, caracteres_validos, 0, '-> '+edo)
    return edo  # Retornamos estado final


def validar(transiciones, cad, edo, index, caracteres_validos, i, rama):
    # print('Entrando en funcion')
    # i = 0 ' -> '
    if index < len(cad):  # Si el indice aun corresponde a la cadena dada procedemos
        print(f'\ni = {i}')
        print(f'index = {index}')
        # Si el caracter en seleccionado es parte de los caracteres validos procedemos
        if cad[index] in caracteres_validos:
            estados = []  # Lista que se retornará
            while i < len(transiciones):  # Recorremos las transiciones
                # Si se reconoce el estado se evalua la transicion
                if ((transiciones[i]))[0] == edo:
                    # Si la transicion es con epsilon transicionamos sin cambiar de caracter
                    if (transiciones[i])[1] == 'E':
                        print(f'Estado actual: {edo}')  # Imprimimos estado
                        print(f'Transicion con epsilon: {(transiciones[i])}')
                        ej = rama + ' -> ' + (transiciones[i])[2]
                        print(f'rama: {ej}')
                        estados.append(validar(transiciones, cad, (transiciones[i])[2], index, caracteres_validos, i+1, rama+' -> ' + (transiciones[i])[2]))
                    # Si no es  epsilon y el caracter en la transicion corresponde al evaluado de la cadena hacmos transicion al estado siguiente con el sig caracter
                    elif cad[index] == (transiciones[i])[1]: 
                        print(f'Estado actual: {edo}')  # Imprimimos estado
                        print(f'Transicion : {(transiciones[i])}')
                        ej = rama + ' -> ' + (transiciones[i])[2]
                        print(f'rama: {ej}\n')
                        estados.append(validar(transiciones, cad, (transiciones[i])[2], index+1, caracteres_validos, 0, rama+' -> ' + (transiciones[i])[2]))
                i += 1 # iteramos  a la siguiente transicion 
            return estados
        else:
            return validar(transiciones, cad, edo, index+1, caracteres_validos, 0, rama)
    else:
        return edo

def hay_estado():
    print('No sabemos')
    if 'si':
        return True
    else:
        return False
    
# leer arcchivo txt
entrada = input("Introduce el nombre del archivo a leer en la carpeta, sin espasios y con la extencion (Ejemplo: 1.txt): ")
f = open(entrada, 'r')

EstadosQ = []
Epsilon = []
EdoInicial = ''
EdosAceptacion = []
Sigma = []

# Metemos los estados a nuestra lista de esados
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        EstadosQ.append(caracter)

# Metemos los simbolos a nuestra lista de Epsilon
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        Epsilon.append(caracter)

# Metemos el estado de start a nuestra lista de Epsilon
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        EdoInicial = caracter

# Metemos los estados finales a nuestra lista de estadosFinales
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        EdosAceptacion.append(caracter)

# Sigue sigma UTF-8 = "\u03A3"

mensaje = f.readline() #Leemos linea del archivo txt
while(mensaje): # Si el resultado de intentar leer es exitoso, analizamos la linea de transicion 
    cadena_aux = '' #Si los estados/transiciones son de mas de un caracter aqui se acumularan 
    transicion = [] #Se adjuntará una lista con los datos de la transicion a la lista de transiciones Sigma
    x = 0 #Para leer cada transicion
    while x < len(mensaje): #Leemos cada transicion caracter por caracter
        if mensaje[x] != '\n' and mensaje[x] != ',': #Si el caracter es diferente que una coma o un salto de linea...
            cadena_aux = cadena_aux + mensaje[x] #... el caracter se añade a la cadena formada por los caracteres 
        elif mensaje[x] == '\n' or mensaje[x] == ',' or x == (len(mensaje) - 1): #Si es un salto de linea, coma o corchete de cierre...
            transicion.append(cadena_aux) #Se adjunta a la lista con los datos
            cadena_aux = '' # Se reinicia la cadena auxiliar 
        x +=  1  #Iteramos caracter
    if len(transicion) < 3: # Si el largo de la lista con los datos significa que nos falta uno; El ultimo
        transicion.append(cadena_aux) #Agregamos el ultimo dato
    Sigma.append(transicion) #Agregamos la transicion a la lista de transiciones Sigma
    mensaje = f.readline() #Leemos siguiente linea

f.close() # Cerramos el archivo

print(f'\u03A3: {Sigma}') #Mostramos transiciones 

Estado_final = funcion(Sigma, input("Introduzca cadena: "), Epsilon, EdoInicial) #Pedimos la cadena y Comenzamos el analisis de la cadena con el automata 
print(f'Estados finales:\n{Estado_final}') #Mostramos estados finales 
