import pyglet, math
from pyglet.window import key
from game import physicalobject, resources

class Player(physicalobject.PhysicalObject):
      
      def __init__(self, *args, **kwargs):
          super(Player, self).__init__(img=resources.car_image, *args, **kwargs)
          self.thrust = 2000.0
          self.rotate_speed = 200.0
          self.key_handler = key.KeyStateHandler()
          
      def update(self, dt):
          super(Player, self).update(dt)
          #self.radians = 90 - self.rotation
          #angle_radians = math.radians(self.radians)
          #print(self.rotation)
          #force_x = math.cos(angle_radians) * self.thrust * dt
          #force_y = math.sin(angle_radians) * self.thrust * dt
          #print(force_x)
          #print(force_y)
          #self.velocity_x = force_x
          #self.velocity_y = force_y
          if self.key_handler[key.LEFT]:
             self.rotation -= self.rotate_speed * dt
          if self.key_handler[key.RIGHT]:
             self.rotation += self.rotate_speed * dt
        
          if self.key_handler[key.UP]:
             self.radians = 90 - self.rotation
             angle_radians = math.radians(self.radians)
             #print(self.rotation)
             force_x = math.cos(angle_radians) * self.thrust * dt
             force_y = math.sin(angle_radians) * self.thrust * dt
             self.velocity_x = force_x
             self.velocity_y = force_y
          
          else: 
             self.velocity_x = 0.0
             self.velocity_y = 0.0

      def contact(self):
          self.radians = 90 - self.rotation
          angle_radians = math.radians(self.radians)
          self.con = abs(math.cos(angle_radians) * self.image.height/2)
          self.son = abs(math.sin(angle_radians) * self.image.height/2)
      
       