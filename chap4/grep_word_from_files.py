import sys


def grep_word_from_files():
    word = sys.argv[1]
    for filename in sys.argv[2:]:
        with open(filename) as file:
            for lino, line in enumerate(file, start=1):
                if word in line:
                    print(f'{filename}:{lino}:{line.rstrip()}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"usage: python {sys.argv[0]} [word] [file...]")
        sys.exit()
    else:
        grep_word_from_files()