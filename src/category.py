class Category:
    def __init__(self):
        self.categories = ['Groceries', 'Utilities', 'Entertainment', 'Other']

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories.append(category_name)
            print(f"Category '{category_name}' added successfully.")
        else:
            print(f"Category '{category_name}' already exists.")

    def get_categories(self):
        return self.categories
