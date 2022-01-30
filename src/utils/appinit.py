#-*- coding: utf-8 -*-

"""App initialization"""

import os
from typing import Any

from .settings import Settings

DIR_SEP: str = os.sep

class AppInit:
    """Properly initalize the app."""
    def __init__(self, app_pathes: dict[str, str])->None:
        self.app_pathes: dict[str, str] = app_pathes
        self.settings: dict[str, Any]

        self.get_settings()
        self.set_pathes()

    def get_settings(self)->None:
        """
        Checks for existence of config file
        in different potential location.
        Delegates retreiving settings to settings.Settings
        """
        config_locations: list[str] = [
            f"{self.app_pathes['root']}{DIR_SEP}data{DIR_SEP}conf.json",
            f"{self.app_pathes['home']}{DIR_SEP}.config{DIR_SEP}yap{DIR_SEP}conf.json",
            f"{self.app_pathes['home']}{DIR_SEP}.yapconf.json"
        ]

        for fp in config_locations:
            if os.path.exists(fp) and os.access(fp, os.R_OK):
                get_conf = Settings(fp)
                self.settings = get_conf.load_settings()
                break

    def set_pathes(self)->None:
        """Creates full path for input and output files"""
        if not os.path.isabs(self.app_pathes["input"]):
            self.app_pathes["input"] = os.path.realpath(self.app_pathes["input"])

        if self.app_pathes["output"] == "default":
            self.app_pathes["output"] = f"{self.app_pathes['cwd']}{DIR_SEP}{self.settings['output']['output_file']}"
        else:
            if not os.path.isabs(self.app_pathes["output"]):
                self.app_pathes["output"] = os.path.realpath(self.app_pathes["output"])

    @property
    def init_ok(self) -> bool:
        """Initialization status indicator"""
        if isinstance(self.settings, dict) and len(self.settings) > 0:
            return True
        return False
