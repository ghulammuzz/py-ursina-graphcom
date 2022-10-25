from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 

app = Ursina()

player = FirstPersonController()
Sky()

arm = Entity(
  parent= camera.ui,
  model= 'cube',
  color= color.brown,
  position= (0.75, -0.6),
  rotation= (150, -10,6),
  scale = (0.2, 0.2, 1.5)
)
terrain = Entity(
    model = 'plane',
    scale = 100,
    texture = 'grass',
    collider = 'mesh',
    position = (0,-10,0)
)
wall_1=Entity(model="cube", collider="box", position=(-7, -10.2, 20), scale=(50.,1,8), rotation=(0,0,0),
	texture="brick", texture_scale=(5,5), color=color.rgb(255, 128, 0))
object=Entity(model='cube', collider="box", position=(-7, -10, 20), scale=1, rotation=(0,0,0),
	texture="BG2.png", texture_scale=(5,5), color=color.rgb(255, 128, 0))
def update():
  if held_keys['left mouse']:
    arm.position = (0.6, -0.5)
  elif held_keys['right mouse']:
    arm.position = (0.6, -0.5)
  else:
    arm.position = (0.75, -0.6)
    
# human1 = Entity(
#     model = 'cube',
#     scale = 1,
#     texture = 'BG2.png',
#     position = (5, -8, 0)
# )
app.run()