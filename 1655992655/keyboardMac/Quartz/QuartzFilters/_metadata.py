# This file is generated by objective.metadata
#
# Last update: Sun Aug  4 21:30:58 2019

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$globalUpdateOK@Z$kQuartzFilterApplicationDomain$kQuartzFilterManagerDidAddFilterNotification$kQuartzFilterManagerDidModifyFilterNotification$kQuartzFilterManagerDidRemoveFilterNotification$kQuartzFilterManagerDidSelectFilterNotification$kQuartzFilterPDFWorkflowDomain$kQuartzFilterPrintingDomain$"""
enums = """$$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"quartzFilterManager:didAddFilter:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"quartzFilterManager:didModifyFilter:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"quartzFilterManager:didRemoveFilter:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"quartzFilterManager:didSelectFilter:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(b"QuartzFilter", b"applyToContext:", {"retval": {"type": b"Z"}})
    r(b"QuartzFilterManager", b"selectFilter:", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
protocols = {
    "QuartzFilterManagerDelegate": objc.informal_protocol(
        "QuartzFilterManagerDelegate",
        [
            objc.selector(
                None, b"quartzFilterManager:didSelectFilter:", b"v@:@@", isRequired=False
            ),
            objc.selector(
                None, b"quartzFilterManager:didAddFilter:", b"v@:@@", isRequired=False
            ),
            objc.selector(
                None, b"quartzFilterManager:didModifyFilter:", b"v@:@@", isRequired=False
            ),
            objc.selector(
                None, b"quartzFilterManager:didRemoveFilter:", b"v@:@@", isRequired=False
            ),
        ],
    )
}
expressions = {}

# END OF FILE
