class TimeMap:

    def __init__(self):
        self.tmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tmap:
            self.tmap[key].append([timestamp,value])
        else:
            self.tmap[key] = [[timestamp,value]]


        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.tmap:
            bin_search = self.tmap[key]
        else:
            return ""
        l,r = 0, len(bin_search) - 1
        res = []

        while l<=r:
            m = l+((r-l)//2)
            if timestamp > bin_search[m][0]:
                res = max(res, bin_search[m])

            if bin_search[m][0] == timestamp:
                return bin_search[m][1]
            elif timestamp > bin_search[m][0]:
                l = m+1
            else:
                r = m-1
        if res:
            return res[1]
        else:
            return ""

        #[4,7,8,10,12]
        
