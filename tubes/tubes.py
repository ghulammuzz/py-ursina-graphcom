from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

Sky()

tanah = Entity(
	model= 'plane',
	scale=100,
	texture='grass',
	collider='mesh',
	position=(0, -10, 0)
)

app.run()