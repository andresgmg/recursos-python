import datetime
import time
import os

print('Reloj hecho con python')
print('')
while(True):
	os.system('cls')  # Limpiamos la pantalla
	print('Reloj hecho con python')
	print('')
	dt = datetime.datetime.now()
	print( "{}:{}:{}".format( dt.hour, dt.minute, dt.second ) )
	print('')
	print("para salir presiona Ctrl + C")
	time.sleep(1)  # Esperar 1 segundo