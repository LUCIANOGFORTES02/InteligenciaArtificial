import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template
from spade.message import Message 

class PotenciaAgent(Agent):
    class PotenciaBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting POTÊNCIA behaviour . . .")
          

        async def run(self):
            # Espere pela mensagem por 10 segundos
            msg = await self.receive(timeout=10)#Recebendo a mensagem
            print("Mensagem recebida do Coordenador")
            if msg:# Enviando de volta para o coordenador a resposta
                valores = msg.body.split(" ")
                resposta = pow(float(valores[0]) , float(valores[1]))
                msg = Message(to="agent1Coordenador@anoxinon.me")#agent1Coordenador@anoxinonme                         #coordenatoragent@anoxinon.me
                #msg.to=("agent1Coordenador@anoxinon.me")# jid do recptor da mensagem
                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")
                msg.body = str(resposta) 

                await self.send(msg)#Mensagem sendo enviada

                print(f"resposta enviada para o COORDENADOR  ({resposta})")
                await self.agent.stop()
            else:
                print("Mensagem n recebida do coordenador")

            
            

        #async def on_end(self):
        #   print("Behaviour finished with exit code {}.".format(self.exit_code))

    async def setup(self):
        print("Agent POTÊNCIA starting . . .")
        my_behav = self.PotenciaBehav()
        # Método usado pelo SPADE para despachar as mensagens recebidas para o comportamento que está 
        # aguardando aquela mensagem
        template = Template()
        template.set_metadata("performative", "inform")

        #Primeiro parametro é o comportamento que queremo adicionar o segundo é o modelo associado a esse comportamento
        self.add_behaviour(my_behav, template) 

if __name__ == "__main__":
    dummy = PotenciaAgent("agent5Potencia@anoxinon.me", "potencia")
    future = dummy.start()                                             
    future.result()  # Wait until the start method is finished
    
    


    # wait until user interrupts with ctrl+C
    while not dummy.my_behav.is_killed():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            dummy.stop()           
            break