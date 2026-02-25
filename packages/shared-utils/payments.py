"""Cross-Border Payment Infrastructure"""
class PaymentInfrastructure:
    def calculate_transfer_cost(self, amount: float, from_currency: str, to_currency: str):
        fx_spread = 0.01  # 1%
        transfer_fee = 50
        return {
            'fx_cost': amount * fx_spread,
            'transfer_fee': transfer_fee,
            'total': amount * fx_spread + transfer_fee
        }
