import sys


def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename)
        for line in fh:
            if line.strip():
                lines.append(line)
    except(IOError, OSError) as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()
    return lines


def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, "w")
        for line in lines:
            fh.write(line)
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()


def remove_blank_lines():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} [file....]")
    for filename in sys.argv[1:]:
        lines = read_data(filename)
    if lines:
        write_data(lines, filename)


if __name__ == '__main__':
    remove_blank_lines()

