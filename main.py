#!/usr/bin/env python

# Standard Library
from glob import glob
from importlib import import_module
from pathlib import Path

# Current project
from validation_base import BaseValidator

for f in glob("./**/validation.py", recursive=True):
    parts = list(Path(f).parts)
    parts[-1] = parts[-1].strip(".py")
    import_module(".".join(parts))

for val in BaseValidator.__subclasses__():
    impl = val()
    for i in [1, 10, 100]:
        print(f"validate({i}) -> {impl.validate(i)}")
