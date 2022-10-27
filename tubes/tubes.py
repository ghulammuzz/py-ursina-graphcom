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
  rotation= (150, -10,6),
  scale = (0.2, 0.2, 1.5)
)
# terrain = Entity(
#     model = 'plane',
#     scale = 100,
#     texture = 'grass',
#     collider = 'mesh',
#     position = (0,-10,0)
# )
# street = Entity(
#   model="cube",
#   collider="box",
#   position=(-7, -10.2, 20),
#   scale=(50.,1,8),
#   rotation=(0,0,0),
# 	texture="brick",
#   texture_scale=(5,5),
#   color=color.rgb(255, 128, 0)
# )

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
for n in range(25):
  for k in range(25):
    box = Button(
      position=(k, -8, n),
      color=color.orange,
      highlight_color=color.lime,
      model='cube',
      texture='grass',
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


# human1 = Entity(
#     model = 'cube',
#     scale = 1,
#     texture = 'BG2.png',
#     position = (5, -8, 0)
# )
app.run()