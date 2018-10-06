class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

def main():

    # Create flight.
    flight = Flight(origin='New York', destination='Paris', duration=540)

    # Change the value of a variable.
    flight.duration += 10

    # Print details about flight.
    print(flight.origin)
    print(flight.destination)
    print(flight.duration)

if __name__ == '__main__':
    main()
