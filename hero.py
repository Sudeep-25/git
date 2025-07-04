class Hero:
    def __init__(self):
    
        self.name = "dboss"
        self.age=47
        self.height = 6.2
        self.mob = 99779
    def act(self):
        print("Hero is acting")
    def dance(self):
        print("Hero is dancing")
h1 = Hero()

print(h1.name)
print(h1.age)
print(h1.height)
print(h1.mob)

h1.mob = 77667

h1.age = 48

h1.noOfMovies= 55
h1.noOfHits= 25

h2=h1
h3=h2

print(h3.name)
print(h2.age)
print(h1.height)
print(h2.mob)
print(h3.noOfMovies)
print(h2.noOfHits)

h3.act()
h1.dance()
                 