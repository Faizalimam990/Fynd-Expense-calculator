import datetime

class Expense:
    def __init__(self, amount, date, category, description):
        self.amount = float(amount)
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
        self.category = category
        self.description = description

    def to_dict(self):
        """Convert the expense to a dictionary format for saving to CSV."""
        return {
            'amount': self.amount,
            'date': self.date.strftime("%Y-%m-%d"),
            'category': self.category,
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        """Create an Expense object from a dictionary."""
        return Expense(data['amount'], data['date'], data['category'], data['description'])
