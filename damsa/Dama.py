class Mesa:
	Tablero = [range (0,8) for i in range (8)]
	Letras = ["A","B","C","D","E","F","G","H"]
	
	#funciona
	def hayPiezasNegras(self):
		for i in range (len (self.Tablero)):
			for j in range (len (self.Tablero)):
				fichaux=self.getFicha(chr(ord("A")+i), j+1)
				if (fichaux.getTipo()=="N"):
					return True
		return False
	
	#funciona
	def hayPiezasBlancas(self):
		for i in range (len (self.Tablero)):
			for j in range (len (self.Tablero)):
				fichaux=self.getFicha(chr(ord("A")+i), j+1)
				if (fichaux.getTipo()=="B"):
					return True
		return False
			
	#funciona
	def vacia(self, letra, numero):
		if (self.getFicha(letra, numero).tipo==" "):
			return True
		else:
			return False
	
	#funciona
	def ponerFicha(self, fich, letra, number):
		fich.setPosicion(letra,number)
		self.Tablero[self.__buscarLetra(letra)][number-1] = fich
	
	#funciona
	def eliminarFicha(self, letra, number):
		fichaux=Ficha(" ", letra, number, self)
		self.ponerFicha(fichaux, letra, number)
	
	#funciona
	def getFicha(self, letra, number):
		return self.Tablero[self.__buscarLetra(letra)][number-1]
	
	#funciona
	def getColorFicha(self, letra, number):
		return self.getFicha(letra, number).getTipo()
	
	#funciona
	def moverFicha(self, ficha, letraFin, numeroFin):
		letraOrigen=ficha.getLetra()
		numeroOrigen=ficha.getNumero()
		#if (not(self.vacia(letraOrigen, numeroOrigen))and(self.vacia(letraFin, numeroFin))):
		#blancas las de arriba
		if ((letraFin=="H" and ficha.getTipo()=="B") or (letraFin=="A" and ficha.getTipo()=="N")):
			fichaDama=Dama(ficha.getTipo(), letraFin, numeroFin, self)
			self.ponerFicha(fichaDama, letraFin, numeroFin)
		else:
			self.ponerFicha(ficha, letraFin, numeroFin)
		self.eliminarFicha(letraOrigen, numeroOrigen)
			
	#funciona
	def rellenaTablero(self):
		for i in range (len (self.Tablero)):
			for j in range (len (self.Tablero)):
				#self.Tablero [i][j]= Ficha(" ", self.Letras[i], j+1, self)
				fichaux = Peon(" ", self.Letras[i], j+1, self)
				self.ponerFicha(fichaux, self.Letras[i], j+1)
		
		for i in range (3):
			m =i%2
			while (m<8):
				#self.Tablero [i][m]= Ficha("b", self.Letras[i], m+1, self)
				fichaux = Peon("b", self.Letras[i], m+1, self)
				self.ponerFicha(fichaux, self.Letras[i], m+1)
				m=m+2
		
		for i in range (5,8):
			m = i%2
			while (m<8):
				#self.Tablero [i][m]= Ficha("n", self.Letras[i], m+1, self)
				fichaux = Peon("n", self.Letras[i], m+1, self)
				self.ponerFicha(fichaux, self.Letras[i], m+1)
				m=m+2
				
	#funciona
	def __buscarLetra(self, elemento):
		for i in range(0,len(self.Letras)):
			if(self.Letras[i] == elemento):
				return i
		return False
		
	#funciona
	def imprimeTablero(self):
		for i in range (len (self.Tablero)):
			print self.Letras[i]+"|",
			for j in range (len (self.Tablero)):
				print self.Tablero[i][j].tipo,
			print "|"

		print "  ",
		for i in range (1,9):
			print i,
		print
	
	#funciona
	def esBorde(self, letra, numero):
		return (letra=="A" or letra=="H" or numero==1 or numero==8)
	
