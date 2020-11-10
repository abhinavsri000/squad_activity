import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parking_project",
    version="0.0.1",
    author="Abhinav Srivastava",
    author_email="abhinavsri000@gmail.com",
    description="Package for parking management ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhinavsri000/squad_activity",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
