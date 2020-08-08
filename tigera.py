from array import *

class TrainRide:
	def __init__(self):
		self.station= [1,2,3,4,5]
		self.seats = [1,2,3,4,5,6,7,8,9]
		self.reserved = {}

	def findAvailableSeats(self, start, end):
		for seat, station in self.reserved.items():
			if str(start) == station:
				self.seats.append(seat)
				del self.reserved[seat]

		if self.seats:
			seat = self.seats.pop(0)
			print(self.seats)
			self.reserved[str(seat)] = str(end)
			return seat

		return "No Seats available!"




def main():
	tr = TrainRide()
	seat = tr.findAvailableSeats(1,2)
	print("Available Seat: ",seat)
	seat = tr.findAvailableSeats(1,2)
	print("Available Seat: ",seat)
	seat = tr.findAvailableSeats(2,4)
	print("Available Seat: ",seat)

if __name__ == "__main__":
	main()