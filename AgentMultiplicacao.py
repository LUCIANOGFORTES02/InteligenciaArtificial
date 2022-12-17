import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template
from spade.message import Message 

class MultiplicacaoAgent(Agent):
    class MultiplicacaoBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0

        async def run(self):
            # Espere pela mensagem por 10 segundos
            msg = await self.receive(timeout=10)#Recebendo a mensagem

            if msg:# Enviando de volta para o coordenador a resposta
                valores = msg.body.split(" ")
                resposta = valores[0] * valores[1]
                msg = Message() 
                msg.to=("agent1Coordenador@anoxinon.me")# jid do recptor da mensagem
                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")
                msg.body = str(resposta) 

                await self.send(msg)#Mensagem sendo enviada

                print(f"resposta send! ({resposta})")
                await self.agent.stop()
            else:
                print("Mensagem n    recebida")

            # stop agent from behaviour
            
            

        async def on_end(self):
            print("Behaviour finished with exit code {}.".format(self.exit_code))

    async def setup(self):
        print("Agent starting . . .")
        self.my_behav = self.MultiplicacaoBehav()
        # Método usado pelo SPADE para despachar as mensagens recebidas para o comportamento que está 
        # aguardando aquela mensagem
        template = Template()
        template.set_metadata("performative", "inform")

        #Primeiro parametro é o comportamento que queremo adicionar o segundo é o modelo associado a esse comportamento
        self.add_behaviour(self.my_behav, template) 

if __name__ == "__main__":
    dummy = MultiplicacaoAgent("multiplyagent@anoxinon.me", "multiply")#"multiplyagent@anoxinon.me", "multiply")
    future = dummy.start()
    future.result()  # Wait until the start method is finished
    dummy.web.start(hostname="127.0.0.1", port="10000")


    # wait until user interrupts with ctrl+C
    while not dummy.my_behav.is_killed():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    dummy.stop()

"""import time

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template

from makeMessage import makeMessage


class MultiplyAgent(Agent):
    class MultiplyBehav(CyclicBehaviour):
        def generateresposta(self, n1, n2):
            return float(n1) * float(n2)

        async def run(self):
            print("MultiplyBehav running")

            # wait for a message for 10 seconds
            msg = await self.receive(timeout=10)
            if msg:
                valores = msg.body.split(" ")
                resposta = self.generateresposta(valores[0], valores[1])
                msgSend = makeMessage("coordenatoragent@anoxinon.me", resposta)

                await self.send(msgSend)

                print(f"resposta send! ({resposta})")
                await self.agent.stop()
            else:
                print("Did not received any message after 10 seconds")

            # stop agent from behaviour

    async def setup(self):
        print("ReceiverAgent started")
        multiplyBehav = self.MultiplyBehav()

        template = Template()
        template.set_metadata("performative", "inform")

        self.add_behaviour(multiplyBehav, template)


if __name__ == "__main__":
    receiveragent = MultiplyAgent("multiplyagent@anoxinon.me", "multiply")
    future = receiveragent.start()
    future.resposta()

    receiveragent.web.start(hostname="127.0.0.1", port="10000")

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            receiveragent.stop()
            break

    print("Agents finished")"""