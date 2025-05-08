#################################################################################
# WaterTAP Copyright (c) 2020-2024, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory, Oak Ridge National Laboratory,
# National Renewable Energy Laboratory, and National Energy Technology
# Laboratory (subject to receipt of any required approvals from the U.S. Dept.
# of Energy). All rights reserved.
#
# Please see the files COPYRIGHT.md and LICENSE.md for full copyright and license
# information, respectively. These files are also available online at the URL
# "https://github.com/watertap-org/watertap/"
#################################################################################
"""
Project setup with setuptools
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from pathlib import Path

cwd = Path(__file__).parent
long_description = (cwd / "README.md").read_text()


# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="watertap",
    url="https://github.com/watertap-org/watertap",
    version="1.4.dev0",
    description="WaterTAP modeling library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="NAWI team",
    license="BSD",
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="water systems, chemical engineering, process modeling, filtration, desalination, nawi",
    # just include watertap and everything under it
    packages=find_packages(
        include=("watertap*",),
    ),
    python_requires=">=3.9",
    install_requires=[
        "Click",
        "cookiecutter",
    ],
    package_data={  # Optional
        "": [
            "*.json",
            "*.yaml",
            "*.yml",
            "*.csv",
            "*.png",
        ],
    },
    entry_points={
        "console_scripts": [
            "watertap=watertap.watertap_cli:cli",  # CLI command
        ],
    },
)
