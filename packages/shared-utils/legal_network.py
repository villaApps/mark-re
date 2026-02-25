"""Legal Network Integration"""
class LegalNetwork:
    def __init__(self):
        self.lawyers = {
            'MT': [{'name': 'Malta Law Firm', 'specialty': 'property'}],
            'US': [],  # Stub
            'UK': []   # Stub
        }
    
    def get_lawyers(self, jurisdiction: str):
        return self.lawyers.get(jurisdiction, [])
