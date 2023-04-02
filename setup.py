from setuptools import find_packages
from setuptools import setup

setup(
    name="qclipboard",
    version="0.1.3",
    license="MIT",
    author="Shoppon",
    author_email="shopppon@gmail.com",
    description="A tool to copy text to clipboard and paste it to the frontmost application.",
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={'': ['*.yaml']},
    include_package_data=True,
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "qclipboard = qclipboard.main:main",
            "qclipboard-provider = qclipboard.provider:main",
        ]
    },
)
