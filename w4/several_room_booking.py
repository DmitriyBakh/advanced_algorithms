""" This time we need to book several rooms instead of one. The rooms are all the same. Each meeting takes place in a single room and one can begin starting from the ending of another. Slots are given in arbitrary order in form of begin/end pairs denoted in Unix seconds, i.e. ints.

Implement function

def solve(

    begin_end_pairs: 'List[Tuple[int, int]]',

    num_rooms: int,

) -> int:

returning the largest number of slots that can be distributed among the rooms so no conflicts happen.

Example (say it's 1 Jan 1970 so Unix seconds are small ints):

begin_end_pairs = [(0, 10), (15, 25), (10, 25), (5, 30)]

num_rooms = 2

then slots 0, 2 go to room 1 and slot 1 goes to room 2. This solution is the best and it uses 3 slots. So the answer is 3. """

def solve(begin_end_pairs, num_rooms):
    begin_end_pairs.sort(key=lambda x: x[0])
    rooms = []
    for i in range(num_rooms):
        rooms.append([])
    for i in range(len(begin_end_pairs)):
        for j in range(len(rooms)):
            if not rooms[j]:
                rooms[j].append(begin_end_pairs[i])
                break
            else:
                if begin_end_pairs[i][0] >= rooms[j][-1][1]:
                    rooms[j].append(begin_end_pairs[i])
                    break
    return sum([len(room) for room in rooms])

print(solve([(0, 10), (15, 25), (10, 25), (5, 30)], 2))