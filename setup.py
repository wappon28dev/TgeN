from setuptools import setup

setup(
    name="TgeN",
    version="0.0.1",
    install_requires=[
        "questionary",
        "tqdm",
        "termcolor",
    ],
    packages=["module"],
    entry_points={
        "console_scripts": [
            "tgen=module.main:main",
            "tn=module.main:main",
        ],
    },
)
