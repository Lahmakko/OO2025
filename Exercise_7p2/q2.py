def calculate_travel_cost(path, town_distances):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += town_distances.get((path[i], path[i + 1]), 0)  # Assuming town_distances is a dictionary
    return total_cost
