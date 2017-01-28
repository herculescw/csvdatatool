

def linecount(filepath):
    """
    count line numbers in file
    :param filepath: file path
    :return: number of lines
    """
    with open(filepath) as f:
        num_lines = sum(1 for line in f)
    return num_lines