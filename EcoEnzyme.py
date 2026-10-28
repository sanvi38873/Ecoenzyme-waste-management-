
import csv
import os
from collections import Counter

FILE_NAME = "biowaste_records.csv"

WASTE_CATEGORIES = {
    "1": "Fruit and Vegetable Waste",
    "2": "Garden Waste",
    "3": "Food Waste",
    "4": "Other Biodegradable Waste"
}


def load_records():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_records(records):
    fields = ["waste_name", "category", "quantity_kg"]

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)


def add_record(records):
    print("\n--- Add Biowaste Record ---")
    name = input("Enter waste name: ").strip()

    if not name:
        print("Waste name cannot be empty.")
        return

    print("\nChoose waste category:")
    for key, category in WASTE_CATEGORIES.items():
        print(f"{key}. {category}")

    choice = input("Enter category number: ").strip()

    if choice not in WASTE_CATEGORIES:
        print("Invalid category.")
        return

    try:
        quantity = float(input("Enter quantity in kg: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    records.append({
        "waste_name": name,
        "category": WASTE_CATEGORIES[choice],
        "quantity_kg": str(quantity)
    })

    save_records(records)
    print("Biowaste record saved successfully!")


def view_records(records):
    print("\n--- Biowaste Records ---")

    if not records:
        print("No records available.")
        return

    for number, record in enumerate(records, start=1):
        print(f"\nRecord {number}")
        print("Waste:", record["waste_name"])
        print("Category:", record["category"])
        print("Quantity:", record["quantity_kg"], "kg")


def show_summary(records):
    print("\n--- Waste Summary ---")

    if not records:
        print("No data available for summary.")
        return

    totals = Counter()

    for record in records:
        totals[record["category"]] += float(record["quantity_kg"])

    for category, quantity in totals.items():
        print(f"{category}: {quantity:.2f} kg")

    overall = sum(float(r["quantity_kg"]) for r in records)
    print(f"\nTotal recorded biowaste: {overall:.2f} kg")


def main():
    records = load_records()

    while True:
        print("\n" + "=" * 38)
        print("       ECOENZYME")
        print(" Biowaste Management Learning Tool")
        print("=" * 38)
        print("1. Add biowaste record")
        print("2. View all records")
        print("3. Show waste summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            show_summary(records)
        elif choice == "4":
            print("Thank you for using EcoEnzyme!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
