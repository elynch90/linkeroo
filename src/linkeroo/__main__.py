from argparse import ArgumentParser
from pathlib import Path
from linkeroo.utils import iter_path, format_static_link


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
