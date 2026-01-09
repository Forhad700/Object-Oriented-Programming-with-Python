class Phone:
    def call(self):
        print("Its Phone call")

class Samsung(Phone):
    def call(self):
        super().call()
        print("Its Samsung call")


s = Samsung()
s.call()