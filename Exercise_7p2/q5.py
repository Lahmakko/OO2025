import itertools

# Define the town_distances dictionary
town_distances = {
    ('Lohja', 'Vaasa'): 100,
    ('Vaasa', 'Lohja'): 100,
    ('Lohja', 'Helsinki'): 50,
    ('Helsinki', 'Vaasa'): 200,
}

# Function to calculate the travel cost
def calculate_travel_cost(path, town_distances):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += town_distances.get((path[i], path[i + 1]), 0)  # Get the cost for the path
    return total_cost

# Function to find the minimum cost path between two towns
def find_min_cost_path(start, end, town_distances, towns):
    possible_paths = itertools.permutations(towns)
    min_cost = float('inf')
    best_path = None

    for path in possible_paths:
        if path[0] == start and path[-1] == end:
            cost = calculate_travel_cost(path, town_distances)  # Calculate the cost of the path
            if cost < min_cost:
                min_cost = cost
                best_path = path

    return best_path, min_cost

# Find minimum cost path from Lohja to Helsinki
towns = ['Lohja', 'Vaasa', 'Helsinki']
best_path, min_cost = find_min_cost_path('Lohja', 'Helsinki', town_distances, towns)
print(f"Minimum cost path: {best_path}, Cost: {min_cost}")
