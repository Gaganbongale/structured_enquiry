from app import calculate_average_cost, assign_category

def test_average():
    bookings = [
        {"days": 2, "cost_per_day": 3000},
        {"days": 1, "cost_per_day": 4000},
        {"days": 3, "cost_per_day": 2000}
    ]
    assert calculate_average_cost(bookings) == 4333.333333333333


def test_category():
    assert assign_category(6000) == "Luxury"
    assert assign_category(4000) == "Premium"
    assert assign_category(2500) == "Standard"
    assert assign_category(1500) == "Economy"
