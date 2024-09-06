from os import getcwd
from argparse import ArgumentParser
from pathlib import Path
from linkeroo.utils import traverse_dir
CWD = getcwd()


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('--fp', help='Input file', default=CWD)
    parser.add_argument('--output', help='Output file', default='linkeroo.txt')
    parser.add_argument('--suffix', help='File suffix', default='.a')
    parser.add_argument(
        '--print', help='print each path', default=False, type=bool)
    args = parser.parse_args()
    fp = Path(args.fp)
    output = Path(args.output)
    suffix = args.suffix
    use_print = args.print
    traverse_dir(fp, output, suffix, use_print)


if __name__ == '__main__':
    main()
