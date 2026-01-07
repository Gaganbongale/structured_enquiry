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
    bookings = []

    for i in range(3):
        print(f"\nBooking {i+1}")
        model = input("Car Model: ")
        rental_type = input("Rental Type: ")
        days = int(input("Days: "))
        cost = float(input("Cost per Day: "))

        bookings.append({
            "model": model,
            "rental_type": rental_type,
            "days": days,
            "cost_per_day": cost
        })

    avg = calculate_average_cost(bookings)
    category = assign_category(avg)

    print("\nAverage Rental Cost:", avg)
    print("Category:", category)


if __name__ == "__main__":
    main()
