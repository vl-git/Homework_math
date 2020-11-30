class Snail():
    _y_location = 0
    _finished = False
    _days_spent = 0
    _nights_spent = 0
    def __init__(self, day_speed: int, night_speed: int):
        self.day_speed = day_speed
        self.night_speed = night_speed

    def climb(self, distance):
        while self._y_location < distance:
            self._y_location += self.day_speed
            self._days_spent += 1
            if self._y_location >= distance:
                self._finished = True
                break
            self._y_location += self.night_speed
            self._nights_spent += 1


    def status(self):
        if self._finished:
            return 'Got the candy!'
        return 'Have not got the candy yet :('

    def __str__(self):
        return f'Little snail\n' \
               f'Already climbs for {self._days_spent} days and {self._nights_spent} nights \n' \
               f'{self.status()}'


if __name__ == '__main__':
    snail = Snail(3, -2)
    print(snail)
    print()
    snail.climb(1000)
    print(snail)
