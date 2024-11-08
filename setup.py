from setuptools import setup

setup(
   name='dsss_homework_2',
#    version='1.0',
   description='Exercise 02 module',
   author='Mohit Yadav',
   author_email='mohit.yadav@fau.de',
   packages=['math_quiz'],  #same as name
   install_requires=['numpy', 'pandas'], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)