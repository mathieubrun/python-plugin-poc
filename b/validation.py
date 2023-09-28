# Current project
from validation_base import BaseValidator


class BValidator(BaseValidator):
    def _validate(self, number: int) -> bool:
        return number > 10
