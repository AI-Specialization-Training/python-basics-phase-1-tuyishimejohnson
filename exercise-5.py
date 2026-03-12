# ============================================================================
# TODO: Use a For Loop with a Range

# Create a function called repeat.
# It takes two parameters, a string and a count, and returns a new string that is the old one repeated count times.
# ============================================================================


def repeat(string, count):
    for s in range(count):
        s += 1
    return f"{string} repeated {s} times"


print(repeat("Johnson", 5))
