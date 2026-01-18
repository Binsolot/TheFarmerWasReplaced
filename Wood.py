import Fn

# Crude wood script which works well with max upgrades.
# Needs refinement to work well in other conditions
def Wood():
    for i in range(max_drones()):
        def Handler(offset=i):
            for _ in range(offset):
                move(East)
                move(North)
            while True:
                harvest()
                plant(Entities.Tree)
                if get_water() < 0.2:
					use_item(Items.Water)
                move(North)
                harvest()
                plant(Entities.Bush)
                move(North)
        spawn_drone(Handler())
    Handler()
