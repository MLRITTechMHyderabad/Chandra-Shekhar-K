class NegativeNumberException(Exception):
    def __init__(self, message):
        self.msg=message
        super.__init__(message)

