"""Multi-Jurisdiction Tax Platform"""
class InternationalTaxPlatform:
    def calculate_withholding_tax(self, amount: float, source: str, recipient: str):
        rates = {('MT', 'US'): 0.15, ('MT', 'UK'): 0.0}
        rate = rates.get((source, recipient), 0.15)
        return {'withholding': amount * rate, 'rate': rate}
