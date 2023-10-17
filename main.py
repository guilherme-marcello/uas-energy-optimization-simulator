from worlds import World2

world = World2()


for i in range(6):
    world.advance(verbose=True)
    print(world.UAVS)

world.switch(
    world.uav_A,
    world.uav_C
)

for i in range(2):
    world.advance(verbose=True)
    print(world.UAVS)
