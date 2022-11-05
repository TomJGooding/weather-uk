import filecmp
from configparser import ConfigParser
from pathlib import Path

import pytest

from weather_uk.config import (
    CONFIG_TEMPLATE,
    UserConfig,
    setup_config_if_none_exists,
    update_config,
)


@pytest.fixture
def mock_config_path_when_none_exists(tmp_path):
    p = tmp_path / "weather-uk"
    return p


@pytest.fixture
def mock_config_path_when_exists():
    p = Path("tests/resources")
    return p


def test_setup_config_if_none_exists(mock_config_path_when_none_exists):
    setup_config_if_none_exists(mock_config_path_when_none_exists)
    config_file = Path(mock_config_path_when_none_exists / "weather-uk.cfg")
    assert config_file.is_file()
    assert config_file.parent.name == "weather-uk"
    assert filecmp.cmp(CONFIG_TEMPLATE, config_file, shallow=False) is True


def test_update_config(mock_config_path_when_none_exists):
    setup_config_if_none_exists(mock_config_path_when_none_exists)
    update_config(
        apikey="metofficeapikey",
        config_path=mock_config_path_when_none_exists,
    )

    cfgparser = ConfigParser()
    config_file = Path(mock_config_path_when_none_exists) / "weather-uk.cfg"
    cfgparser.read(config_file)
    auth = cfgparser["auth"]
    assert config_file.is_file()
    assert auth["apikey"] == "metofficeapikey"


def test_user_config_class(mock_config_path_when_exists):
    user_config = UserConfig.from_cfg_file(mock_config_path_when_exists)
    assert user_config.apikey == "01234567-89ab-cdef-0123-456789abcdef"
