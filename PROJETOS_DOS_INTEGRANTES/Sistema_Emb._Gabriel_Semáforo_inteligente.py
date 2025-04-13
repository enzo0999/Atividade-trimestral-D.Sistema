import time

def mostrar_semaforo(cor):
    print(f"----------------")
    print(f"Vermelho  : {'🔴' if cor == 'Vermelho' else '⚫'}")
    print(f"Amarelo   : {'🟡' if cor == 'Amarelo' else '⚫'}")
    print(f"Verde     : {'🟢' if cor == 'Verde' else '⚫'}")
    print(f"----------------")

def semaforo():
    while True:
        mostrar_semaforo('Verde')
        time.sleep(5)

        mostrar_semaforo('Amarelo')
        time.sleep(2)

        mostrar_semaforo('Vermelho')
        time.sleep(5)

semaforo()
