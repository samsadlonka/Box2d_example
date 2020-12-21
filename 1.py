"""
shape = 'форма двумерный геометрический объект'
rigid_body = 'не изменяет своих размеров при взаимодействии'
fixture = 'приспособление, связывает форму и тело, добовляя разные физ свойства'
joint = 'совмещение, соединение'
world = 'мир'
"""

from Box2D.examples.framework import Framework
from Box2D import *


class Example(Framework):
    def __init__(self):
        super(Example, self).__init__()

        self.world.CreateBody(shapes=b2LoopShape(
            vertices=[(20, 0), (20, 40), (-20, 40), (-20, 0)]
        ))
        circle = b2FixtureDef(
            shape=b2CircleShape(radius=3), density=1,
            friction=1.0, restitution=0.5
        )
        self.world.CreateBody(
            type=b2_dynamicBody, position=b2Vec2(0, 30),
            fixtures=circle, linearVelocity=(5, 0)
        )

    def Step(self, settings):
        super(Example, self).Step(settings)


if __name__ == '__main__':
    Example().run()
