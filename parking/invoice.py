class Invoice:
    def __init__(self) -> None:
        self.ticketNumber = 0
        self.fee = 0
        self.entryTime = -1
        self.exitTime = -1

    #Basic Function to generate invoice
    def generateInvoice(self, vehicle):
        ticket = vehicle.ticket
        ticketId = ticket.getId()
        licencePlate = vehicle.getLicencePlate()
        inTime = ticket.getIntime()
        invoiceString = """ Parking Ticket:
                                Ticket Number: {ticketId}
                                Vehicle Number: {licencePlate}
                                Entry Date-time: {inTime}
""".format(ticketId=ticketId, licencePlate=licencePlate, inTime=inTime)
        return invoiceString