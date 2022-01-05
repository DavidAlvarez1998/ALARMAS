from datetime import datetime
import pygame
import time
import threading



def repro():
	archivo = open("./song.mp3", "r")
	pygame.mixer.init()
	sonido = pygame.mixer.Sound(archivo)
	pygame.mixer.Sound.play(sonido)
	time.sleep(1)
	pygame.mixer.Sound.stop(sonido)
	archivo.close()


def reloj():
	while True:
		now = datetime.now()
		hora=now.hour
		minuto=now.minute
		segundo=now.second
		print(str(hora)+":"+str(minuto)+":"+str(segundo))
		time.sleep(1)

def m1():
        while True:
                now = datetime.now()
                segundo=now.second
                if segundo==0:
                        print("M1")
                        repro()
                time.sleep(1)
		
def m5():
	while True:
		now = datetime.now()
		minuto=now.minute
		if minuto%5==0:
			print("M5")
			repro()
			time.sleep(60)
		time.sleep(1)
		
def m15():	
	while True:
		now = datetime.now()
		minuto=now.minute
		if minuto%15==0:
			print("M15")
			repro()
			time.sleep(60)
		time.sleep(1)

def h1():	
	while True:
		now = datetime.now()
		hora=now.hour
		if hora%1==0:
			print("H1")
			repro()
			time.sleep(60*59)
		time.sleep(1)

def h4():	
	while True:
		now = datetime.now()
		hora=now.hour
		if hora%4==0:
			print("H4")
			repro()
			time.sleep(4*60*59)
		time.sleep(1)

def menu():
	#  1=M1  2=M5  3=M15  4=H1  5=H4
	while True:

		print("OPCIONES:\n1) M1\n2) M5\n3) M15\n4) H1\n5) H4")
		opcion=str(input("Seleccione una opcion: "))
		hilo = threading.Thread(target=reloj)
		hilo.start()
		
		if opcion=="1":
			hilo1 = threading.Thread(target=m1)
			hilo1.start()
		elif opcion=="2":
			hilo2 = threading.Thread(target=m5)
			hilo2.start()
		elif opcion=="3":
			hilo3 = threading.Thread(target=m15)
			hilo3.start()
		elif opcion=="4":
			hilo4 = threading.Thread(target=h1)
			hilo4.start()
		elif opcion=="5":
			hilo5 = threading.Thread(target=h4)
			hilo5.start()

if __name__ == '__main__':
	repro()
	menu()



'''
#Día actual
today = date.today()
#Fecha actual
now = datetime.now()
print(today)
print(now)
#Date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))
#Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))
print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))
'''
