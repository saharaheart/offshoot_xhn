class Mammal(object):
    extremities = 4
    def feeds(self):
        print ("milk")
    def proliferates(self):
        pass
class Marsupial(Mammal):
        def proliferates(self):
            print("poach")
class Eutherian(Mammal):
        def proliferates(self):
            print("placenta")