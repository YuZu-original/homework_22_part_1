class Unit:
    def move(self, field: object, x: int, y: int, direction: str, is_flying: bool = False, is_crawling: bool = False, speed: int = 1):
        
        if is_flying and is_crawling:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_flying:
            speed *= 1.2
        if is_crawling:
            speed *= 0.5
        
        directions = {
            "UP":      (0, 1),
            "DOWN":    (0, -1),
            "LEFT":    (-1, 0),
            "RIGHT":   (1, 0),
        }
        
        dir_x, dir_y = directions.get(direction, (0, 0))

        x += dir_x * speed
        y += dir_y * speed
        
        field.set_unit(x=x, y=x, unit=self)


