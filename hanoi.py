def hanoi(level,stick_from,stick_to,step=1):
	if(stick_from>2 or stick_to>2):
		raise ValueError("Sticks should be 0 (left), 1 (center) or 2 (right)")
	elif(stick_from==stick_to):
		print("Game already solved")
	elif(level==1):
		print("({}) Move from {} to {}".format(step,stick_from,stick_to))
		return step+1
	else:	
		step=hanoi(level-1,stick_from,3-stick_from-stick_to,step)
		print("({}) Move from {} to {}".format(step,stick_from,stick_to))
		step=hanoi(level-1,3-stick_from-stick_to,stick_to,step+1)
		return step

hanoi(17,2,1)