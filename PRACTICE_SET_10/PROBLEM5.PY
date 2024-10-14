# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.
from random import randint
class train:
    def __init__(self,train_no,fro,to,seat_no) -> None:
        self.train_no=train_no
        self.fro=fro
        self.to=to
        self.seat_no=seat_no
    def book(self):
        print(f"Ticket is booked in train no: {self.train_no} from {self.fro} to {self.to}")
    def get_status(self):
        print(f"Your ticket is CONFIRMED and seat number is-{self.seat_no}")
    def get_fare(self):
        print(f"Ticket fare in train no: {self.train_no} from {self.fro} to {self.to} is {randint(222, 5555)}")

train_details=train(453899,"Rampur","Delhi","32B")
train_details.book()
train_details.get_status()
train_details.get_fare()   
