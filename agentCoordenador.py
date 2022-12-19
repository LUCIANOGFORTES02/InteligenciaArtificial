import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from VerificandoExpressao import dividindoExpressao,OrdemOperacoes
from AgentAdicao import AdicaoAgent
from AgentSub import SubAgent
from spade.message import Message 
from AgentMultiplicacao import MultiplicacaoAgent
from AgentDivisao import DivisaoAgent
from AgentAdicao import AdicaoAgent
from AgentPotencia import PotenciaAgent
from AgentSub import SubAgent


class CoordenadorAgent(Agent):
    class  CoordenadorBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
        
        #É o metodo no qual o nucleo da programação é feito porque            
        #esse método é chamado a cada interação do loop de comportamento 
        async def run(self):  
            print ("Digite a expressao")
            expressao = "23 + 12 - 55 + ( 2 + 4 ) - 8 / 2 ^ 2"
            #expressao=str(input ())

            valor= dividindoExpressao(expressao)
            
            #Qual agente será chamado
            while (len(valor)>1):
                operadores =  OrdemOperacoes(valor)#Retorna um dicionario
                valores = f"{operadores['valor1']} {operadores['valor2']}"
                
                receiveragent = None
                
                if operadores["Op"] == "-":
                    receiveragent = SubAgent("agent6Subtracao@anoxinon.me", "subtracao")
                    msg = Message(to="agent6Subtracao@anoxinon.me")
                
                elif operadores["Op"] == "+":
                    receiveragent = AdicaoAgent("agent4Adicao@anoxinon.me", "adicao")
                    msg = Message(to="agent4Adicao@anoxinon.me")

                elif operadores["Op"] == "^":
                    receiveragent = PotenciaAgent("agent5Potencia@anoxinon.me", "potencia")
                    msg = Message(to="agent5Potencia@anoxinon.me")


                elif operadores["Op"] == "/":
                    receiveragent = DivisaoAgent("agent3Divisao@anoxinon.me", "divisao")
                    msg = Message(to="agent3Divisao@anoxinon.me")

                elif operadores["Op"] == "*":
                    receiveragent = MultiplicacaoAgent("agent2Multipli@anoxinon.me", "multiplicacao")
                    msg = Message(to="agent2Multipli@anoxinon.me")#Para quem a mensagem sera enviada
                
                await receiveragent.start(auto_register=True)
                
                
                print("Valor1 e Valor2 = "+valores)
                #msg = Message(to="agent2Multipli@anoxinon.me")
                #msg.to=str(receiveragent.jid)# jid do recptor da mensagem
                # Set the "inform" FIPA performative
                msg.set_metadata("performative", "inform")
                msg.body = str(valores)

                await self.send(msg)#Envia a mensagem para o agente escolhido
                print("Mensagem enviada do COORDENADOR= " + valores)
                
                #Recebe a mesagem de volta do agente que foi escolhido
                msg = await self.receive(timeout=50) #Espera a mensagem por 50 segundos
                if msg:
                    print("Resultado recebido do AGENTE ESCOLHIDO "+ msg.body )
                    valor[operadores["indiceOp"]] = msg.body # A passagem do indice estava errado
                    del(valor[operadores['indiceOp'] + 1])#Deletando valor1 e valor2 e substituindo o operador (-,+,/,*,^)
                    del(valor[operadores['indiceOp'] - 1])#pela resposta devolvida pelos agentes
                    #print("Nova expressao " + valor[0]) #ele nao estava printando a list -> tem que alterar essa logica pq nao esta prevendo tudo
                    print(f"Expressao : {valor}")
                

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