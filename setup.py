from distutils.core import setup

with open("./typedllm/version.py") as f:
    VERSION = f.read().split("=")[1].strip().strip('"')

setup(
    name="typedllm",
    version=VERSION,
    description="Large Language Model to Typed Dataclass Conversion",
    author="Sean Kruzel, ClosedLoop Technologies, LLC",
    author_email="sean@closedloop.tech",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    package_data={
        "": ["*.txt", "*.rst", "*.md", "*.csv"],
    },
    packages=["typedllm"],
)
