import sys


if __name__ == "__main__":
    vowels = 'aeiouAEIOU'
    if len(sys.argv) == 2:
        user_value = str(sys.argv[1])
        if user_value[0] in vowels:
            print(
                f"Ahow, Captain, an {user_value.capitalize()} off the landboard bow!")
        else:
            print(
                f"Ahow, Captain, a {user_value.capitalize()} off the landboard bow!")
    else:
        result_str = ""
        for c, i in enumerate(sys.argv[1:]):
            if c == 0:
                result_str += "an " + i if i[0] in vowels else "a " + i
            elif not c == (len(sys.argv)-2):
                result_str += ", an " + i if i[0] in vowels else ", a " + i
            else:
                result_str += " and an " + \
                    i if i[0] in vowels else " and a " + i
        print(f"Ahow, Captain, {result_str} of the landboard bow!")
