class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f'Flight origin: {self.origin}')
        print(f'Flight destination: {self.destination}')
        print(f'Flight duration: {self.duration}')


def main():

    # Create first flight, print out its information.
    first = Flight(origin='New York', destination='Paris', duration=540)
    first.print_info()

    print('---')

    # Create second flight, print out its information.
    second = Flight(origin='Tokyo', destination='Shanghai', duration=185)
    second.print_info()


if __name__ == '__main__':
    main()
