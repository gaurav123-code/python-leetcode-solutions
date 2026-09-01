class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.d = 0

        self.dir = ["East", "North", "West", "South"]

        self.total = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        num %= self.total

        # Special case:
        # A complete cycle from (0,0) ends at (0,0) facing South.
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.d = 3
            return

        while num > 0:

            if self.d == 0:  # East
                move = min(num, self.w - 1 - self.x)
                self.x += move
                num -= move

                if num > 0:
                    self.d = 1

            elif self.d == 1:  # North
                move = min(num, self.h - 1 - self.y)
                self.y += move
                num -= move

                if num > 0:
                    self.d = 2

            elif self.d == 2:  # West
                move = min(num, self.x)
                self.x -= move
                num -= move

                if num > 0:
                    self.d = 3

            else:  # South
                move = min(num, self.y)
                self.y -= move
                num -= move

                if num > 0:
                    self.d = 0

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dir[self.d]