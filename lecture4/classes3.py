class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f'Flight origin: {self.origin}')
        print(f'Flight destination: {self.destination}')
        print(f'Flight duration: {self.duration}')

    def delay(self, amount):
        self.duration += amount


def main():

    # Create flight, print out its information.
    flight = Flight(origin='New York', destination='Paris', duration=540)
    flight.print_info()

    # Delay the flight, then re-print the information.
    flight.delay(10)
    flight.print_info()


if __name__ == '__main__':
    main()
