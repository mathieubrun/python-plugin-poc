class BaseValidator:
    def validate(self, number: int) -> bool:
        print(f"validating from {self.__class__.__module__}.{self.__class__.__name__}")
        return self._validate(number)

    def _validate(self, number: int) -> bool:
        pass