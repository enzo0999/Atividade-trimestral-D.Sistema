import random
import time

class SistemaAirbag:
    def _init_(self):
        self.limiar_impacto = 50  
        self.tempo_resposta = 0.3 
        self.airbag_acionado = False
    
    def detectar_impacto(self):
        aceleracao = random.randint(0, 100)
        print(f"Aceleração detectada: {aceleracao} m/s²")
        return aceleracao >= self.limiar_impacto
    
    def acionar_airbag(self):
        self.airbag_acionado = True
        print("Airbag acionado!")
    
    def simular_tempo_resposta(self):
        print(f"Aguardando {self.tempo_resposta} segundos para acionar o airbag...")
        time.sleep(self.tempo_resposta)
    
    def sistema(self, ciclos=10):
        print("Iniciando sistema de detecção de impacto...")
        for _ in range(ciclos):
            if self.airbag_acionado:
                print("Airbag já foi acionado. Encerrando simulação.")
                break

            impacto = self.detectar_impacto()
            if impacto:
                self.simular_tempo_resposta()
                self.acionar_airbag()
            else:
                print("Sem impacto detectado.\n")
            time.sleep(1)

sistema_airbag = SistemaAirbag()
sistema_airbag.sistema()