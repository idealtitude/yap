#-*- coding: utf-8 -*-

"""Utilities for managing app settings and user prefrences"""

from typing import Any

from .filehandler import JsonFile


class Settings:
    """General app settings."""
    def __init__(self, config_file: str)->None:
        self.config_file: str = config_file

    def load_settings(self)->Any:
        """Load basic settings from json config file."""
        getjson = JsonFile(self.config_file)
        return getjson.get_json()
