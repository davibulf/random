from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print(bob)

for i in range(4):
    bob.fd(100)
    lt(bob)

wait_for_user()
