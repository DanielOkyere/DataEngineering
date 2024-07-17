import io
import os

from zipfile import ZipFile


class Utils:
    @staticmethod
    def make_zip_file_bytes(path):
        buf = io.BytesIO()
        with ZipFile(buf, 'w') as zip:
            for full_path, archive_name in Utils.files_to_zip(path=path):
                zip.write(full_path, archive_name)
        return buf.getvalue()

    @staticmethod
    def files_to_zip(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                archive_name = full_path[len(path) + len(os.sep):]
                yield full_path, archive_name
