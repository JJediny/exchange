# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 Boundless Spatial
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import os
from distutils.core import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

docs_requires = [
    "mkdocs==0.15.3"
]

setup(
    name="exchange",
    version=__import__('exchange').get_version(),
    author="Boundless Spatial",
    author_email="contact@boundlessgeo.com",
    description="Exchange, a platform for geospatial collaboration",
    long_description=(read('README.md')),
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="exchange geonode django",
    url='https://github.com/boundlessgeo/exchange',
    packages=['exchange', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # see requirements.txt
    ],
    extras_require={
        'docs': docs_requires
    },
)