class Ficha:

	Letras = ["A","B","C","D","E","F","G","H"]
	
	tipo = " "
	letra = "Z"
	numero = 0
	
	#funciona
	def __init__(self, tip, let, num, tabla):
		self.tipo=tip
		self.letra=let
		self.numero=num
		self.tablero = tabla
	
	#funciona
	def __buscarLetra(self, elemento):
		for i in range(0,len(self.Letras)):
			if(self.Letras[i] == elemento):
				return i
		return False
	
	#funciona
	def vacia(self):
		return (self.tipo==" ")
	
	#funciona
	def fichaMismoColor(self, letra, numero):
		return str.upper(self.getTipo())==str.upper(self.tablero.getColorFicha(letra, numero))
	
	#funciona
	def fichaDistintoColor(self, letra, numero):
		return ((not (self.fichaMismoColor(letra, numero))) and (not self.tablero.getFicha(letra, numero).vacia()))
	
	#-----
	def setPosicion(self, letra, numero):
		self.letra=letra
		self.numero=numero
	
	#-----
	def getPosicion(self):
		return self.letra + str(self.numero) +self.tipo
	
	#funciona
	def getLetra(self):
		return self.letra
	
	#funciona
	def getNumero(self):
		return self.numero
	
	#fuciona
	def getTipo(self):
		return str.upper(self.tipo)
	
	#funciona
	def imprimeFicha(self):
		print (self.letra)
		print (self.numero)
		print (self.tipo)
	
	#funciona
	def posicionAnteriorAlMovimiento(self, letra, numero):
		#antes de realizar un potetico movimiento a la posicion indicada 
		#devolvemos la posicion siguiente a dicho movimiento
		#letra y numero tienen que ser letra entre [B,I] , numero entre [2,7]
		x=numero-self.getNumero()
		y=ord(letra)-ord(self.getLetra())
		x1=abs(x)-1
		x1=(x/abs(x))*x1
		y1=abs(y)-1
		y1=(y/abs(y))*y1
		return self.tablero.getFicha(chr(ord(self.getLetra())+y1), self.getNumero()+x1)

	#funciona	
	def posicionSiguienteAlMovimiento(self, letra, numero):
		#antes de realizar un potetico movimiento a la posicion indicada 
		#devolvemos la posicion siguiente a dicho movimiento
		#letra y numero tienen que ser letra entre [B,I] , numero entre [2,7]
		x=numero-self.getNumero()
		y=ord(letra)-ord(self.getLetra())
		x1=abs(x)+1
		x1=(x/abs(x))*x1
		y1=abs(y)+1
		y1=(y/abs(y))*y1 
		return self.tablero.getFicha(chr(ord(self.getLetra())+y1), self.getNumero()+x1)
	
	#funciona
	def esDiagonalDeRadio(self, letra, numero, radio):
		return (abs(ord(self.getLetra())-ord(letra))==abs(self.getNumero()-numero)==radio)

	#funciona	
	def puedeComerFicha(self):
		for i in range (8):
			for j in range (8):
				letraAux=chr(ord("A")+i)
				numeroAux=j+1
				if ((self.getNumero()!=numeroAux) and (self.getLetra()!=letraAux) and (self.fichaComible(letraAux, numeroAux))):
					return True
		return False
	
class Peon(Ficha):

	#funciona	
	def fichaComible(self, letra, numero):
		return ((not self.tablero.esBorde(letra, numero)) and self.fichaDistintoColor(letra, numero) and (not self.tablero.vacia(letra, numero)) and (self.esDiagonalDeRadio(letra, numero, 1)) and (self.posicionSiguienteAlMovimiento(letra, numero)).vacia())

	def casillaMovibleComiendo(self, letra, numero):
		return self.fichaComible(letra, numero)
		
	#funciona	
	def posicionMovible(self, letra, numero):
		return (self.fichaComible(letra, numero) or (self.tablero.vacia(letra, numero) and self.esDiagonalDeRadio(letra, numero, 1)))
	
	#funciona
	def moverACasilla(self, letra, numero):
		if self.posicionMovible(letra, numero):
			if self.fichaComible(letra, numero):
				self.tablero.eliminarFicha(letra, numero)
				self.tablero.moverFicha(self, self.posicionSiguienteAlMovimiento(letra, numero).getLetra(), self.posicionSiguienteAlMovimiento(letra, numero).getNumero())
				return True
			else:
				self.tablero.moverFicha(self, letra, numero)
				return False
		else:
			return False
		
