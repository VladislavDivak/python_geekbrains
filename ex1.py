from time import sleep

class TrafficLight:
    __color = 'Red'

    def running(self):
        while True:
            print('Red')
            sleep(7)
            print('Yellow')
            sleep(2)
            print('Green')
            sleep(4)

traffic = TrafficLight()
traffic.running()
