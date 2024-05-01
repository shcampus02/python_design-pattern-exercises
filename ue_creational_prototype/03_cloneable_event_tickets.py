# Implement an EventTicket class that can be cloned with modifications for seat numbers while keeping other event
# details unchanged.





if __name__ == '__main__':
    event_ticket = EventTicket("Concert", "2024-07-04", "A1")
    print(event_ticket)  # Concert on 2024-07-04, Seat: A1

    cloned_ticket = event_ticket.clone()
    cloned_ticket.set_seat("A2")
    print(event_ticket)   # Should still print: Concert on 2024-07-04, Seat: A1
    print(cloned_ticket)  # Should print: Concert on 2024-07-04, Seat: A2
