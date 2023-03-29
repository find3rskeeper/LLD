class User:
    def __init__(self, userId, name, drivingLicence, age, score = None) -> None:
        self.userId = userId
        self.name = name
        self.drivingLicence = drivingLicence
        self.age = age
        self.userScore = score

