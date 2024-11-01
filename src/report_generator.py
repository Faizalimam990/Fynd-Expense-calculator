from collections import defaultdict

class ReportGenerator:
    def __init__(self, expenses):
        self.expenses = expenses

    def generate_report(self, period):
        report = defaultdict(float)

        for expense in self.expenses:
            if period == 'daily':
                key = expense.date.strftime("%Y-%m-%d")
            elif period == 'weekly':
                key = expense.date.strftime("%Y-%U")
            elif period == 'monthly':
                key = expense.date.strftime("%Y-%m")

            report[key] += expense.amount

        self.display_report(report)

    def display_report(self, report):
        print(f"\n{'Period':<15} {'Total Amount':<10}")
        print("-" * 30)
        for period, total in report.items():
            print(f"{period:<15} {total:<10}")
