import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swissweather",
    version="0.2.4",
    author="Dennis Staiger",
    author_email="dnsstaiger@gmx.net",
    description="SRF Meteo weather forecast in Switzerland",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davosian/swissweather",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
          'requests',
          'oauthlib',
          'requests_oauthlib',
          'aiohttp'
      ],
    python_requires='>=3.8',
)