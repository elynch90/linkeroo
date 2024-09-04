from argparse import ArgumentParser
from pathlib import Path


def iter_path(path: str):
    """Recursively iterate over a directory and yield all files
    :param path: Path to directory
    :return: Generator of files"""
    if path.is_dir():
        for sub_path in path.iterdir():
            yield from iter_path(sub_path)
    if path.is_file():
        yield path


def format_static_link(fp: str) -> str:
    """Format a static library file path for linking
    :param fp: File path to format
    :return: Formatted string"""
    dir = fp.parent
    file = fp.name
    dir_str = f'-L{dir}'
    file = file.replace('lib', '-l').replace('.a', '')
    return f'{dir_str} {file}'


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('--fp', help='Input file')
    parser.add_argument('--output', help='Output file')
    parser.add_argument('--suffix', help='File suffix', default='.a')
    args = parser.parse_args()
    fp = Path(args.fp)
    file_list = []
    for path in fp.iterdir():
        if path.is_dir():
            for sub_path in iter_path(path):
                file_list.append(sub_path) if sub_path.suffix == args.suffix \
                    else None
        if path.is_file():
            file_list.append(path) if path.suffix == args.suffix else None
    # todo, pool together by common subdirectory -Lsubdir -> -lfile -lfile -lfile
    # instead of -lsuperdir/file -lsuperdir/file
    for fp in file_list:
        print(f'{fp}')
    with open(args.output, 'w') as f:
        for fp in file_list:
            f.write(f'{format_static_link(fp)}\n')


if __name__ == '__main__':
    main()
