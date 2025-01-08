class Transaction:
    def __init__(self, amount, category, description="", date=None):
        import datetime
        self.amount = amount  
        self.category = category 
        self.description = description
        self.date = date or datetime.datetime.now().strftime("%y-%m-%d")

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data.get("description", ""),
            date=data.get("date")
        )