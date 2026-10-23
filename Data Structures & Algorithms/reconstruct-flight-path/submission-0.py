class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flight_book = defaultdict(list)
        tickets.sort(key= lambda x:  x[1], reverse=True)

        for u, v in tickets:
            flight_book[u].append(v)
        
        itinerary = []

        def fly(loc):
            while flight_book[loc]:
                next_loc = flight_book[loc].pop()
                fly(next_loc)

            itinerary.append(loc)
        
        fly("JFK")
        return itinerary[::-1]
