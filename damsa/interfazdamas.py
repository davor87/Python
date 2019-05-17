#!/usr/bin/python
import pygtk
import gtk
import gtk.glade
import Dama

class main:

	def __init__(self):
		#define la cantidad de movimientos maximos para desahacer
		self.buffer_deshacer=10
		self.posiblesdeshacer=0
		self.posiblesrehacer=0
		
		self.buffer=range(self.buffer_deshacer)
		self.indice_buffer_circular=0
	# Crea la ventana de trabajo Principal y obtiene los objetos en Glade
		self.builder = gtk.Builder()
		self.builder.add_from_file("damas2.glade")
		#self.widgets = gtk.glade.XML("damas2.glade")
		signals = { "mover" : self.mover,
					"abrir" : self.abrir,
					"nuevo" : self.nuevo,
					"guardar": self.guardar,
					"undo"	: self.undo,
					"redo"	: self.redo,
					"gtk_main_quit" : gtk.main_quit }
		self.builder.connect_signals(signals)
		self.botones = range(64)
		for i in range(64):
			nombre_imagen = "image"+str(i+1)
			self.botones[i]=self.builder.get_object(nombre_imagen)
			#print gtk.Buildable.get_name(self.botones[i])
		self.entrada = self.builder.get_object("entry1")
		self.label = self.builder.get_object("label1")
		self.juego=Dama.InterfazJuego()
		self.juego.tabla.imprimeTablero()
		self.mostrar();
	
	def mostrar(self):
		k=0
		for i in range (8):
			for j in range (8):
				#print self.juego.tabla.getColorFicha(chr(ord("A")+i).upper(), j+1)
				#print k
				ficha = self.juego.tabla.getFicha(chr(ord("A")+i).upper(), j+1).tipo
				if (ficha=="n"):
					self.botones[k].set_from_file("damanegra.jpg")
				elif (ficha=="N"):
					self.botones[k].set_from_file("reinanegra.jpg")
				elif (ficha=="b"):
					self.botones[k].set_from_file("damablanca.jpg")
				elif (ficha=="B"):
					self.botones[k].set_from_file("reinablanca.jpg")
				elif (((i+j)%2)==0):
					self.botones[k].set_from_file("negro.jpg")
				else:
					self.botones[k].set_from_file("blanco.jpeg")
				self.botones[k].show
				k=k+1
	
	def mover(self, widget):
		texto_entrada = self.entrada.get_text()
		self.label.set_text(self.juego.mover_interfaz(texto_entrada));
		self.juego.tabla.imprimeTablero()
		self.mostrar()
		self.entrada.set_text("")
		#print gtk.Buildable.get_name(widget)
		
	def abrir(self, widget):
		print "abrir"
	
	def nuevo(self, widget):
		print "nuevo"
	
	def guardar(self, widget):
		print "guardar"
		
	def undo(self, widget):
		print "undo"
		
	def redo(self, widget):
		print "redo"
		
#Ejecucion del programa
if __name__ == "__main__":
	main()
	gtk.main()