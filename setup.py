from setuptools import setup

setup(
    name="dnstwist",
    version="20200429",
    author="Bryce B",
    author_email="swarvingprogrammer@gmail.com",
    description="Modified version of DNSTWIST. Domain name permutation engine for detecting homograph phishing attacks, typo squatting, and brand impersonation",
    long_description="Original Project website: https://github.com/elceef/dnstwist",
    url="https://github.com/bjb28/dnstwist",
    py_modules=["dnstwist"],
    entry_points={"console_scripts": ["dnstwist=dnstwist:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=[
        "docopt >= 0.6.2",
        "GeoIP>=1.3.2",
        "dnspython>=1.14.0",
        "requests>=2.20.0",
        "schema>=0.7.1",
        "ssdeep>=3.1.1",
        "whois>=0.7",
        "tld>=0.9.1",
        "ipython >= 7.0",
    ],
)
