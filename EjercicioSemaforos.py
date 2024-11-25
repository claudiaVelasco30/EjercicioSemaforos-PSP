import threading
import time
import random

def accederEstacionamiento(idVehiculo):
    print(f"Vehículo {idVehiculo} intentando entrar al estacionamiento.")
    semaforo.acquire() #Adquirimos el semáforo para entrar al estacionamiento
    print(f"Vehículo {idVehiculo} ha entrado al estacionamiento.")
    time.sleep(random.uniform(1, 3)) #Simulamos tiempo en el estacionamientos
    print(f"Vehículo {idVehiculo} ha salido del estacionamiento.")
    semaforo.release() #Liberamos el semáforo para permitir que otro entre

#Creamos un semáforo con capacidad de 3
semaforo = threading.Semaphore(3)

#Creamos e iniciamos 10 hilos
vehiculos = []

for i in range(10):
    t = threading.Thread(target=accederEstacionamiento, args=(i,))
    vehiculos.append(t)
    t.start()

#Esperamos a que todos los hilos terminen
for t in vehiculos:
    t.join()

print("Todos los vehículos han pasado por el estacionamiento.")