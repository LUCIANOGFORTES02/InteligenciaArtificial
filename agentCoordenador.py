import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from VerificandoExpressao import dividindoExpressao,OrdemOperacoes
from AgentAdicao import AdicaoAgent
from AgentSub import SubAgent
from spade.message import Message 
from AgentMultiplicacao import MultiplicacaoAgent

class CoordenadorAgent(Agent):
    class  CoordenadorBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
        
        #É o metodo no qual o nucleo da programação é feito porque            
        #esse método é chamado a cada interação do loop de comportamento 
        async def run(self):  
            print ("Digite a expressao")
            #expressao = "23 + 12 - 55 + ( 2 + 4 ) - 8 / 2 ^ 2"
            expressao=str(input ())

            valor= dividindoExpressao(expressao)
            
            #Qual agente será chamado
            while (len(valor)>1):
                operadores =  OrdemOperacoes(valor)#Retorna um dicionario
                valores = f"{operadores['valor1']} {operadores['valor2']}"
                """
                receiveragent = None
                if operadores["Op"] == "-":
                    receiveragent = SubAgent(" ", "minus")#jid , senha
                elif operadores["Op"] == "+":
                    receiveragent = AdicaoAgent(" ", " ")
                
                elif operadores["Op"]== "*":
                    receiveragent = MultiplicacaoAgent("agent2Multipli@anoxinon.me", "multiplicacao")
                 
                elif operadores["Op"] == "/":
                    receiveragent = DivisionAgent("divisionagent@anoxinon.me", "division")
                elif operadores["Op"] == "^":
                    receiveragent = ExponentiationAgent("exponentiationAgent@anoxinon.me", "exponentiation")
                
                """
                
                receiveragent = None
                """
                if operands["Op"] == "+":
                    receiveragent = AdditionAgent("sumagent@anoxinon.me", "sum")
                elif operands["Op"] == "-":
                    receiveragent = SubtractionAgent("minusagent@anoxinon.me", "minus")
                elif operands["Op"] == "/":
                    receiveragent = DivisionAgent("divisionagent@anoxinon.me", "division")
                elif operands["Op"] == "^":
                    receiveragent = ExponentiationAgent("exponentiationAgent@anoxinon.me", "exponentiation")
                """
                if operadores["Op"] == "*":
                    receiveragent = MultiplicacaoAgent("agent2Multipli@anoxinon.me", "multiplicacao")
                  #agent2Multipli@anoxinon.me", "multiplicacao  #multiplyagent@anoxinon.me", "multiply
                await receiveragent.start(auto_register=True)
                
                
                #await asyncio.sleep(1)
                print("Valor1 e Valor2 = "+valores)
                #print(" jid "+str(receiveragent.jid))
                msg = Message(to="agent2Multipli@anoxinon.me")
                #msg.to=str(receiveragent.jid)# jid do recptor da mensagem
                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")
                msg.body = str(valores)

                await self.send(msg)#Envia a mensagem para o agente escolhido
                print("Mensagem enviada do COORDENADOR= " + valores)
                
                #Recebe a mesagem de volta do agente que foi escolhido
                msg = await self.receive(timeout=50) #Espera a mensagem por 10 segundos
                if msg:
                    print("Resultado recebido do AGENTE ESCOLHIDO "+ msg.body )
                    valor[operadores["indiceOp"]] = msg.body # A passagem do indice estva errado
                    del(valor[operadores['indiceOp'] + 1])#Deletando valor1 e valor2 e substituindo o operador (-,+,/,*,^)
                    del(valor[operadores['indiceOp'] - 1])#pela resposta devolvida pelos agentes
                    print("Nova expressao " + valor[0]) #ele nao estava printando a list -> tem que alterar essa logica pq nao esta prevendo tudo
                

    async def setup(self):
        print("Agent Coordenador starting . . .")
        b = self.CoordenadorBehav()
        self.add_behaviour(b)

if __name__ == "__main__":
    dummy = CoordenadorAgent("agent1Coordenador@anoxinon.me", "coordenador")#agent1Coordenador@anoxinon.me", "coordenador
    future = dummy.start()                                                #coordenatoragent@anoxinon.me", "coordenator
    future.result()

    

    print("Wait until user interrupts with ctrl+C")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
    dummy.stop()

"""
import time

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template

from AdditionAgent import AdditionAgent
from DivisionAgent import DivisionAgent
from ExponentiationAgent import ExponentiationAgent
from ExpressionAnalysis import separateString, solve_expression
from makeMessage import makeMessage
from MultiplyAgent import MultiplyAgent
from SubtractionAgent import SubtractionAgent


class CoordenatorAgent(Agent):
    class CoordenatorBehav(CyclicBehaviour):

        async def run(self):
            print("CoordenatorBehav running")

            # Receives a expression from user
            data = separateString(str(input("Digite a expressão > ")))

            # Tratar a expressão para saber qual agente chamar

            # Answer = 25
            # data = separateString("(100 – 413 * (20 – 5 * 4) + 25) / 5")

            # Answer = 32
            # data = separateString("27 + (14 + 3 * (100 / (18 – 4 * 2) + 7) ) / 13")

            # Answer = 180
            # data = separateString("10 * (30 / (2 * 3 + 4) + 15)")

            # Answer = -81
            # data = separateString("25 + (14 – (25 * 4 + 40 – 20))")

            # Answer = -16
            # data = separateString("23 + 12 - 55 + (2 + 4) - 8 / 2 ^ 2")

            # Answer = 30
            # data = separateString("32 + 22 / 2 + 5 - 6 * 3")

            print(data)

            while(len(data) > 1):
                operands = solve_expression(data)

                onlyNumbersData = f"{operands['x1']} {operands['x2']}"

                # Send the message to the agent
                receiveragent = None
                if operands["Op"] == "+":
                    receiveragent = AdditionAgent("sumagent@anoxinon.me", "sum")
                elif operands["Op"] == "-":
                    receiveragent = SubtractionAgent("minusagent@anoxinon.me", "minus")
                elif operands["Op"] == "/":
                    receiveragent = DivisionAgent("divisionagent@anoxinon.me", "division")
                elif operands["Op"] == "^":
                    receiveragent = ExponentiationAgent("exponentiationAgent@anoxinon.me", "exponentiation")
                elif operands["Op"] == "*":
                    receiveragent = MultiplyAgent("multiplyagent@anoxinon.me", "multiply")

                await receiveragent.start(auto_register=True)

                print(onlyNumbersData)
                msg = makeMessage(str(receiveragent.jid), onlyNumbersData)

                await self.send(msg)
                print(f"Message sent! ({onlyNumbersData})")
                msg = await self.receive(timeout=10)
                if msg:
                    print(f"Result received! ({msg.body})")
                    data[operands["n"]] = msg.body
                    del(data[operands['n'] + 1])
                    del(data[operands['n'] - 1])
                    print(f"Answer: {data}")
            print(f"================ FINAL ANSWER: {float(data[0])} ================")

    async def setup(self):
        print("CoordenatorAgent started")

        informBehav = self.CoordenatorBehav()

        self.add_behaviour(informBehav)


if __name__ == "__main__":
    senderagent = CoordenatorAgent("coordenatoragent@anoxinon.me", "coordenator")
    future = senderagent.start()
    future.result()

    senderagent.web.start(hostname="127.0.0.1", port="2")

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            senderagent.stop()
            break
    print("Agents finished")
    """