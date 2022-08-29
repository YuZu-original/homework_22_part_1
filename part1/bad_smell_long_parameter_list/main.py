# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field: object, x_coord: int, y_coord: int, state: str = "idle", speed: int = 1) -> None:
        self.field = field
        self.x = x_coord
        self.y = y_coord
        self.state = state
        self.speed = speed
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value: str):
        self._state = value
        self.speed = self._get_speed_by_state()
    
    
    def _get_speed_by_state(self):
        return {
            "idle": 1,
            "fly": 1.2,
            "crawl": 0.5
            }.get(self.state, 1)
    
    
    def move(self, direction: str):
        directions = { # x, y
            "UP":      (0, 1),
            "DOWN":    (0, -1),
            "LEFT":    (-1, 0),
            "RIGHT":   (1, 0),
        }
        
        dir_x, dir_y = directions.get(direction, (0, 0))

        self.x += dir_x * self.speed
        self.y += dir_y * self.speed
        
        self.field.set_unit(x=self.x, y=self.x, unit=self)


