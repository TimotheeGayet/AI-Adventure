class Character:
    def __init__(self, name, body_state):
        self.name = name
        self.body_state = body_state

    def take_damage(self, damage):
        self.body_state -= damage