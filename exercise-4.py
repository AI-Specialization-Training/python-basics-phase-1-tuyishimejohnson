# ============================================================================
# TODO: Data Type Conversion

# Create a function called data_type_conversion.
# It takes two parameters, the value and the name of the data type requested, one of float, str, or int.
# Return the converted value.
# Error handling: The function might be called with a bad parameter.
# For example, the caller might try to convert the string "nonsense" to a float.
# Catch the error that occurs in this case. If this error occurs,
# return the string You can't convert {value} into a {type}., so again you use a formatted string.

# ============================================================================


def data_type_conversion(value, str):
    if str == "float":
        return float(value)
    elif str == "int":
        return int(value)
    elif str == "str":
        return str(value)
    else:
        return f"You can't convert {value} into a {str}"


print(data_type_conversion(45, "float"))
