from time import time
import matplotlib.pyplot as plt

def graficar(titulo, x, y, titEjeX, titEjeY, leyenda):
	plt.plot(x, y, color='cyan', linewidth = 2, marker='*', markerfacecolor='red', markersize=20)
	plt.title(titulo)
	plt.xlabel(titEjeX)
	plt.ylabel(titEjeY)
	plt.legend( leyenda, loc = 'upper left')
	plt.grid(True)
	plt.show()

def crearTablero(llave):
	tablero = []
	llaveAux = llave.replace(" ", "")
	#Se definen las letras exceptuando la j
	letras = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#NSe limpia la llave
	llaveLimpia = []
	for letra in llaveAux:
		if not letra in llaveLimpia:
			llaveLimpia.append(letra)
    #Se ingresan las demas letras
	for letra in letras:
        #Para que si el usuario ingresa una conbinacvion de mayusculas y minusculas, no afecte en la generacion del tablero
		if not letra in llaveLimpia and not letra.upper() in llaveLimpia:
			llaveLimpia.append(letra)
    #Se pasa a mayuscula
	for i in range(len(llaveLimpia)):
		llaveLimpia[i] = llaveLimpia[i].upper()
    #Se ingresan las letras en orden al tablero de 5x5
	while llaveLimpia != []:
		tablero.append(llaveLimpia[:5])
		llaveLimpia = llaveLimpia[5:]
	return tablero

def buscarLetra(letra,tablero):
	f = 0 #para las filas
	c = 0 #para las columnas
	posicion = []
	while(f < 5):
		while(c < 5):
			if letra == tablero[f][c]:
				posicion.append(f)
				posicion.append(c)
			c = c + 1
		c = 0
		f = f + 1
	return posicion


def encriptar(texto, tablero):
	#Se limpia el texto
	aux = 0
	mensajeLimpio1 = ""
	while(aux < len(texto)):
		mensajeLimpio1 = mensajeLimpio1 + texto[aux]
		#Se acabo el texto
		if aux == (len(texto) - 1):
			break
		#Caso en que hay 2 letars iguales juntas
		elif texto[aux] == texto[aux+1]:
			#Se le agrega la x
			mensajeLimpio1 = mensajeLimpio1 + "x"
		aux = aux + 1
	#Se eliminan los espacios y se arma
	mensajeLimpio2 = mensajeLimpio1.replace(" ", "")
	#Se separan las letras en pares
	mensajeLimpioFinal = [mensajeLimpio2[i:i+2] for i in range(0, len(mensajeLimpio2), 2)]
	for par in mensajeLimpioFinal:
		#Se remplaza la j por i
		if ("j" in par):
			mensajeLimpioFinal = [par.replace('j', 'i') for par in mensajeLimpioFinal]
		if len(par) < 2:
			anterior = par
			actual = par + "x"
			mensajeLimpioFinal = [par.replace(anterior,actual) for par in mensajeLimpioFinal]
	#Se pasan a mayusculas
	for i in range(len(mensajeLimpioFinal)):
		mensajeLimpioFinal[i] = mensajeLimpioFinal[i].upper()

	textoEncriptado = ""
	for par in mensajeLimpioFinal:
		posicion = []
		#Se obtiene la ubicacion de cada letra en el tablero
		for letra in par:
			#Se agrega a la lista de posiciones, esto con el objetivo de tener referencia para los posteriores movimientos dadas las condiciones del cifrado
			posicion.append(buscarLetra(letra,tablero))
		#La condicion dice que si el par esta en la misma fila, el resultado seran una posicion a la derecha en el teblero
		if posicion[0][0] == posicion[1][0]:
			posicion[0][1] = posicion[0][1] + 1
			posicion[1][1] = posicion[1][1] + 1
			fila1 = posicion[0][0]
			columna1 = posicion[0][1]
			fila2 = posicion[1][0]
			columna2 = posicion[1][1]
			#Si esta al borde de abajo
			if fila1 == 5:
				#Pasa a la primera fila
				fila1 = 0
			#Si esta al borde derecho
			elif columna1 == 5:
				#Pasa a la primera columna
				columna1 = 0
			#Si esta al borde de abajo
			elif fila2 == 5:
				#Pasa a la primera fila
				fila2 = 0
			#Si esta al borde derecho
			elif columna2 == 5:
				#Pasa a la primera columna
				columna2 = 0
			textoEncriptado = textoEncriptado + tablero[fila1][columna1]
			textoEncriptado = textoEncriptado + tablero[fila2][columna2]
			
		#La condicion dice que si el par esta en la misma columna, el resultado sera una posicion hacia abajo
		if posicion[0][1] == posicion[1][1]:
			posicion[0][0] = posicion[0][0] + 1 
			posicion[1][0] = posicion[1][0] + 1
			fila1 = posicion[0][0]
			columna1 = posicion[0][1]
			fila2 = posicion[1][0]
			columna2 = posicion[1][1]
			#Si esta al borde de abajo
			if fila1 == 5:
				#Pasa a la primera fila
				fila1 = 0
			#Si esta al borde derecho
			elif columna1 == 5:
				#Pasa a la primera columna
				columna1 = 0
			#Si esta al borde de abajo
			elif fila2 == 5:
				#Pasa a la primera fila
				fila2 = 0
			#Si esta al borde derecho
			elif columna2 == 5:
				#Pasa a la primera columna
				columna2 = 0
			textoEncriptado = textoEncriptado + tablero[fila1][columna1]
			textoEncriptado = textoEncriptado + tablero[fila2][columna2]

		#La condicion dice que si el par esta en diferente fila y columna a la vez, se forma un cuadrado tomando estas posciiones como esquinas, y las otras 2 esquinas del cuadrado seran las nuevas 
		#posiciones
		if (posicion[0][0] != posicion[1][0]) and (posicion[0][1] != posicion[1][1]):
			aux = posicion[0][1]
			posicion[0][1] = posicion[1][1] 
			posicion[1][1] = aux
			fila1 = posicion[0][0]
			columna1 = posicion[0][1]
			fila2 = posicion[1][0]
			columna2 = posicion[1][1]
			textoEncriptado = textoEncriptado + tablero[fila1][columna1]
			textoEncriptado = textoEncriptado + tablero[fila2][columna2]
	return textoEncriptado


