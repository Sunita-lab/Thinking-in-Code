class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        items = []
        for i in range (len(boxTypes)):
            items.append([boxTypes[i][0], boxTypes[i][0]*boxTypes[i][1]])
        items.sort(key=lambda x: x[1]/x[0], reverse=True)
        i = 0
        maximum = 0

        while truckSize > 0 and i < len(items):
            if items[i][0] <= truckSize:
                maximum += items[i][1]
                truckSize -= items[i][0]
            else:
                maximum += truckSize * (items[i][1]/items[i][0])   
                truckSize -= truckSize
            i += 1    
        return int(maximum)        


        