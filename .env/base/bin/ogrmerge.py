#!/home/tobi/Desktop/gis/sandox/notebook/.env/base/bin/python3

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.ogrmerge as a convenience to use as a script
from osgeo_utils.ogrmerge import *  # noqa
from osgeo_utils.ogrmerge import main

deprecation_warn("ogrmerge")
sys.exit(main(sys.argv))