class Dama(Ficha):

	#funciona
	def posicionMovible(self, letra, numero):
		if (self.tablero.esBorde(letra, numero) and not (self.tablero.vacia(letra, numero))):
			return False
		else:
			return self.casillaMovible(letra, numero)
	
	#funciona
	def fichaComible(self, letra, numero):
		if (self.tablero.esBorde(letra, numero)):
			return False
		else:
			return self.esDiagonal(letra, numero) and (not (self.tablero.vacia(letra, numero))) and self.fichaDistintoColor(letra, numero) and (not self.hayFichasEnMovimiento(letra, numero)) and self.posicionSiguienteAlMovimiento(letra, numero).vacia() and (not self.tablero.esBorde(letra, numero))
	
	#funciona
	def moverACasilla(self, letra, numero):
		#devuelve true si ha comido
		booleanoaux=False
		if self.casillaMovible(letra, numero):
			if not self.tablero.vacia(letra, numero):
				self.tablero.eliminarFicha(letra, numero)
				self.tablero.moverFicha(self, self.posicionSiguienteAlMovimiento(letra, numero).getLetra(), self.posicionSiguienteAlMovimiento(letra, numero).getNumero())
			else:
				aux=self.fichaMasCercanaEnMovimiento(letra, numero, True)
				if (not (aux==True or aux==False)):
					booleanoaux=True
					self.tablero.eliminarFicha(aux.getLetra(), aux.getNumero())
				if (not self.tablero.vacia(letra, numero)):
					self.tablero.moverFicha(self, self.posicionSiguienteAlMovimiento(letra, numero).getLetra(), self.posicionSiguienteAlMovimiento(letra, numero).getNumero())
				else:
					self.tablero.moverFicha(self, letra, numero)
			return booleanoaux
		return False
			
	#funciona		
	def casillaMovibleComiendo(self, letra, numero):
		return (self.fichaComible(letra, numero) or (self.esDiagonal(letra, numero) and (self.numeroFichasEnMovimiento(letra, numero, 0)==1) and self.fichaComible(self.fichaMasCercanaEnMovimiento(letra, numero, True).getLetra(), self.fichaMasCercanaEnMovimiento(letra, numero, True).getNumero())))
	
	#funciona
	def casillaMovible(self, letra, numero):
		return (self.casillaMovibleComiendo(letra, numero)or(self.esDiagonal(letra, numero) and (not self.hayFichasEnMovimiento(letra, numero)) and self.tablero.vacia(letra, numero)))
	
	#funciona
	def esDiagonal(self, letra, numero):
		radio = abs(self.getNumero()-numero)
		if (abs(ord(self.getLetra())-ord(letra))==radio):
			return True
		else:
			return False
	
	#funciona cuidado con el return false
	def hayFichasEnMovimiento(self, letra, numero):
		#comprueba si hay fichas entre la ficha actual y la casilla indicada sin contar la ficha actual ni la indicada
		if self.esDiagonalDeRadio(letra, numero, 1):
			return False
		elif (self.esDiagonal(letra, numero)):
			x=numero-self.getNumero()
			y=ord(letra)-ord(self.getLetra())
			x1=abs(x)-1
			x1=(x/abs(x))*x1
			y1=abs(y)-1
			y1=(y/abs(y))*y1
			return ((not self.tablero.vacia(chr(ord(self.getLetra())+y1), self.getNumero()+x1)) or self.hayFichasEnMovimiento(chr(ord(self.getLetra())+y1), self.getNumero()+x1))
		else:
			#lanzar exception
			return False
	
	#funciona cuidado con el return false
	def numeroFichasEnMovimiento(self, letra, numero, cantidad):
		#comprueba si hay fichas entre la ficha actual y la casilla indicada sin contar la ficha actual ni la indicada
		if self.esDiagonalDeRadio(letra, numero, 1):
			return cantidad
		elif self.esDiagonal(letra,numero):
			x=numero-self.getNumero()
			y=ord(letra)-ord(self.getLetra())
			x1=abs(x)-1
			x1=(x/abs(x))*x1
			y1=abs(y)-1
			y1=(y/abs(y))*y1
			if (not self.tablero.vacia(chr(ord(self.getLetra())+y1), self.getNumero()+x1)):
				cantidad=cantidad+1
			return (self.numeroFichasEnMovimiento(chr(ord(self.getLetra())+y1), self.getNumero()+x1, cantidad))
		else:
			#lanzar excepcion
			return False
			
	#funciona
	def fichaMasCercanaEnMovimiento(self, letra, numero, fichaAux):
		#Se llama con false si devuelve false es que no hay fichas entre ese movimiento sin contrar la ficha propia y la final
		#comprueba si hay fichas entre la ficha actual y la casilla indicada sin contar la ficha actual ni la indicada
		if self.esDiagonalDeRadio(letra, numero, 1):
			return fichaAux
		elif self.esDiagonal(letra,numero):
			x=numero-self.getNumero()
			y=ord(letra)-ord(self.getLetra())
			x1=abs(x)-1
			x1=(x/abs(x))*x1
			y1=abs(y)-1
			y1=(y/abs(y))*y1
			if (not self.tablero.vacia(chr(ord(self.getLetra())+y1), self.getNumero()+x1)):
				fichaAux = self.tablero.getFicha(chr(ord(self.getLetra())+y1), self.getNumero()+x1)
			return (self.fichaMasCercanaEnMovimiento(chr(ord(self.getLetra())+y1), self.getNumero()+x1, fichaAux))
		else:
			#lanzar excepcion
			return False

	
