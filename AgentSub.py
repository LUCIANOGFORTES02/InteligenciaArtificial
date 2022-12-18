import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class SubAgent(Agent):
    class MyBehav(CyclicBehaviour):
       

        async def run(self):
            print("Counter: {}".format(self.counter))
            


        
    async def setup(self):
        print("Agent starting . . .")
        self.my_behav = self.MyBehav()
        self.add_behaviour(self.my_behav)

if __name__ == "__main__":
    dummy = SubAgent(" ", " ")
    future = dummy.start()
    future.result()  # Wait until the start method is finished

    # wait until user interrupts with ctrl+C
    while not dummy.my_behav.is_killed():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    dummy.stop()