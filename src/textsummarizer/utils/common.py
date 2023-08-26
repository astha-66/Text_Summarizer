import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import path
from typing import Any


@ensure_annotations

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml file and return
    :param path_to_yaml: Path to yaml file
       """