def desencriptar(texto, tablero):
	pares = [texto[i:i+2] for i in range(0, len(texto), 2)]
	textoOriginal = ""
	for par in pares:
		posicion = []
		#Se obtiene la ubicacion de cada letra en el tablero
		for letra in par:
			#Se agrega a la lista de posiciones, esto con el objetivo de tener referencia para los posteriores movimientos dadas las condiciones del cifrado
			posicion.append(buscarLetra(letra,tablero))

		#La condicion dice que si el par esta en la misma fila, el resultado seran una posicion a la izquierda en el teblero
		if posicion[0][0] == posicion[1][0]:
			#En este caso, se retrocede una posicion
			posicion[0][1] = posicion[0][1] - 1
			posicion[1][1] = posicion[1][1] - 1
			fila1 = posicion[0][0]
			columna1 = posicion[0][1]
			fila2 = posicion[1][0]
			columna2 = posicion[1][1]
			#Si esta al borde de abajo
			if fila1 == 5:
				#Pasa a la primera fila
				fila1 = 0
			#Si esta al borde derecho
			elif columna1 == 5:
				#Pasa a la primera columna
				columna1 = 0
			#Si esta al borde de abajo
			elif fila2 == 5:
				#Pasa a la primera fila
				fila2 = 0
			#Si esta al borde derecho
			elif columna2 == 5:
				#Pasa a la primera columna
				columna2 = 0
			textoOriginal = textoOriginal + tablero[fila1][columna1]
			textoOriginal = textoOriginal + tablero[fila2][columna2]
			
		#La condicion dice que si el par esta en la misma columna, el resultado sera una posicion hacia arriba
		if posicion[0][1] == posicion[1][1]:
			#En este caso, se retrocede una posicion hacia arriba
			posicion[0][0] = posicion[0][0] - 1 
			posicion[1][0] = posicion[1][0] - 1
			fila1 = posicion[0][0]
			columna1 = posicion[0][1]
			fila2 = posicion[1][0]
			columna2 = posicion[1][1]
			#Si esta al borde de abajo
			if fila1 == 5:
				#Pasa a la primera fila
				fila1 = 0
			#Si esta al borde derecho
			elif columna1 == 5:
				#Pasa a la primera columna
				columna1 = 0
			#Si esta al borde de abajo
			elif fila2 == 5:
				#Pasa a la primera fila
				fila2 = 0
			#Si esta al borde derecho
			elif columna2 == 5:
				#Pasa a la primera columna
				columna2 = 0
			textoOriginal = textoOriginal + tablero[fila1][columna1]
			textoOriginal = textoOriginal + tablero[fila2][columna2]

		#La condicion dice que si el par esta en diferente fila y columna a la vez, se forma un cuadrado tomando estas posciiones como esquinas, y las otras 2 esquinas del cuadrado seran las nuevas 
		#posiciones
		if (posicion[0][0] != posicion[1][0]) and (posicion[0][1] != posicion[1][1]):
			aux = posicion[0][1]
			#En este caso, es las esquinas del mensaje original
			posicion[0][1] = posicion[1][1] 
			posicion[1][1] = aux
			fila1 = posicion[0][0]
			columna1 = posicion[0][1]
			fila2 = posicion[1][0]
			columna2 = posicion[1][1]
			textoOriginal = textoOriginal + tablero[fila1][columna1]
			textoOriginal = textoOriginal + tablero[fila2][columna2]
	return textoOriginal


