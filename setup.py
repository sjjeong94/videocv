from setuptools import setup, find_packages

setup(
    name='videocv',
    packages=find_packages(),
    version='0.1.4',
    license='MIT',
    description='Video & OpenCV',
    author='sjjeong94',
    author_email='sjjeong94@gmail.com',
    url='https://github.com/sjjeong94/videocv',
    install_requires=['opencv-python'],
)
