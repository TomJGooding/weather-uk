import shutil
from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path

import platformdirs
from importlib_resources import files

APPNAME: str = "weather-uk"

CONFIG_PATH: Path = platformdirs.user_config_path(APPNAME)
CONFIG_FILENAME = f"{APPNAME}.cfg"

CONFIG_TEMPLATE = files("weather_uk.config_template").joinpath(CONFIG_FILENAME)


@dataclass
class UserConfig:
    apikey: str

    @classmethod
    def from_cfg_file(cls, config_path: Path = CONFIG_PATH):
        cfgparser = ConfigParser()
        config_file = config_path / CONFIG_FILENAME
        cfgparser.read(config_file)

        try:
            auth = cfgparser["auth"]
            apikey = auth["apikey"]
            return cls(apikey=apikey)
        except KeyError as e:
            msg = (
                f"Error detected in config file: {config_file}  "
                f"Missing expected {e} entry."
            )
            print(msg)


def setup_config_if_none_exists(config_path: Path = CONFIG_PATH) -> None:
    if not config_path.is_dir():
        config_path.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy(CONFIG_TEMPLATE, config_path)
        except PermissionError:
            msg = (
                f"Error creating config file at: {config_path}  "
                "Permission is denied."
            )
            print(msg)


def update_config(apikey: str, config_path: Path = CONFIG_PATH):
    cfgparser = ConfigParser()
    config_file = config_path / CONFIG_FILENAME
    cfgparser.read(config_file)

    try:
        auth = cfgparser["auth"]
        auth["apikey"] = apikey
    except KeyError as e:
        msg = (
            f"Error detected in config file: {config_file}  "
            f"Missing expected {e} entry."
        )
        print(msg)

    with open(config_file, "wt") as f:
        cfgparser.write(f)
