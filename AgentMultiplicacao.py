import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class MultiplicacaoAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0

        async def run(self):
            print("Counter: {}".format(self.counter))
            self.counter += 1
            if self.counter > 3:
                self.kill(exit_code=10)
                return
            await asyncio.sleep(1)

        async def on_end(self):
            print("Behaviour finished with exit code {}.".format(self.exit_code))

    async def setup(self):
        print("Agent starting . . .")
        self.my_behav = self.MyBehav()
        self.add_behaviour(self.my_behav)

if __name__ == "__main__":
    dummy = MultiplicacaoAgent("your_jid@your_xmpp_server", "your_password")
    future = dummy.start()
    future.result()  # Wait until the start method is finished

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
        def generateResult(self, n1, n2):
            return float(n1) * float(n2)

        async def run(self):
            print("MultiplyBehav running")

            # wait for a message for 10 seconds
            msg = await self.receive(timeout=10)
            if msg:
                numbers = msg.body.split(" ")
                result = self.generateResult(numbers[0], numbers[1])
                msgSend = makeMessage("coordenatoragent@anoxinon.me", result)

                await self.send(msgSend)

                print(f"Result send! ({result})")
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
    future.result()

    receiveragent.web.start(hostname="127.0.0.1", port="10000")

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            receiveragent.stop()
            break

    print("Agents finished")"""