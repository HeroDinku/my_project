import csv

# Allow the data file to be configurable
DATA_FILE = 'data/expenses.csv'

def add_expense(category, amount):
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])

def remove_expense(category):
    lines = []
    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        lines = [row for row in reader if row[0] != category]

    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

def view_expenses():
    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def calculate_total():
    total = 0.0
    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        total = sum(float(row[1]) for row in reader)
    return total

if __name__ == '__main__':
    add_expense('Groceries', 50)
    print(view_expenses())
    print(f'Total: {calculate_total()}')
