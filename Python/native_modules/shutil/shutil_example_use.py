import shutil


def move(filename, destination):
    return shutil.move(filename, destination)


def copy(filename, destination):
    return shutil.copy(filename, destination)


def _prompt_toolkit():
    filename = str(input("Enter path + filename: "))
    destination = str(input("Enter destination path: "))
    return filename, destination


if __name__ == "__main__":
    operation = str(input("Enter [c/m] for copy/move :"))
    if operation.lower() == "c":
        filename, destination = _prompt_toolkit()
        copy(filename, destination)
    elif operation.lower() == "m":
        filename, destination = _prompt_toolkit()
        move(filename, destination)
