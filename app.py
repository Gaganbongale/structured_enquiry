import os

def calculate_average_cost(bookings):
    total = 0
    for booking in bookings:
        total += booking["days"] * booking["cost_per_day"]
    return total / len(bookings)


def assign_category(avg_cost):
    if avg_cost >= 5000:
        return "Luxury"
    elif 3500 <= avg_cost <= 4999:
        return "Premium"
    elif 2000 <= avg_cost <= 3499:
        return "Standard"
    else:
        return "Economy"


def main():
    bookings = [
        {
            "model": os.getenv("MODEL1"),
            "rental_type": os.getenv("TYPE1"),
            "days": int(os.getenv("DAYS1")),
            "cost_per_day": float(os.getenv("COST1"))
        },
        {
            "model": os.getenv("MODEL2"),
            "rental_type": os.getenv("TYPE2"),
            "days": int(os.getenv("DAYS2")),
            "cost_per_day": float(os.getenv("COST2"))
        },
        {
            "model": os.getenv("MODEL3"),
            "rental_type": os.getenv("TYPE3"),
            "days": int(os.getenv("DAYS3")),
            "cost_per_day": float(os.getenv("COST3"))
        }
    ]

    avg_cost = calculate_average_cost(bookings)
    category = assign_category(avg_cost)

    print("Average Rental Cost:", avg_cost)
    print("Category:", category)


if __name__ == "__main__":
    main()
