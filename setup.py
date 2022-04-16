from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Loja_Bicicleta",
    version="0.0.1",
    author="Celso Romero",
    author_email="celsobrf@msn.com",
    description="Pacote para implementar uma loja de Bicicleta",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/celsobrf"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)