def testAvalancha(texto1, texto2, llave):
	mensaje1 = texto1
	a = ' '.join(format(x, 'b') for x in bytearray(mensaje1, 'utf-8'))
	mensaje2 = texto2
	b = ' '.join(format(x, 'b') for x in bytearray(mensaje2, 'utf-8'))
	#Se encripta la primera palabra
	# Se crea el tablero para ambos encriptados
	tablero = crearTablero(llave) 
	# Se encripta la segunda palabra
	mensaje1Encriptado = encriptar(mensaje1,tablero)
	#Se genera la salida en bits
	bits1 = ' '.join(format(x, 'b') for x in bytearray(mensaje1, 'utf-8'))
	print("Ambas palabras fueron encriptadas con la misma llave: " + llave)
	print("La encriptacion de la palabra: "+mensaje1+" resultado en: "+mensaje1Encriptado+", con la siguiente representacion en bits: "+bits1)
	#Se encripta la segunda palabra
	mensaje2Encriptado = encriptar(mensaje2,tablero)
	#Se genera la salida en bits
	bits2 = ' '.join(format(x, 'b') for x in bytearray(mensaje2, 'utf-8'))
	print("La encriptacion de la palabra: "+mensaje2+" resultado en: "+mensaje2Encriptado+", con la siguiente representacion en bits: "+bits2)

#Menu 
def menu():
	tamañoBloque = 0.003
	bandera = True
	while bandera:
		print("Bienvenido al cifrador Playfair")
		print("Primero, es necesario que ingrese la llave tanto para cifrar como para descifrar (solo letras)")
		print("Considere que la llave puede ser tanto en mayusculas como en minusculas")
		llave = input("Ingrese la llave para el cifrador Playfair: ")
		print("Seleccione la accion que desea realizar: ")
		print("1 para Encriptar")
		print("2 para Desencriptar")
		print("0 para Salir")
		opcion = input("Ingrese su opción: ")
		
		tablero = crearTablero(llave)
		#Encriptado
		if int(opcion) == 1:
			texto = input("Ingrese el texto que desea encriptar: ")
			inicio = time()
			textoEncriptado = encriptar(texto,tablero)
			print("Para el texto " + texto)
			print("Y la llave " + llave)
			print("Este es el texto encriptado:" + textoEncriptado)
			final = time()
			tiempoEncriptado = final - inicio
			print("Con tiempo de encriptado de: " + str(tiempoEncriptado) + " segundos")
			throughput1 = tamañoBloque / tiempoEncriptado
			throughput2 = (tamañoBloque*1.5) / tiempoEncriptado
			throughput3 = (tamañoBloque*2) / tiempoEncriptado
			#Grafico
			x = [tamañoBloque, tamañoBloque*1.5, tamañoBloque*2] 
			y = [throughput1, throughput2, throughput3]
			nombres = ["Encriptado"]
			graficar("Throughputs vs tamaño del bloque(Encriptado)", x, y, "Tamaño del bloque", "Throughput", nombres)
			bandera = False
		#Desencriptado
		if int(opcion) == 2:
			texto = input("Ingrese el texto que desea desencriptar: ")
			inicio = time()
			textoOriginal = desencriptar(texto,tablero)
			print("Para el texto " + texto)
			print("Y la llave " + llave)
			print("Este es el texto desencriptado:" + textoOriginal)
			final = time()
			tiempoDesencriptado = final - inicio
			print("Con tiempo de desencriptado de: " + str(tiempoDesencriptado) + " segundos")
			throughput1 = tamañoBloque / tiempoDesencriptado
			throughput2 = (tamañoBloque*1.5) / tiempoDesencriptado
			throughput3 = (tamañoBloque*2) / tiempoDesencriptado
			#Grafico
			x = [tamañoBloque, tamañoBloque*1.5, tamañoBloque*2] 
			y = [throughput1, throughput2, throughput3]
			nombres = ["Desencriptado"]
			graficar("Throughputs vs tamaño del bloque(Desencriptado)", x, y, "Tamaño del bloque", "Throughput", nombres)
			bandera = False
		#Salir
		if int(opcion) == 0:
			print("Ejecución finalizada")
			bandera = False

menu()

#testAvalancha("playstation","pleystation", "secret")