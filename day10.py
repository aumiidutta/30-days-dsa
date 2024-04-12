class Solution:
    def insert(self, interval, Interval):
        n = len(interval)
        res = []
        i = 0

        while (i<n) and (interval[i].end<Interval.start):
            res.append(interval[i])
            i += 1

        while (i<n) and (interval[i].start<=Interval.end):
            Interval.start = min(interval[i].start, Interval.start)
            Interval.end = max(interval[i].end, Interval.end)
            i += 1
        res.append(Interval)

        while i<n:
            res.append(interval[i])
            i += 1

        return res
