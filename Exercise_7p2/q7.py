import re
import time
# Generate a text of 30,000 words
text = " ".join(["word"] * 30000)
replace_string = "string_to_insert"

# a) Using re.sub
def test_re_sub():
    for _ in range(200):
        start_time = time.time()
        modified_text = re.sub("word", replace_string, text)
        print(f"re.sub execution time: {time.time() - start_time}")

# b) Custom function for substitution
def custom_sub(pattern, replacement, text):
    start = 0
    while start < len(text):
        start = text.find(pattern, start)
        if start == -1:
            break
        text = text[:start] + replacement + text[start + len(pattern):]
        start += len(replacement)
    return text

# c) Experimental test for custom substitution
def test_custom_sub():
    for _ in range(200):
        start_time = time.time()
        modified_text = custom_sub("word", replace_string, text)
        print(f"Custom sub execution time: {time.time() - start_time}")

# Running tests for re.sub and custom substitution
test_re_sub()
test_custom_sub()