class InterfazJuego:
	
	#funciona
	def __init__(self):
		self.tabla=Mesa()
		self.tabla.rellenaTablero()
		self.turno=1
	
	#funciona
	def cambiarTurno(self):
		self.turno = ((self.turno)%2)+1
	
	#funciona
	def esLetra(self, letra):
		return ((ord(str.upper(letra))>=ord("A")) and (ord(str.upper(letra))<=ord("H")))

	#funciona
	def esDigito(self, digito):
		return ((ord(digito)>=ord("1"))and(ord(digito)<=ord("8")))
	
	#funciona
	def entradaValida(self, cadena):
		return ((len(cadena)==4) and (self.esLetra(cadena[0])) and ((self.esLetra(cadena[2]))) and (self.esDigito(cadena[1])) and ((self.esDigito(cadena[3]))))
	
	#funciona
	def letraOrigen(self, cadena):
		if self.entradaValida(cadena):
			return str.upper(cadena[0])
		else:
			return "Z"
	
	#funciona
	def letraFin(self, cadena):
		if self.entradaValida(cadena):
			return str.upper(cadena[2])
		else:
			return "Z"
	
	#funciona
	def numeroOrigen(self, cadena):
		if self.entradaValida(cadena):
			return int(cadena[1])
		else:
			return 0
	
	#funciona
	def numeroFin(self, cadena):
		if self.entradaValida(cadena):
			return int(cadena[3])
		else:
			return 0
	
	def mover_interfaz(self, movimiento):
		letra=self.letraOrigen(movimiento)
		numero=self.numeroOrigen(movimiento)
		noSeMueve=((movimiento[0]==movimiento[2])and(movimiento[1]==movimiento[3]))
		origenNoVacio= not self.tabla.getFicha(letra,numero).vacia()
		movible = (self.entradaValida(movimiento)and origenNoVacio and (not noSeMueve))
		if movible:
			movible = self.tabla.getFicha(letra, numero).posicionMovible(self.letraFin(movimiento),self.numeroFin(movimiento)) and (self.turno==1 and (self.tabla.getFicha(letra, numero).getTipo()=="B")or(self.turno==2 and self.tabla.getFicha(letra, numero).getTipo()=="N"))
		if (not movible):
			return "Entrada incorrecta vuelva a introducir un movimiento"+str(self.turno)
		else:
			if (not self.tabla.getFicha(letra, numero).casillaMovibleComiendo(self.letraFin(movimiento),self.numeroFin(movimiento))):
				self.cambiarTurno()
			self.tabla.getFicha(letra, numero).moverACasilla(self.letraFin(movimiento), self.numeroFin(movimiento))
			return str(self.turno)
		
	def mover(self):
		movimiento = raw_input()
		#print movimiento
		letra=self.letraOrigen(movimiento)
		numero=self.numeroOrigen(movimiento)
		noSeMueve=((movimiento[0]==movimiento[2])and(movimiento[1]==movimiento[3]))
		origenNoVacio= not self.tabla.getFicha(letra,numero).vacia()
		movible = (self.entradaValida(movimiento)and origenNoVacio and (not noSeMueve))
		
		if movible:
			movible = self.tabla.getFicha(letra, numero).posicionMovible(self.letraFin(movimiento),self.numeroFin(movimiento)) and (self.turno==1 and (self.tabla.getFicha(letra, numero).getTipo()=="B")or(self.turno==2 and self.tabla.getFicha(letra, numero).getTipo()=="N"))
		while (not movible):
			print "Entrada incorrecta vuelva a introducir un numero"
			movimiento=raw_input()
			letra=self.letraOrigen(movimiento)
			numero=self.numeroOrigen(movimiento)
			noSeMueve=((movimiento[0]==movimiento[2])and(movimiento[1]==movimiento[3]))
			origenNoVacio= not self.tabla.getFicha(letra,numero).vacia()
			movible = (self.entradaValida(movimiento)and origenNoVacio and (not noSeMueve))
			if movible:
				movible = self.tabla.getFicha(letra, numero).posicionMovible(self.letraFin(movimiento),self.numeroFin(movimiento)) and (self.turno==1 and (self.tabla.getFicha(letra, numero).getTipo()=="B")or(self.turno==2 and self.tabla.getFicha(letra, numero).getTipo()=="N"))
		
		if (not self.tabla.getFicha(letra, numero).casillaMovibleComiendo(self.letraFin(movimiento),self.numeroFin(movimiento))):
			self.cambiarTurno()
		self.tabla.getFicha(letra, numero).moverACasilla(self.letraFin(movimiento), self.numeroFin(movimiento))
	
	def jugar(self):
		while (self.tabla.hayPiezasNegras() and self.tabla.hayPiezasNegras()):
			self.tabla.imprimeTablero()
			print "Jugador", self.turno, "introduzca jugada: "
			self.mover()
		self.tabla.imprimeTablero()
		print "Juego finalizado, Ha ganado ", self.turno
		

#juego=InterfazJuego()
#juego.tabla.imprimeTablero()
'''
juego.tabla.eliminarFicha("B", 2)
juego.tabla.moverFicha(juego.tabla.getFicha("C", 1), "E", 3)
juego.tabla.moverFicha(juego.tabla.getFicha("H", 6), "A", 1)
juego.tabla.moverFicha(juego.tabla.getFicha("A", 1), "E", 5)


juego.tabla.imprimeTablero()
print juego.tabla.getFicha("E", 5).puedeComerFicha()
print juego.tabla.getFicha("F", 4).puedeComerFicha()
print juego.tabla.getFicha("F", 2).puedeComerFicha()
print juego.tabla.getFicha("F", 8).puedeComerFicha()
print juego.tabla.getFicha("B", 4).puedeComerFicha()
print juego.tabla.getFicha("C", 3).puedeComerFicha()
print juego.tabla.getFicha("E", 3).puedeComerFicha()
print juego.tabla.getFicha("B", 6).puedeComerFicha()
juego.tabla.getFicha("E", 5).moverACasilla("C", 3)
juego.tabla.imprimeTablero()
'''
#juego.jugar()