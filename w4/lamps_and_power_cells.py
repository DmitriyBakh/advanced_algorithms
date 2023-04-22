""" There's a long line with n lamps and n power cells on it. Each lamp has a power cord of length cord_len. Is it possible to connect each lamp to a power cell? Each power cell can feed at most 1 lamp and must be not longer than cord_len from it.

Please implement the function def solve( lamps: 'List[float]', cells: 'List[float]', cord_len: float, ) -> bool: returning True if and only if it is possible to power all the lamps.

Warning! Function must have name and arguments exactly as described above.

Example: lamps = [1, 3.5, 8] cells = [2, 10, 4] cord_len = 2 Let's connect it like this: lamps[0]<->cells[0], lamps[1]<->cells[2], lamps[2]<->cells[1]. Which will require cord lengths correspondingly: abs(1 - 2)=1, abs(3.5-4)=0.5, abs(8-10)=2. So the longest cord required is 2 which is <= cord_len. So the answer is True.

Example: lamps = [1, 3.5, 8] cells = [2, 10, 4] cord_len = 1 There's no way to connect the lamps so that in every pair the distance is <= cord_len. So the answer is False. """

#solve with greedy algorithm

def solve(lamps, cells, cord_len):
    lamps.sort()
    cells.sort()
    for i in range(len(lamps)):
        if abs(lamps[i] - cells[i]) > cord_len:
            return False
    return True

print(solve([1, 3.5, 8], [2, 10, 4], 2))
print(solve([1, 3.5, 8], [2, 10, 4], 1))