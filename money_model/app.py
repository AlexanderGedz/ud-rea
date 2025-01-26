import mesa
import seaborn as sns
import numpy as np
import pandas as pd


class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1

    def say_hi(self):
        print(f"Hi, I am agent {self.unique_id} and I have {self.wealth} wealth.")


class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        MoneyAgent.create_agents(model=self, n=n)

    def step(self):
        """Advance the model by one step."""
        
        self.agents.shuffle_do("say_hi")


starter_model = MoneyModel(10)
starter_model.step()
