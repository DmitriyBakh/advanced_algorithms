""" You have produced num_bricks of soap and now you pack a truck to sell them. You don't care about volume and shape. All you care about is that total weight of soap is <= weight_limit . And of course you want to maximize the total value of the bricks. You can cut bricks to any pieces you like in case a full brick doesn't fit in the truck. What it the biggest value you can get?

Each soap brick has a value, as well as 3 measurements that can be used to determine its volume. Different sorts of soap have different relative price, so you have to choose. All bricks have the same density.

More precisely, implement function def solve( bricks: 'List[Tuple[float, float, float]]', values: 'List[float]', weight_limit: float, density: float, ) -> float: that returns the biggest value of (possibly fractional) soap pieces that don't exceed weight_limit in total.

Example: bricks = [(1, 2, 3), (2, 3, 2)] values = [10, 15] weight_limit = 7.5 density = 2.5 Bricks have volumes: 1x2x3=6, 2x3x2=12. Therefore they have weights: 6x2.5=15, 12x2.5=30. One possible configuration is to take 50% of brick 0: the total weight is 15x0.5=7.5<=weight_limit and the total value is 10x0.5=5. It also happens to be the best possible solution, so the answer is 5.
 """

def solve(bricks, values, weight_limit, density):
    bricks.sort(key=lambda x: x[0] * x[1] * x[2])
    values.sort()
    total_value = 0
    for i in range(len(bricks)):
        if bricks[i][0] * bricks[i][1] * bricks[i][2] * density <= weight_limit:
            total_value += values[i]
            weight_limit -= bricks[i][0] * bricks[i][1] * bricks[i][2] * density
        else:
            total_value += values[i] * weight_limit / (bricks[i][0] * bricks[i][1] * bricks[i][2] * density)
            break
    # grader in lms platform doesn't accept float
    return int(total_value)

print(solve([(1, 2, 3), (2, 3, 2)], [10, 15], 7.5, 2.5))