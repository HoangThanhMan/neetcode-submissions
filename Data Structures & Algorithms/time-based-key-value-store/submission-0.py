class TimeMap:

    def __init__(self):
        self.set_tmap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.set_tmap:
            self.set_tmap[key] = []
        self.set_tmap[key].append((value, int(timestamp)))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.set_tmap or len(self.set_tmap[key]) == 0:
            return ""

        arr = self.set_tmap[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            if arr[m][1] == timestamp:
                return arr[m][0]
            if arr[m][1] < timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
