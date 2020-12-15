class Seat():
    def __init__(self):
        self.occupied = False
        self.next_state_occupied = False
        self.neighbours = []


def getNeighbours(seatMap, posy, posx):
    neighbours = []
    possible = [(posy - 1, posx - 1), (posy - 1, posx), (posy - 1, posx + 1), (posy, posx + 1), (posy + 1, posx + 1), (posy + 1, posx), (posy + 1, posx - 1), (posy, posx - 1)]
    for possible_neighbour in possible:
        if possible_neighbour[0] >= 0 and possible_neighbour[0] < len(seatMap) and possible_neighbour[1] >= 0 and possible_neighbour[1] < len(seatMap[0]) and seatMap[possible_neighbour[0]][possible_neighbour[1]] != None:
            neighbours.append(possible_neighbour)
    
    return neighbours

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

seatMap = []

# Create the seatMap with the seat objects
for line in lines:
    line = line.strip("\n")
    line_in_map = []
    for char in line:
        if char == "L":
            line_in_map.append(Seat())
        else:
            line_in_map.append(None)
    seatMap.append(line_in_map)

# Populate the neighbours list of each seat for faster access
for i in range(len(seatMap)):
    for j in range(len(seatMap[0])):
        if seatMap[i][j] != None:
            seatMap[i][j].neighbours = getNeighbours(seatMap, i, j)

changes = True

while changes:
    changes = False
    for i in range(len(seatMap)):
        for j in range(len(seatMap[0])):
            if seatMap[i][j] != None:
                curr_seat = seatMap[i][j]
                if curr_seat.occupied == False:
                    occupied_adjacent = 0
                    for adj_seat_pos in curr_seat.neighbours:
                        adj_seat = seatMap[adj_seat_pos[0]][adj_seat_pos[1]]
                        if adj_seat.occupied:
                            occupied_adjacent += 1
                    if occupied_adjacent == 0:
                        changes = True
                        curr_seat.next_state_occupied = True
                    else:
                        curr_seat.next_state_occupied = False
                else:
                    occupied_adjacent = 0
                    for adj_seat_pos in curr_seat.neighbours:
                        adj_seat = seatMap[adj_seat_pos[0]][adj_seat_pos[1]]
                        if adj_seat.occupied:
                            occupied_adjacent += 1
                    if occupied_adjacent >= 4:
                        changes = True
                        curr_seat.next_state_occupied = False
                    else:
                        curr_seat.next_state_occupied = True

    for i in range(len(seatMap)):
        for j in range(len(seatMap[0])):
            if seatMap[i][j] != None:
                seatMap[i][j].occupied = seatMap[i][j].next_state_occupied

occupiedSeats = 0

for i in range(len(seatMap)):
    for j in range(len(seatMap[0])):
        if seatMap[i][j] != None and seatMap[i][j].occupied == True:
            occupiedSeats += 1

print(occupiedSeats)