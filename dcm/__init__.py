VERSION = "0.1.3"

import os
__DEBUG__ = os.environ.get("DCM_DEBUG", 0)

from dcm.mst import MST

# Data Complexity Measures
from dcm.dcm import F1, N1, C12
