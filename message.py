from spade.message import Message


def messageCreator ():
    async def run(self):
        print("Mensagem")
        msg = Message(to="receiver@your_xmpp_server")     # Instantiate the message
        msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
        msg.set_metadata("ontology", "myOntology")  # Set the ontology of the message content
        msg.set_metadata("language", "OWL-S")       # Set the language of the message content
        msg.body = "Hello World"                    # Set the message content


        await self.send(msg)
        print("Message sent!")
        # stop agent from behaviour
        await self.agent.stop()



def senderAgent ():
     async def run(self):
            print("InformBehav running")
            msg = Message(to="receiver@your_xmpp_server")     # Instantiate the message
            msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
            msg.body = "Hello World"                    # Set the message content

            await self.send(msg)
            print("Message sent!")

            # stop agent from behaviour
            await self.agent.stop()

def receiveAgent():
     async def run(self):
            print("RecvBehav running")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                print("Message received with content: {}".format(msg.body))
            else:
                print("Did not received any message after 10 seconds")

            # stop agent from behaviour
            await self.agent.stop()
            # teste de compartilhamento de repositorio