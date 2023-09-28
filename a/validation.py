# Current project
from validation_base import BaseValidator


class AValidator(BaseValidator):
    def _validate(self, number: int) -> bool:
        return number > 2
