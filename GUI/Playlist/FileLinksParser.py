from pathlib import Path, PureWindowsPath, PurePath
import mimetypes
from urllib import parse
import re
from xspf_lib import Playlist
import platform


if platform.system() == 'Windows':
    mimetypes.add_type('application/pls+xml', '.pls')
    mimetypes.add_type('application/xspf+xml', '.xspf')
AudioMimes = ['audio/x-wav', 'audio/wav', 'audio/mpeg', 'audio/aiff', 'audio/x-aiff', 'audio/x-flac', 'audio/ogg',
              'application/ogg']
PLMimes = ['audio/x-mpegurl', 'application/pls+xml', 'application/xspf+xml']


def pathsResolve(Paths: list[str], return_dict: dict):
    def make_error_list(msg):
        errors.append(str(msg))
    paths = []
    errors = []
    for path in Paths:
        _Path = Path(path)
        if _Path.is_file():
            paths.append(path)
        elif _Path.is_dir():
            paths.extend(filesFromDir(_Path))
            paths.sort()
    paths = filePathsFilter(expandPlayLists(filePathsFilter(paths), callback=make_error_list))
    return_dict['Paths'] = paths
    return_dict['Errors'] = errors
    return return_dict


def filesFromDir(dirpath: Path):
    dir_content = dirpath.glob('**/*')
    return [str(el) for el in dir_content if el.is_file()]


def filePathsFilter(paths: list[str]):
    MimeTypes = AudioMimes + PLMimes
    return [path for path in paths if
            mimetypes.guess_type(path)[0] in MimeTypes and not Path(path).name.startswith('.')]


def expandPlayLists(paths: list[str], callback=None):
    paths_expanded = []
    for path in paths:
        if mimetypes.guess_type(path)[0] in PLMimes:
            files = files_from_PL(path, callback)
            paths_expanded.extend(files)
        else:
            paths_expanded.append(path)
    return paths_expanded


def files_from_PL(pl_path: str, callback=None):
    def cb(arg):
        if callback is not None:
            callback(str(arg))

    mime = mimetypes.guess_type(pl_path)[0]
    err_mess = f'Error occurred while parsing "{pl_path}": '
    if mime == 'application/xspf+xml':
        try:
            pl_urls = parseUrlsFromXSPF(pl_path)
        except Exception as e:
            cb(f'{err_mess}{e}')
            return []
    elif mime in ('audio/x-mpegurl', 'application/pls+xml'):
        try:
            with open(pl_path, 'r') as f:
                pl_lines = [line.rstrip() for line in f.readlines()]
        except Exception as e:
            cb(f'{err_mess}{e}')
            return []
        pl_urls = pl_lines if mime not in ('application/pls+xml') else list(map(parseUrlFrom_PLS, pl_lines))
    else:
        return []
    return urlsToExistingFiles(pl_urls, Path(pl_path).parent)


def parseUrlFrom_PLS(line: str):
    return re.sub('File\d+=', '', line, count=1)


def parseUrlsFromXSPF(filepath: str):
    return [track.location[0] for track in Playlist.parse(filepath).data]


def urlsToExistingFiles(urls: list, current_dir):
    files = []
    for url in urls:
        path = parse.urlparse(url).path
        abs_path = path if Path(path).is_absolute() \
            else str(PurePath.joinpath(current_dir, PureWindowsPath(path).as_posix()))
        if Path(abs_path).is_file():
            files.append(abs_path)
    return files
