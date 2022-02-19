import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="receptorMaps",
    version="0.0.0",
    author="Sean S. Darcy",
    author_email="sdarcy2@jhu.edu",
    description="Receptor density maps in fslr_32k for JH CPCR use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "scipy", "rich"],
    include_package_data=True,
    python_requires=">=3.9",
)