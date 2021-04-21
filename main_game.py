#main_game.py

from room import Room


def main_game():
	
	
	rooms=[]
	rooms.append(Room(0,'Starting Area', 'an empty room',-1,1,2,-1,[]))
	rooms.append(Room(1,'Intersection','an intersection',0,3,1,-1,[]))
	rooms.append(Room(2,'Chest Room','a room with a chest',0,3,2,-1,[]))
	rooms.append(Room(3,'Final Room','a room',1,2,-1,-1,[]))

	
	
	
	location=0
	done=False
	while not done:
		print("You are in {0}.".format(rooms[location].description))
		answer=input('? ')
		if answer.lower()=="north" or answer.lower()=="n":
			if rooms[location].north !=-1:
				location = rooms[location].north
			else:
				print('You cannot go in that direction!')
				print()
		elif answer.lower()=="south" or answer.lower()=="s":
			if rooms[location].south !=-1:
				location = rooms[location].south
			else:
				print('You cannot go in that direction!')
				print()
		elif answer.lower()=="east" or answer.lower()=="e":
			if rooms[location].east !=-1:
				location = rooms[location].east
			else:
				print('You cannot go in that direction!')
				print()
		elif answer.lower()=="west" or answer.lower()=="w":
			if rooms[location].west !=-1:
				location = rooms[location].west
			else:
				print('You cannot go in that direction!')
				print()
		else:
			print('I don''t know how to do that!')
			print()
            
            
main_game()
