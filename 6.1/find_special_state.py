def get_keyboard_rows() -> list[set[str]]:
    """
    Return a list of sets that include letters in each line on the keyboard.
    :return: Letters in each line on the keyboard.
    """
    return [set("q,w,e,r,t,y,u,i,o,p".split(",")), set("a,s,d,f,g,h,j,k,l".split(",")), set("z,x,c,v,b,n,m".split(","))]


def find_special_state(file_name: str) -> str:
    """
    Search inside a file which is the special state and return state's name (should be just one).
    A special state is a state that wrote in one line on the keyboard.
    :param file_name: Path to the state.txt file.
    :return: Special state's name.
    """
    keyboard_rows = get_keyboard_rows()
    with open(file_name) as file:
        for line in file:
            for row in keyboard_rows:
                if set(line[:-1]).issubset(row):
                    return line


def main_special_state() -> None:
    print(find_special_state("states.txt"))


if __name__ == "__main__":
    main_special_state()
