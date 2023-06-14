#!/usr/bin/python3
"""Reads from standard input and computes metrics
"""


def print_stats(file_size, status_codes):
    """Print accumulated metrics
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(file_size, status_codes)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                file_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid_codes:
                    if status_codes.get(parts[-2], -1) == -1:
                        status_codes[parts[-2]] = 1
                    else:
                        status_codes[parts[-2]] += 1
            except IndexError:
                pass

        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
