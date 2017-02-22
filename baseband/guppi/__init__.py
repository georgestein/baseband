# Licensed under the GPLv3 - see LICENSE.rst
"""GUPPI baseband data reader.
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .base import open
from .header import GUPPIHeader
from .payload import GUPPIPayload
from .frame import GUPPIFrame
