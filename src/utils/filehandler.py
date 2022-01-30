#-*- coding: utf-8 -*-

"""File handler"""

import sys
import os
import errno

from typing import Any, Type
import json


""" def custom_excepthook(etype: Type[BaseException], value: BaseException, traceback: Any)->None:
    '''Custom excepthook'''
    print(f"{etype}\n{value}\n{traceback}" )

sys.excepthook = custom_excepthook """


class FileChecks:
    """Performs various checking on fils"""
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path

    def is_readable(self)->bool:
        return os.access(self.file_path, os.R_OK)

    def is_writable(self)->bool:
        return os.access(self.file_path, os.W_OK)

    def is_file(self)->bool:
        if os.path.isfile(self.file_path):
            return True
        return False

    def raise_errors(self, errcode: int)->None:
        errmsr: str

        if errcode == 1:
            errmsg = f"Error {errno.ENOENT}: {os.strerror(errno.ENOENT)} {self.file_path}"
            raise FileNotFoundError(errmsg)

        if errcode == 2:
            errmsg = f"Error {errno.EPERM}: {os.strerror(errno.EPERM)} {self.file_path}"
            raise PermissionError(errmsg)

class BasicFIle:
    """Basic file class"""
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        self.checks = FileChecks(file_path)

    def get_content(self, rettype: str = "list", openmode: str = 'r') -> list[str | bytes] | str | bytes | None:
        file_content: list[str | bytes] | str | bytes | None
        check_exists: bool = self.checks.is_file()
        check_readable: bool = self.checks.is_readable()

        if check_exists and check_readable:
            with open(self.file_path, openmode) as fp:
                if rettype == "list":
                    file_content = fp.readlines()
                elif rettype == "str":
                    file_content = fp.read()
                else:
                    file_content = None
        else:
            if not check_exists:
                self.checks.raise_errors(1)

            if not check_readable:
                self.checks.raise_errors(2)

        return file_content

    def set_content(self, content: str | list[str]) -> bool:
        check_exists: bool = self.checks.is_file()
        check_writable: bool = self.checks.is_writable()

        if check_exists and check_writable:
            with open(self.file_path, 'w') as fp:
                if isinstance(content, list):
                    fp.writelines(content)
                elif isinstance(content, str):
                    fp.write(content)
                else:
                    return False
        else:
            if not check_exists:
                self.checks.raise_errors(1)

            if not check_writable:
                self.checks.raise_errors(2)

        return True

class JsonFile(BasicFIle):
    """Child class of BasicFile especially for json files"""
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def get_json(self)->Any:
        """Return dict from json"""
        raw_content: list[str | bytes] | str | bytes | None = self.get_content(rettype="str", openmode="r")

        return json.loads(str(raw_content))
