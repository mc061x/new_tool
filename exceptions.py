class TimeLimitExceededException(Exception):
    """Called when the program exceeded the configured time limit"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RuntimeErrorException(Exception):
    """Called when the program caught a runtime error or have not returned the code 0"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class MemoryLimitExceededException(Exception):
    """Called when the program exceeded the configured time limit"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RequestTimeoutException(Exception):
    """Called when the request exceeded the configured time limit"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RequestConnectionErrorException(Exception):
    """Called when user lost connection during(before) the request"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InternalAPIErrorException(Exception):
    """Called when CF API is experiencing some issues"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class HandleNotSetException(Exception):
    """Called when user has called a method that requires the handle, but the handle was not set"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UndefinedAPIErrorException(Exception):
    """Called when something unexpected happened during the request"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
