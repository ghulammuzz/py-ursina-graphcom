from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Menyembunyakan FPS Counter dan Exit Button
window.fps_counter.enabled = False
window.exit_button.visible = False

# Membuat suara
punch = Audio('dir/punch', autoplay=False)

blocks = [
    load_texture('dir/grass.png'), # 0
    load_texture('dir/grass.png'), # 1
    load_texture('dir/stone.png'), # 2
    load_texture('dir/gold.png'),  # 3
    load_texture('dir/lava.png'),  # 4
]

block_id = 1

# Membuat fungsi dari inputan keyboard numeric
def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]

# Membuat Entitas Langit
sky = Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('dir/sky.jpg'),
    scale=500,
    double_sided=True
)

# Membuat Entitas Tangan
hand = Entity(
    parent=camera.ui,
    model='dir/block',
    texture=blocks[block_id],
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)
# mouse kiri = menambahkan block
# mouse kanan = menghapus block 
def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        punch.play()
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)

# Membuat kelas Voxel
# modeling block
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='dir/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='dir/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'right mouse down':
                destroy(self)

# Membuat terrain box
for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

# Inisialisasi player
player = FirstPersonController()

app.run()