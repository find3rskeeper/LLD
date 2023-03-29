class BookMyShow:
    def __init__(self, cities) -> None:
        for city in cities:
            self.cities[city.name] = city
    
    def findTheatres(self, city, movie):
        return self.cities[city].giveTheatres(movie)
    
    def bookTicket(self, city, movie, theatre, seatNos):
        return self.cities[city].bookTicket(movie, theatre, seatNos)
