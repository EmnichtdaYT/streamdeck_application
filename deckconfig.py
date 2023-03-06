import os
from os import path
import json
import logger

device_config_path = path.realpath('./config/deckconfig')


def create_deckconfig(serial: str) -> bool:
    deckconfig_path = path.realpath(path.join(device_config_path, serial))
    deckconfig_file_path = path.join(deckconfig_path, "config.json")

    if not path.exists(deckconfig_path):
        try:
            os.makedirs(deckconfig_path)
        except OSError as e:
            logger.log_error(str(e))
            return False
    elif not path.isdir(deckconfig_path):
        logger.log_error(f"Deckconfig path '{deckconfig_path}' is not a directory!")
        return False

    if not path.exists(deckconfig_file_path):
        with open(deckconfig_file_path, "w+") as deckconfig_file:
            deckconfig_file.write("{}")

    return True
