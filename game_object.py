
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None

    def render(self, canvas):
        width = self.image.get_width()
        height = self.image.get_height()
        render_pos = (self.x - width / 2, self.y - height / 2)
        canvas.blit(self.image, render_pos)

    def update(self):
        pass

all_character = []

def add(new_character):
    all_character.append(new_character)
def update():
    for c in all_character:
        c.update()

def render(canvas):
    for c in all_character:
        c.render(canvas)

