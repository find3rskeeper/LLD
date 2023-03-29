from theatre import *
from movie import Movie
from city import City
movie = Movie('1947')
pvrPV = Theatre('PVR Prashant Vihar', 'Delhi')
pvrPV.addScreens(5, 50)
pvrPV.addShow({'movie': movie, 'startTime': 1, 'endTime': 7, 'price': 100})
city = City('Delhi', 'Delhi', [pvrPV])
city.bookTicket('1947', 'PVR Prashant Vihar', [1,2])