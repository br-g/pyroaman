from typing import Union
import json
from pathlib import Path
from pyroaman.database import Database
from pyroaman.parsing import parse_database


def load(path_json: Union[str, Path]) -> Database:
    with open(path_json) as f:
        raw = json.load(f)
    return parse_database(raw)
