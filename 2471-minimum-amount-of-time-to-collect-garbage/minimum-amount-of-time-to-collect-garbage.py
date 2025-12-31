class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #creating a travel_time to initialize the time when it is in intital position
        travel_time=[0]
        travel_time.extend(travel)

        #creating distance to calculate the distance time for each garbage
        distance=[travel_time[0]]
        for i in range(1,len(travel_time)):
            distance.append(distance[i-1]+travel_time[i])
        
        #below 3 variables used to found their highest index of type of garbage that exists
        metal=paper=glass=0
        for j in range(len(garbage)):
            if 'M' in garbage[j]:
                metal=j
            if 'P' in garbage[j]:
                paper=j
            if 'G' in garbage[j]:
                glass=j

        #total_garbage_count finds the total number of garbages of all types
        total_garbage_count=len("".join(garbage))
        time=total_garbage_count+distance[metal]+distance[paper]+distance[glass]
        return time