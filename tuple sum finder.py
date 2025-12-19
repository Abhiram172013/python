class TupleSumFinder:
    def __init__(self, data):
        self.data = data

    def find_positions(self, target_sum):
        result = []
        n = len(self.data)

        for i in range(n):
            for j in range(i + 1, n):
                if self.data[i] + self.data[j] == target_sum:
                    result.append((i, j))

        return result
t = (10, 20, 30, 40, 50, 60, 70, 80, 90)
finder = TupleSumFinder(t)
target = int(input("Enter the sum: "))
positions = finder.find_positions(target)
if positions:
    print("Pairs of positions whose values add up to the sum:")
    for pos in positions:
        print(pos)
else:
    print("No pairs found.")
