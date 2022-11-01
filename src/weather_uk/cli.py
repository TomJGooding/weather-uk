import platformdirs


def main():
    appname = "weather-uk"
    print(platformdirs.user_config_dir(appname))
