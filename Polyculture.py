clear()
memory = {}

# Function to handle tilling/untilling
def Plant(crop):
	if crop == Entities.Grass:
		if get_ground_type() == Grounds.Soil:
			till()
	else:
		if get_ground_type() == Grounds.Grassland:
			till()
	plant(crop)
# Mostly tested with max upgrades, may need some tweaking for other situations
# Smaller farms might need a higher water level, or a can_harvest() check
def Poly(crop):
	for i in range(max_drones()):
		def Handler(offset=i):
			for _ in range(offset):
				move(East)
			global memory
			while True:
				pos = (get_pos_x(), get_pos_y())
				harvest()
				if pos in memory:
					Plant(memory.pop(pos))
				else:
					Plant(crop)
				comp = get_companion()
				if comp:
					ctype, cord = comp
					memory[cord] = ctype
				if get_water() < 0.25:
					use_item(Items.Water)
				move(North)
				if pos[1] == 0:
					move(East)
		spawn_drone(Handler)
	Handler(i)
