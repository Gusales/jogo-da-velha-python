def printNameWithColor(color, name):
    match color:
        case "purple":
            return f"\033[1;34m{name}\033[m"
        case "blue":
            return f"\033[1;36m{name}\033[m"
        case "white":
            return f"\033[1;30m{name}\033[m"
        case _:
            return name