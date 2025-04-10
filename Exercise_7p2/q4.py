def make_bidirectional(paths):
    for path in list(paths):
        paths.add((path[1], path[0]))  # Add reverse direction
    return paths
town_distances = {
    ('Lohja', 'Vaasa'): 100,
    ('Vaasa', 'Lohja'): 100,
    ('Lohja', 'Helsinki'): 50,
    ('Helsinki', 'Vaasa'): 200,
}

bidirectional_paths = set(town_distances.keys())
print(f"Bidirectional paths: {make_bidirectional(bidirectional_paths)}")
