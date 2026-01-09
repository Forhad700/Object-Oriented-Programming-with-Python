class Phone:
    def call(self):
        print("It's phone call")

class Samsung(Phone):
    def call(self):
        print("It's samsung call")


s = Samsung()
s.call()