import pyglet

def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

car_image = pyglet.resource.image("timg.png")
center_image(car_image)

