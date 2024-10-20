class BirdFly:
    def flyBird(self,bird):
        bird.fly()

class Parrot :
    def fly(self):
        print("Parrot is flying")

class Crow :
    def fly(self):
        print("crow is flying")

p = Parrot()
c = Crow()

bf = BirdFly()

bf.flyBird(p)
bf.flyBird(c)