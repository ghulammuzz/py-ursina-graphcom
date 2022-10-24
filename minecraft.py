from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

daratan = 'assets\wood'
square = 'assets\square'
obj1 = ''

app = Ursina()
Sky()
player = FirstPersonController()
window.fullscreen = False
window.fullscreen_size = (1920, 1080)
arm = Entity(
  parent= camera.ui,
  model= load_model(daratan),
  color= color.brown,
  position= (0.75, -0.6),
  rotation= (150, -10,6),
  scale = (0.2, 0.2, 1.5)
)
def update():
  if held_keys['left mouse']:
    arm.position = (0.6, -0.5)
  elif held_keys['right mouse']:
    arm.position = (0.6, -0.5)
  else:
    arm.position = (0.75, -0.6)

boxes = []

for n in range(12):
  for k in range(12):
    box = Button(
      position=(k, 0, n),
      color=color.orange,
      highlight_color=color.lime,
      model='cube',
      texture=load_texture(square),
      origin_y=0.5,
      parent=scene
    )
    boxes.append(box)
    

def input(key):
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        newBox = Button(
          position=
          box.position + mouse.normal,
          color=color.orange,
          highlight_color=color.lime,
          model='cube',
          texture=
          load_texture('assets\wood'),
          origin_y=0.5,
          parent=scene
        )
        boxes.append(newBox)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)

app.run()