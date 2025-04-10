calculate_travel_cost_lambda = lambda path, town_distances: sum(town_distances.get((path[i], path[i + 1]), 0) for i in range(len(path) - 1))
town_distances = {
    ('Lohja', 'Vaasa'): 100,
    ('Vaasa', 'Lohja'): 100,
    ('Lohja', 'Helsinki'): 50,
    ('Helsinki', 'Vaasa'): 200,
}
path = ['Lohja', 'Vaasa', 'Helsinki']
print(f"Lambda travel cost for {path}: {calculate_travel_cost_lambda(path, town_distances)}")
