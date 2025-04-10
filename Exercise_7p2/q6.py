import re
def regex_operations():
    pattern = r"\d+"

    # Match
    result = re.match(pattern, "123abc")
    print(f"Match result: {result.group() if result else 'No match'}")

    # Search
    result = re.search(pattern, "abc123xyz")
    print(f"Search result: {result.group() if result else 'No match'}")

    # Substitution
    result = re.sub(pattern, "REPLACEMENT", "abc123xyz")
    print(f"Substitution result: {result}")

regex_operations()