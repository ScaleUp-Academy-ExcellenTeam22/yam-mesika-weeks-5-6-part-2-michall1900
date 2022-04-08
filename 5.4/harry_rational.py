from os import rename
from re import search


# Note: I have created a directory with that name but didn't upload it.
DIRECTORY_PATH = "to harry rational"


def find_file_chapter(file_path: str) -> int:
    """
    Return the actual file's chapter.
    :param file_path: File to search in its chapter's name.
    :return: Chapter's number.
    """
    with open(f"{file_path}.html") as file:
        for line in file:
            if line.startswith('<div id="chapter-title">'):
                return int(line[search("[0-9]+", line).start():search("[0-9]+", line).end()])


def page_number_and_its_chapter() -> dict:
    """
    Creating dictionary with key = file's name and argument = it's correct name(the chapter).
    :return: Dictionary as described before.
    """
    return {page_number: find_file_chapter(DIRECTORY_PATH + fr"\{page_number}") for page_number in range(1, 123)}


def swap_file_names(first_file_name: str, second_file_name: str) -> None:
    """
    Swap between two file names.
    :param first_file_name: File's name you want to swap with another file's name.
    :param second_file_name: The second file.
    :return: None.
    """
    rename(first_file_name, DIRECTORY_PATH + r"\temp.html")
    rename(second_file_name, first_file_name)
    rename(DIRECTORY_PATH + r"\temp.html", second_file_name)


def rename_files() -> None:
    """
    Rename files to their actually name.
    :return: None.
    """
    pages_and_chapters = page_number_and_its_chapter()
    chapters_and_pages = {item: key for key, item in pages_and_chapters.items()}
    for page_name in pages_and_chapters:
        if page_name != pages_and_chapters[page_name]:
            actually_page_name = chapters_and_pages[page_name]
            swap_file_names(DIRECTORY_PATH + rf"\{page_name}.html", DIRECTORY_PATH + rf"\{actually_page_name}.html")
            pages_and_chapters[actually_page_name] = pages_and_chapters[page_name]
            chapters_and_pages[pages_and_chapters[page_name]] = actually_page_name


def main_harry_rational() -> None:
    rename_files()


if __name__ == "__main__":
    main_harry_rational()
