from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 

app = Ursina()

player = FirstPersonController()
player.speed = 5
Sky()


arm = Entity(
  parent= camera.ui,
  model= 'cube',
  color= color.brown,
  position= (0.75, -0.6),
  rotation= (150, -20,6),
  scale = (0.2, 0.2, 1.5)
)

boxes = Button(
  model='cube',
  position=(15, -7.5, 15),
  scale=1,
  rotation=(0,0,0),
	texture="brick",
  texture_scale=(5,5), 
  color=color.rgb(255, 128, 0))

def update():
  if held_keys['left mouse']:
    arm.position = (0.6, -0.5)
  elif held_keys['right mouse']:
    arm.position = (0.6, -0.5)
  else:
    arm.position = (0.75, -0.6)

boxes = []
for n in range(10):
  for k in range(10):
    box = Button(
      position=(k, -10, n),
      color=color.orange,
      highlight_color=color.lime,
      model='cube',
      texture='brick',
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
          texture='brick',
          origin_y=0.5,
          parent=scene
        )
        boxes.append(newBox)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)

app.run()