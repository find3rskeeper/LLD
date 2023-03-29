class City:
    def __init__(self, name, location, theatres) -> None:
        self.name = name
        self.location = location
        self.theatres = {}
        for theatre in theatres:
            self.theatres[theatre.name] = theatre
    
    def giveTheatres(self, moviename):
        theatres = []
        for theatrename in self.theatres:
            theatre = self.theatres[theatrename]
            if theatre.hasMovie(moviename):
                theatres.append(theatre)

        return theatres
    
    def bookTicket(self, moviename, theatrename, seatNos):
        if theatrename not in self.theatres or not self.theatres[theatrename].hasMovie(moviename):
            return 'No Screening Available on this theatre'
        
        return self.theatres[theatrename].bookSeatsInShow(moviename, 1, 5, seatNos)

