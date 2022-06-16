# Create classes , methods

class wait_what:
    def __init__(self, state, real):
        self.state = state
        self.real = real

    def __str__(self):
        return self.state

    def __repr__(self):
        return self.real

    def exc(self):
        print("Bruh self is just this keyword")

    def pig(self):
        print("Pog state:", self.state)
        print("Pog real:", self.real)

a = wait_what("", "")
a.exc()

b = wait_what("i like [ this ] keyword", "real")
b.pig()
