"""Command line tooling for interacting with the Dragonfly system."""

import tarfile
from io import BytesIO
from zipfile import ZipFile

from letsbuilda.pypi import PyPIServices
from requests import Session

from dragonfly_lib.constants import TAR_FILE_EXTENSIONS, ZIP_FILE_EXTENSIONS


def read_zipfile(buffer: BytesIO) -> dict[str, str]:
    """Return a dictionary mapping filenames to content."""
    files = {}
    with ZipFile(file=buffer) as zip_file:
        for zip_info in zip_file.infolist():
            if not zip_info.is_dir():
                files[zip_info.filename] = zip_file.read(zip_info).decode(encoding="UTF-8", errors="ignore")
    return files


def read_tarfile(buffer: BytesIO) -> dict[str, str]:
    """Return a dictionary mapping filenames to content."""
    files = {}
    with tarfile.open(fileobj=buffer) as file:
        for tarinfo in file:
            if tarinfo.isreg():
                files[tarinfo.name] = file.extractfile(tarinfo).read().decode(encoding="UTF-8", errors="ignore")
    return files


def get_archive_contents(filename: str, url: str) -> dict[str, str]:
    """Return a dictionary mapping filenames to content."""
    http_session = Session()
    client = PyPIServices(http_session)
    bytes_ = client.fetch_bytes(url)

    if any(filename.endswith(text) for text in ZIP_FILE_EXTENSIONS):
        return read_zipfile(bytes_)

    if any(filename.endswith(text) for text in TAR_FILE_EXTENSIONS):
        return read_tarfile(bytes_)

    msg = "Unsupported file type!"
    raise ValueError(msg)
