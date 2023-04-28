class Hello:
    def __init__(self, str):
        self.str = str

class NewestClass(Hello):
    def __init__(self, str):
        super().__init__(str)
        self.str = str
    def __str__(self):
        return self.str



