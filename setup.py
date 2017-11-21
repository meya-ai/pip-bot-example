from setuptools import setup

VERSION = '1.0.0'

description = (
    'Include common bot functionality via custom Python packages.'
)

install_requires = []

packages = [
    'utilities'
]


setup(
    name='pip-bot-example',
    version=VERSION,
    description=description,
    url='https://github.com/meya-ai/pip-bot-example',
    author='Meya.ai',
    author_email='support@meya.ai',
    license='None',
    packages=packages,
    install_requires=install_requires,
    zip_safe=False)
