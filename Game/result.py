class Result:
    """A Sample Result Class"""

    def __init__(self, p1, p2, p1_wins, p2_wins, draw):
        self.p1 = p1
        self.p2 = p2
        self.p1_wins = p1_wins
        self.p2_wins = p2_wins
        self.draw = draw

    def __repr__(self):
        return "Employee('{}', '{}', {}, {}, {})".format(self.p1, self.p2, self.p1, self.p2_wins, self.draw)
