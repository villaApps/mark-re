"""Currency Hedging Calculator"""
class FXHedgingCalculator:
    def calculate_forward_cost(self, amount: float, currency: str, months: int):
        forward_rate = 0.02  # 2% annual
        cost = amount * forward_rate * (months / 12)
        return {'hedging_cost': cost, 'percentage': forward_rate * 100}
