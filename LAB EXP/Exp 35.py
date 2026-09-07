import numpy as np

# Portfolio allocations
portfolios = {
    "Conservative": [0.2, 0.8],
    "Balanced": [0.5, 0.5],
    "Aggressive": [0.8, 0.2]
}

# Expected returns
stock_return = 0.10
bond_return = 0.05

print("Investment Portfolio Value Prediction")
print("--------------------------------------")

initial_investment = 100000

for name, allocation in portfolios.items():

    stock = allocation[0]
    bond = allocation[1]

    expected_return = (
        stock * stock_return +
        bond * bond_return
    )

    future_value = (
        initial_investment *
        (1 + expected_return)
    )

    print("\nPortfolio:", name)
    print("Stock Allocation:", stock * 100, "%")
    print("Bond Allocation :", bond * 100, "%")
    print("Expected Return :", round(expected_return * 100, 2), "%")
    print("Predicted Value  :", round(future_value, 2))
