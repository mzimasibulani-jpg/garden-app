# Garden Advice App

season = input("Enter the season (spring, summer, autumn, or winter): ").strip().lower()


def get_gardening_advice(season):
    """Return gardening advice based on the selected season."""
    if season == "spring":
        return "Spring is a great time to plant flowers and vegetables."
    elif season == "summer":
        return "Water your garden regularly during summer."
    elif season == "autumn":
        return "Autumn is a good time to prepare your garden for winter."
    elif season == "winter":
        return "Protect sensitive plants from cold weather."
    else:
        return "Please enter a valid season."


advice = get_gardening_advice(season)

# Print the gardening advice once to avoid duplicate output.
print(advice)