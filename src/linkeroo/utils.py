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


def format_static_link(fp: str) -> str:
    """Format a static library file path for linking
    :param fp: File path to format
    :return: Formatted string"""
    dir = fp.parent
    file = fp.name
    dir_str = f'-L{dir}'
    file = file.replace('lib', '-l').replace('.a', '')
    return f'{dir_str} {file}'
