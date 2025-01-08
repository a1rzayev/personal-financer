class Statistics:
    @staticmethod
    def calculate_total(transactions):
        return sum(t["amount"] for t in transactions)

    @staticmethod
    def filter_by_category(transactions, category_name):
        return [t for t in transactions if t["category"] == category_name]

    @staticmethod
    def generate_summary(transactions):
        summary = {}
        for t in transactions:
            category = t["category"]
            summary[category] = summary.get(category, 0) + t["amount"]
        return summary
