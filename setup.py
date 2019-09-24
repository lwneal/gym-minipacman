from setuptools import setup

setup(name='gym_minipacman',
      version='0.0.1',
      install_requires=['gym',
                        'numpy'],
      packages=[
          "gym_minipacman",
          "gym_minipacman/envs",
      ],
)
