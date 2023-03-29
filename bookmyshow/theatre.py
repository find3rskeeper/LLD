from show import Show
from collections import defaultdict
from screen import Screen

class Theatre:
    def __init__(self, name, location) -> None:
        self.location = location
        self.name = name
        self.screens = []
        self.screenCount = 0
        self.shows = defaultdict(list)

    def addScreens(self, screenCount, seatNos):
        for i in range(self.screenCount, self.screenCount + screenCount):
            self.screens.append(Screen(i, seatNos))
        
        return

    def addShow(self, showDetails):
        movieName = showDetails['movie'].name
        screen = self.getFreeScreen(movieName, showDetails['startTime'], showDetails['endTime'])
        show = Show(showDetails['movie'], showDetails['startTime'], showDetails['endTime'], screen, showDetails['price'])
        self.shows[movieName].append(show)
        return True

    def hasMovie(self, moviename):
        return moviename in self.shows.keys()
    
    def bookSeatsInShow(self, moviename, showStartTime, showEndTime, seatNos):
        show = self.getShow(moviename, showStartTime, showEndTime)
        return show.bookSeats(seatNos)
    
    def getFreeScreen(self, moviename, startTime, endTime):
        return self.screens[0]
    
    def getShow(self, moviename, showStartTime, showEndTime):
        return self.shows[moviename][0]