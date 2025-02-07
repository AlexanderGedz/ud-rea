from money_model.model import MoneyModel

starter_model = MoneyModel(10)
for _ in range(30):
    starter_model.step()
