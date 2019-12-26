from distutils.core import setup

setup(
    name='raspi-device-mocks',
    version='0.0.1',    
    description='Mock libraries for low-level device interfaces for Raspberry Pi',
    long_description = open('README.md').read(),
    keywords         = 'Raspberry Pi Mocks',
    url='https://github.com/iva2k/raspi-device-mocks',
    author='iva2k',
    author_email='iva2k@yahoo.com',
    license='GNU',
    packages=['rpidevmocks'],
    install_requires=[
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Home Automation',
        'Topic :: System :: Hardware',
    ],
)
