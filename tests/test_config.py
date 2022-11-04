import filecmp
from configparser import ConfigParser
from pathlib import Path

import pytest

from weather_uk.config import (
    CONFIG_TEMPLATE,
    setup_config_if_none_exists,
    update_config,
)


@pytest.fixture
def mock_config_path(tmp_path):
    p = tmp_path / "weather-uk"
    return p


def test_setup_config_if_none_exists(mock_config_path):
    setup_config_if_none_exists(mock_config_path)
    config_file = Path(mock_config_path / "weather-uk.cfg")
    assert config_file.is_file()
    assert config_file.parent.name == "weather-uk"
    assert filecmp.cmp(CONFIG_TEMPLATE, config_file, shallow=False) is True


def test_update_config(mock_config_path):
    setup_config_if_none_exists(mock_config_path)
    update_config(apikey="metofficeapikey", config_path=mock_config_path)

    cfgparser = ConfigParser()
    config_file = Path(mock_config_path) / "weather-uk.cfg"
    cfgparser.read(config_file)
    auth = cfgparser["auth"]
    assert config_file.is_file()
    assert auth["apikey"] == "metofficeapikey"
