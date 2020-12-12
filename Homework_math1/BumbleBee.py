class BumbleBee:
    _x_coord = 0
    _direction = True
    _distance = 0
    def __init__(self, speed: int):
        self.speed = speed

    def reverse(self):
        if self._direction:
            self._direction = False
        else:
            self._direction = True

    def fly(self, train):
        time = abs(self._x_coord - train.x_coord) / (self.speed + abs(train.speed))
        self._distance += self.speed * time
        train.x_coord += train.speed * time
        if self._direction:
            self._x_coord += self.speed * time
        else:
            self._x_coord -= self.speed * time
        self.reverse()
        return time


class Train():
    def __init__(self, x_coord: int, speed):
        self.x_coord = x_coord
        self.speed = speed

    def go(self, time):
        self.x_coord += self.speed * time


if __name__ == '__main__':
    def change_curr(curr):
        if curr == train1:
            return train2
        return train1


    bumblebee = BumbleBee(90)
    train1 = Train(0, 50)
    train2 = Train(100, -50)

    curr_train = train1
    not_curr = train2
    while train1.x_coord != train2.x_coord:
        curr_train = change_curr(curr_train)
        not_curr = change_curr(not_curr)
        not_curr.go(bumblebee.fly(curr_train))
        print(f'Текущая пройденная дистанция {bumblebee._distance} километров')

    print(f'{bumblebee._distance} километров пролетел шмель')
