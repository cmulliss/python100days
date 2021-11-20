def format_name(first, last):
    # if user enter an empty first or last name, or both
    if first == "" or last == "":
        return "You didn't provide valid inputs"

    format_first = first.title()
    format_last = last.title()
    return f"{format_first} {format_last}"


print(
    format_name(input("What is your first name? "), input("What is your last name? "))
)
