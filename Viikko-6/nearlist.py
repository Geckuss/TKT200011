class NearList:
    def __init__(self, t):
        self.t = sorted(t)

    def find(self, x):
        # Binary search
        left, right = 0, len(self.t) - 1
        while left < right:
            mid = (left + right) // 2
            if self.t[mid] < x:
                left = mid + 1
            else:
                right = mid
        # Check if the previous number is closer
        if left == 0:
            return self.t[0]
        if left == len(self.t):
            return self.t[-1]
        before, after = self.t[left - 1], self.t[left]
        if x - before <= after - x:
            return before
        return after