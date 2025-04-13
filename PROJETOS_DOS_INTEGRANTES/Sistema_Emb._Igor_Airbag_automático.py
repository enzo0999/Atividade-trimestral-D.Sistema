import random
import time

def sensor_de_impacto():
    return random.choice(["nenhum impacto detectado", "air bag acionado!"])

def detectando_velocidade(velocidade_maxima):
    return random.randint(0, velocidade_maxima)

def gerenciar_airbag(velocidade_atual):
    if velocidade_atual > 50: 
        print("-------------------------")
        estado_sensor = sensor_de_impacto()
        if estado_sensor == "air bag acionado!":
            print("Impacto dectado! Air bag acionado")
        else:
            print("Nenhum impacto detectado")
        print("-----------------------")
    else:
        print(f"Velocidade baixa ({velocidade_atual} km/h) - Air bag não acionado.")
        print("-------------------------")

def airbag():
    while True:
        velocidade_atual = detectando_velocidade(120)
        print(f"Velocidade atual: {velocidade_atual} km/h")
        gerenciar_airbag(velocidade_atual)  
        time.sleep(5) 

airbag()





