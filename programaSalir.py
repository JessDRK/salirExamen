import os
class Persona():
	def __init__(self):
		self.nombre=input("Nombre: ")
		self.apellido=input("Apellido: ")
		self.edad=input("Edad: ")
"""
Profe, no estaba seguro de si podría poner la clase persona con solo esta función, 
pero es que de verdad necesitaba el objeto "Persona" y esto es todo lo que quería,
no estoy seguro si había otra manera
"""

class Salida():
	grupo = []
	person = Persona
	lugar = int
	vehicu = int
	prom = int
	prom1 = int
	tiempo = float
	
	def mostrar(self):
		self.tiempo=self.prom*self.prom1
		x = 0 #No me gustaba inicializar tantas variables en 0 o 1, ¿Hay alguna otra forma?
		if self.lugar==1:
			lugar_s="a la playa"
		elif self.lugar==2:
			lugar_s="al cetro comercial"
		elif self.lugar==3:
			lugar_s="al parque de diversiones"	
		elif self.lugar==4:
			lugar_s="al cine"
		if self.vehicu==1:
			vehicu_s="en carro"
		elif self.vehicu==2:
			vehicu_s="en autobus"
		elif self.vehicu==3:
			vehicu_s="en moto"
		print("La persona o el grupo de: ")
		print()
		for i in self.grupo:
			x = 1 + x
		for i in range(x):
			print(self.grupo[i].nombre, self.grupo[i].apellido,"de",self.grupo[i].edad,"años")
		print()
		print("Va/n", lugar_s, vehicu_s)
		print("Tiempo promedio:",self.tiempo,"min")
		print()	
	def Grupo(self):
		x = 1
		while x==1: 
			self.grupo.append(self.person())
			x = 0
			while x<1 or x>2:
				x = int(input("¿Agregar a otra persona al grupo? 1 = si, 2 = no: "))
				os.system('cls')
				if x<1 or x>2:
					print("Opción no válida")
		
	def Grupo_modi(self):
		x = 0
		opc = 0
		for i in self.grupo:
			x = 1 + x
		for i in range(x):
			print(i+1,".-",self.grupo[i].nombre, self.grupo[i].apellido,"de",self.grupo[i].edad,"años")		
		while opc<1 or opc>3:
			print("1: Modificar algun dato")
			print("2: Añadir persona/s")
			print("3: Eliminar un usuario")
			opc = int(input())	
			if opc ==1:
				print("¿De qué persona desea modificar algún dato?")
				i=-1
				while(i<1 or i>x):
					i = int(input())
					if i<1 or i>x:
						print("Posición de la lista no válido")
				i = i-1
				print("¿Que desea modificar")
				opc = 0
				while opc<1 or opc>3: 
					print("1: Nombre")
					print("2: Apellido")
					print("3: Edad")
					opc=int(input())
					if opc==1:
						self.grupo[i].nombre=input()
					elif opc==2:
						self.grupo[i].apellido=input()
					elif opc==3:
						self.grupo[i].edad=input()
					elif opc<1 or opc>3:
						print("Opción no válida")
			elif opc==2:
				os.system('cls')
				self.Grupo(self)
			elif opc==3: 
				i=-1
				print("¿Cual desea eliminar?")
				while(i<1 or i>x):
					i = int(input())
				self.grupo.pop(i-1)
	def Lugar(self):
		self.lugar=0
		
		while(self.lugar<1 or self.lugar>4):
			print("¿A dónde desean ir?")
			print("1: Playa")
			print("2: Centro Comercial")
			print("3: Parque de diversiones")
			print("4: Cine")
			self.lugar = int(input())
			if self.lugar==1: 
				self.prom1=40
			elif self.lugar==2: 
				self.prom1=50
			elif self.lugar==3:
				self.prom1=60 
			elif self.lugar==4:
				self.prom1=60 
			if self.lugar<1 or self.lugar>4:
					print("Opción no válida")
	def Vehiculo(self):
		self.vehicu=0
		while(self.vehicu<1 or self.vehicu>3):
			print("¿En que van?")
			print("1: Carro")
			print("2: Autobus")
			print("3: Moto")
			self.vehicu=int(input())
			if (self.vehicu==1):
				self.prom=0.7
			elif (self.vehicu==2):
				self.prom= 1
			elif (self.vehicu==3):
				self.prom= 0.5
			if self.vehicu<1 or self.vehicu>2:
					print("Opción no válida")
			#Trabajar con tantos if es un poco confuso, no sé si era mejor usar diccionarios
			
		

#El orden del programa como tal
salir = Salida
print("Ingrese los datos de las personas pertenecientes al grupo")
print()
salir.Grupo(salir)
os.system('cls')
salir.Lugar(salir)
os.system('cls')
salir.Vehiculo(salir)
os.system('cls')

opc=1
print()
while opc!=4:
	os.system('cls')
	salir.mostrar(salir)
	print("¿Desea modificar algo?")
	print("1: Grupo")
	print("2: Lugar")
	print("3: Vehiculo")
	print("4: Ver lista final y salir")
	opc = int(input())
	if opc==1:
		salir.Grupo_modi(salir)
	elif opc==2:
		salir.Lugar(salir)
	elif opc==3:
		salir.Vehiculo(salir)
	elif opc==4:
		os.system('cls')
		salir.mostrar(salir)
#Sé que está algo corto, pero creo que esto es lo esencial
