from os import environ
from pathlib import Path


def iter_path(path: Path) -> iter:
    """Recursively iterate over a directory and yield all files
    :param path: Path to directory
    :return: Generator of files"""
    if path.is_dir():
        for sub_path in path.iterdir():
            yield from iter_path(sub_path)
    if path.is_file():
        yield path


def fetch_links(fp: str, suffix: str) -> list[str]:
    p = Path(fp)
    dir_path = p if p.is_dir() else p.parent
    if not dir_path.exists():
        raise ValueError("Directory does not exist")
    links = []
    dirs = [dir_path]
    while dirs:
        new_dirs = []
        for item in dirs:
            lib_paths = []
            for path in item.iterdir():
                if path.is_file() and path.suffix == suffix:
                    lib_name = path.name.replace('lib', 'l').replace(suffix, '')
                    lib_paths.append(lib_name)
                elif path.is_dir():
                    new_dirs.append(path)
            if lib_paths:
                links.append(f'-L{item} ' + ' '.join(f'-{lib}' for lib in lib_paths))
        dirs = new_dirs
    return links


def traverse_dir(fp: Path, output, suffix: str, use_print: bool) -> None:
    """Traverse a directory and write all static library files to a file
    :param fp: Path to directory
    :param output: Output file
    :param suffix: File suffix
    :param use_print: Print each path"""
    links = fetch_links(fp, suffix)
    # todo, pool together by common subdirectory -Lsubdir -> -lfile -lfile -lfile
    # instead of -lsuperdir/file -lsuperdir/file
    with open(output, 'w') as f:
        for link in links:
            if use_print:
                print(f'{link}')
            f.write(f'{link}\n')
    print(f'Output written to {output}')


def main() -> None:
    fp = 'test/'
    output = "linkeroo.txt"
    suffix = ".a"
    use_print = True
    fp = Path(fp)
    output = Path(output)
    traverse_dir(fp, output, suffix, use_print)


# test
if __name__ == '__main__':
    main()
