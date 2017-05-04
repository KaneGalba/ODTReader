from setuptools import setup, find_packages
 
setup(
    name='ODTReader',
    version='0.0.2',
    url='https://github.com/KaneGalba/ODTReader/',
    download_url='https://github.com/KaneGalba/ODTReader/archive/master.zip',
    author='Kane Galba',
    author_email='kane@galba.co',
    description='Lightweight python module to allow extracting text from OpenDocument (odt) files.',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='GPL',
    install_requires=[],
)
