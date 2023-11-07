
class MyServo:
    def __init__(self, p : int):
        self.pin = p

    def write(self, val: int):
        return