def smallest_average(person1: dict, person2: dict, person3: dict):
    # Calculate the average result for each contestant
    avg1 = (person1['result1'] + person1['result2'] + person1['result3']) / 3
    avg2 = (person2['result1'] + person2['result2'] + person2['result3']) / 3
    avg3 = (person3['result1'] + person3['result2'] + person3['result3']) / 3
    
    # Compare the averages and return the contestant with the smallest average
    if avg1 < avg2 and avg1 < avg3:
        return person1
    elif avg2 < avg1 and avg2 < avg3:
        return person2
    else:
        return person3
person1 = {"name": "Alice", "result1": 7, "result2": 8, "result3": 9}
person2 = {"name": "Bob", "result1": 6, "result2": 6, "result3": 7}
person3 = {"name": "Charlie", "result1": 9, "result2": 9, "result3": 10}

smallest = smallest_average(person1, person2, person3)
print(smallest)
