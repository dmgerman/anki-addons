"""
Python mapping for the QuartzCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys
import objc
import Foundation

from Quartz.QuartzFilters import _metadata

sys.modules["Quartz.QuartzFilters"] = mod = objc.ObjCLazyModule(
    "Quartz.QuartzFilters",
    "com.apple.quartzfilters",
    objc.pathForFramework(
        "/System/Library/Frameworks/Quartz.framework/Frameworks/QuartzFilters.framework"
    ),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (Foundation,),
)

import sys

del sys.modules["Quartz.QuartzFilters._metadata"]
