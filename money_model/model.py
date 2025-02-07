import mesa
import seaborn as sns
import numpy as np
import pandas as pd


class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, model):
        # Pass the parameters to the parent class.
        super().__init__(model)

        # Create the agent's variable and set the initial values.
        self.wealth = 1

    def say_hi(self):
        print(f"Hi, I am an agent, you can call me {str(self.unique_id)}.")

    def say_wealth(self):
        if self.wealth > 0:
            print(f"Hi, I am an agent {str(self.unique_id)} and I have {self.wealth} units of money.")
        else:
            print(f"Hi, I am an agent {str(self.unique_id)} and I am broke!")

    def exchange(self):
        if self.wealth > 0:
            other_agent = self.random.choice(self.model.agents)
            if other_agent is not None:
                other_agent.wealth += 1
                self.wealth -= 1


class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n

        # Create n agents
        MoneyAgent.create_agents(model=self, n=n)

    def step(self):
        """Advance the model by one step."""

        self.agents.do("say_wealth")
        self.agents.shuffle_do("exchange")
        self.agents.do("say_wealth")
