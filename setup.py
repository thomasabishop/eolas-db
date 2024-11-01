from setuptools import find_packages, setup

setup(
    name="eolas-db",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["python-frontmatter, "hurry.filesize"],
    entry_points={
        "console_scripts": [
            "run=app:main",
        ],
    },
)
