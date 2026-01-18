def Greedy_Bones():
	ws = get_world_size()
	body_size = ws * ws
	stop = body_size // 2

  	# O(1) tracking for body position
	head = 0
	tail = 0
	length = 0
	# Initialize circular buffer for body
    	body = []
    	for _ in range(body_size):
        	body.append(None)

	# Get initial target apple
	t = measure()
	tx, ty = t

	while length < stop:
		x = get_pos_x()
		y = get_pos_y()

		# Parity-based movement
		if x % 2 == 0:
			if y % 2 == 0:
				if ty < y:
					if not move(South):
						move(East)
				else:
					if not move(East):
						move(South)
			else:
				if tx < x:
					if not move(West):
						move(South)
				else:
					if not move(South):
						move(West)
		else:
			if y % 2 == 0:
				if tx > x:
					if not move(East):
						move(North)
				else:
					if not move(North):
						move(East)
			else:
				if ty > y:
					if not move(North):
						move(West)
				else:
					if not move(West):
						move(North)

		# Update snake body in circular buffer
		cx = get_pos_x()
		cy = get_pos_y()
		body[head] = (cx, cy)
		head += 1
		if head >= body_size:
			head = 0

		# Check if apple was collected
		t = measure()
		if t:
			tx, ty = t
			snake_length += 1
		else:
			tail += 1
			if tail >= body_size:
				tail = 0

	return body, head, tail
