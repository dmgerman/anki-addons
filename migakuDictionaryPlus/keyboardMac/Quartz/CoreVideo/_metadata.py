# This file is generated by objective.metadata
#
# Last update: Fri Aug  9 18:36:47 2019

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
misc.update(
    {
        "CVTimeStamp": objc.createStructType(
            "CVTimeStamp",
            sel32or64(
                b"{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}",
                b"{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
            ),
            [
                "version",
                "videoTimeScale",
                "videoTime",
                "hostTime",
                "rateScalar",
                "videoRefreshPeriod",
                "smpteTime",
                "flags",
                "reserved",
            ],
        ),
        "CVPlanarPixelBufferInfo_YCbCrBiPlanar": objc.createStructType(
            "CVPlanarPixelBufferInfo_YCbCrBiPlanar",
            b"{CVPlanarPixelBufferInfo_YCbCrBiPlanar={CVPlanarComponentInfo=iI}{CVPlanarComponentInfo=iI}}",
            ["componentInfoY", "componentInfoCbCr"],
        ),
        "CVPlanarPixelBufferInfo_YCbCrPlanar": objc.createStructType(
            "CVPlanarPixelBufferInfo_YCbCrPlanar",
            b"{CVPlanarPixelBufferInfo_YCbCrPlanar={CVPlanarComponentInfo=iI}{CVPlanarComponentInfo=iI}{CVPlanarComponentInfo=iI}}",
            ["componentInfoY", "componentInfoCb", "componentInfoCr"],
        ),
        "CVPlanarComponentInfo": objc.createStructType(
            "CVPlanarComponentInfo", b"{CVPlanarComponentInfo=iI}", ["offset", "rowBytes"]
        ),
        "CVTime": objc.createStructType(
            "CVTime", b"{_CVTime=qii}", ["timeValue", "timeScale", "flags"]
        ),
        "CVSMPTETime": objc.createStructType(
            "CVSMPTETime",
            sel32or64(b"{CVSMPTETime=ssLLLssss}", b"{CVSMPTETime=ssIIIssss}"),
            [
                "subframes",
                "subframeDivisor",
                "counter",
                "type",
                "flags",
                "hours",
                "minutes",
                "seconds",
                "frames",
            ],
        ),
        "CVPlanarPixelBufferInfo": objc.createStructType(
            "CVPlanarPixelBufferInfo",
            b"{CVPlanarPixelBufferInfo=[1{CVPlanarComponentInfo=iI}]}",
            ["componentInfo"],
        ),
    }
)
constants = """$kCVBufferMovieTimeKey@^{__CFString=}$kCVBufferNonPropagatedAttachmentsKey@^{__CFString=}$kCVBufferPropagatedAttachmentsKey@^{__CFString=}$kCVBufferTimeScaleKey@^{__CFString=}$kCVBufferTimeValueKey@^{__CFString=}$kCVImageBufferAlphaChannelIsOpaque@^{__CFString=}$kCVImageBufferAlphaChannelModeKey@^{__CFString=}$kCVImageBufferAlphaChannelMode_PremultipliedAlpha@^{__CFString=}$kCVImageBufferAlphaChannelMode_StraightAlpha@^{__CFString=}$kCVImageBufferCGColorSpaceKey@^{__CFString=}$kCVImageBufferChromaLocationBottomFieldKey@^{__CFString=}$kCVImageBufferChromaLocationTopFieldKey@^{__CFString=}$kCVImageBufferChromaLocation_Bottom@^{__CFString=}$kCVImageBufferChromaLocation_BottomLeft@^{__CFString=}$kCVImageBufferChromaLocation_Center@^{__CFString=}$kCVImageBufferChromaLocation_DV420@^{__CFString=}$kCVImageBufferChromaLocation_Left@^{__CFString=}$kCVImageBufferChromaLocation_Top@^{__CFString=}$kCVImageBufferChromaLocation_TopLeft@^{__CFString=}$kCVImageBufferChromaSubsamplingKey@^{__CFString=}$kCVImageBufferChromaSubsampling_411@^{__CFString=}$kCVImageBufferChromaSubsampling_420@^{__CFString=}$kCVImageBufferChromaSubsampling_422@^{__CFString=}$kCVImageBufferCleanApertureHeightKey@^{__CFString=}$kCVImageBufferCleanApertureHorizontalOffsetKey@^{__CFString=}$kCVImageBufferCleanApertureKey@^{__CFString=}$kCVImageBufferCleanApertureVerticalOffsetKey@^{__CFString=}$kCVImageBufferCleanApertureWidthKey@^{__CFString=}$kCVImageBufferColorPrimariesKey@^{__CFString=}$kCVImageBufferColorPrimaries_DCI_P3@^{__CFString=}$kCVImageBufferColorPrimaries_EBU_3213@^{__CFString=}$kCVImageBufferColorPrimaries_ITU_R_2020@^{__CFString=}$kCVImageBufferColorPrimaries_ITU_R_709_2@^{__CFString=}$kCVImageBufferColorPrimaries_P22@^{__CFString=}$kCVImageBufferColorPrimaries_P3_D65@^{__CFString=}$kCVImageBufferColorPrimaries_SMPTE_C@^{__CFString=}$kCVImageBufferContentLightLevelInfoKey@^{__CFString=}$kCVImageBufferDisplayDimensionsKey@^{__CFString=}$kCVImageBufferDisplayHeightKey@^{__CFString=}$kCVImageBufferDisplayWidthKey@^{__CFString=}$kCVImageBufferFieldCountKey@^{__CFString=}$kCVImageBufferFieldDetailKey@^{__CFString=}$kCVImageBufferFieldDetailSpatialFirstLineEarly@^{__CFString=}$kCVImageBufferFieldDetailSpatialFirstLineLate@^{__CFString=}$kCVImageBufferFieldDetailTemporalBottomFirst@^{__CFString=}$kCVImageBufferFieldDetailTemporalTopFirst@^{__CFString=}$kCVImageBufferGammaLevelKey@^{__CFString=}$kCVImageBufferICCProfileKey@^{__CFString=}$kCVImageBufferMasteringDisplayColorVolumeKey@^{__CFString=}$kCVImageBufferPixelAspectRatioHorizontalSpacingKey@^{__CFString=}$kCVImageBufferPixelAspectRatioKey@^{__CFString=}$kCVImageBufferPixelAspectRatioVerticalSpacingKey@^{__CFString=}$kCVImageBufferPreferredCleanApertureKey@^{__CFString=}$kCVImageBufferTransferFunctionKey@^{__CFString=}$kCVImageBufferTransferFunction_EBU_3213@^{__CFString=}$kCVImageBufferTransferFunction_ITU_R_2020@^{__CFString=}$kCVImageBufferTransferFunction_ITU_R_2100_HLG@^{__CFString=}$kCVImageBufferTransferFunction_ITU_R_709_2@^{__CFString=}$kCVImageBufferTransferFunction_Linear@^{__CFString=}$kCVImageBufferTransferFunction_SMPTE_240M_1995@^{__CFString=}$kCVImageBufferTransferFunction_SMPTE_C@^{__CFString=}$kCVImageBufferTransferFunction_SMPTE_ST_2084_PQ@^{__CFString=}$kCVImageBufferTransferFunction_SMPTE_ST_428_1@^{__CFString=}$kCVImageBufferTransferFunction_UseGamma@^{__CFString=}$kCVImageBufferTransferFunction_sRGB@^{__CFString=}$kCVImageBufferYCbCrMatrixKey@^{__CFString=}$kCVImageBufferYCbCrMatrix_DCI_P3@^{__CFString=}$kCVImageBufferYCbCrMatrix_ITU_R_2020@^{__CFString=}$kCVImageBufferYCbCrMatrix_ITU_R_601_4@^{__CFString=}$kCVImageBufferYCbCrMatrix_ITU_R_709_2@^{__CFString=}$kCVImageBufferYCbCrMatrix_P3_D65@^{__CFString=}$kCVImageBufferYCbCrMatrix_SMPTE_240M_1995@^{__CFString=}$kCVIndefiniteTime@{_CVTime=qii}$kCVMetalTextureCacheMaximumTextureAgeKey@^{__CFString=}$kCVMetalTextureStorageMode@^{__CFString=}$kCVMetalTextureUsage@^{__CFString=}$kCVOpenGLBufferHeight@^{__CFString=}$kCVOpenGLBufferInternalFormat@^{__CFString=}$kCVOpenGLBufferMaximumMipmapLevel@^{__CFString=}$kCVOpenGLBufferPoolMaximumBufferAgeKey@^{__CFString=}$kCVOpenGLBufferPoolMinimumBufferCountKey@^{__CFString=}$kCVOpenGLBufferTarget@^{__CFString=}$kCVOpenGLBufferWidth@^{__CFString=}$kCVOpenGLTextureCacheChromaSamplingModeAutomatic@^{__CFString=}$kCVOpenGLTextureCacheChromaSamplingModeBestPerformance@^{__CFString=}$kCVOpenGLTextureCacheChromaSamplingModeHighestQuality@^{__CFString=}$kCVOpenGLTextureCacheChromaSamplingModeKey@^{__CFString=}$kCVPixelBufferBytesPerRowAlignmentKey@^{__CFString=}$kCVPixelBufferCGBitmapContextCompatibilityKey@^{__CFString=}$kCVPixelBufferCGImageCompatibilityKey@^{__CFString=}$kCVPixelBufferExtendedPixelsBottomKey@^{__CFString=}$kCVPixelBufferExtendedPixelsLeftKey@^{__CFString=}$kCVPixelBufferExtendedPixelsRightKey@^{__CFString=}$kCVPixelBufferExtendedPixelsTopKey@^{__CFString=}$kCVPixelBufferHeightKey@^{__CFString=}$kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey@^{__CFString=}$kCVPixelBufferIOSurfaceOpenGLESFBOCompatibilityKey@^{__CFString=}$kCVPixelBufferIOSurfaceOpenGLESTextureCompatibilityKey@^{__CFString=}$kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey@^{__CFString=}$kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey@^{__CFString=}$kCVPixelBufferIOSurfacePropertiesKey@^{__CFString=}$kCVPixelBufferMemoryAllocatorKey@^{__CFString=}$kCVPixelBufferMetalCompatibilityKey@^{__CFString=}$kCVPixelBufferOpenGLCompatibilityKey@^{__CFString=}$kCVPixelBufferOpenGLESCompatibilityKey@^{__CFString=}$kCVPixelBufferOpenGLESTextureCacheCompatibilityKey@^{__CFString=}$kCVPixelBufferOpenGLTextureCacheCompatibilityKey@^{__CFString=}$kCVPixelBufferPixelFormatTypeKey@^{__CFString=}$kCVPixelBufferPlaneAlignmentKey@^{__CFString=}$kCVPixelBufferPoolAllocationThresholdKey@^{__CFString=}$kCVPixelBufferPoolFlushExcessBuffers$kCVPixelBufferPoolFreeBufferNotification@^{__CFString=}$kCVPixelBufferPoolMaximumBufferAgeKey@^{__CFString=}$kCVPixelBufferPoolMinimumBufferCountKey@^{__CFString=}$kCVPixelBufferWidthKey@^{__CFString=}$kCVPixelFormatBitsPerBlock@^{__CFString=}$kCVPixelFormatBlackBlock@^{__CFString=}$kCVPixelFormatBlockHeight@^{__CFString=}$kCVPixelFormatBlockHorizontalAlignment@^{__CFString=}$kCVPixelFormatBlockVerticalAlignment@^{__CFString=}$kCVPixelFormatBlockWidth@^{__CFString=}$kCVPixelFormatCGBitmapContextCompatibility@^{__CFString=}$kCVPixelFormatCGBitmapInfo@^{__CFString=}$kCVPixelFormatCGImageCompatibility@^{__CFString=}$kCVPixelFormatCodecType@^{__CFString=}$kCVPixelFormatComponentRange@^{__CFString=}$kCVPixelFormatComponentRange_FullRange@^{__CFString=}$kCVPixelFormatComponentRange_VideoRange@^{__CFString=}$kCVPixelFormatComponentRange_WideRange@^{__CFString=}$kCVPixelFormatConstant@^{__CFString=}$kCVPixelFormatContainsAlpha@^{__CFString=}$kCVPixelFormatContainsGrayscale@^{__CFString=}$kCVPixelFormatContainsRGB@^{__CFString=}$kCVPixelFormatContainsYCbCr@^{__CFString=}$kCVPixelFormatFillExtendedPixelsCallback@^{__CFString=}$kCVPixelFormatFourCC@^{__CFString=}$kCVPixelFormatHorizontalSubsampling@^{__CFString=}$kCVPixelFormatName@^{__CFString=}$kCVPixelFormatOpenGLCompatibility@^{__CFString=}$kCVPixelFormatOpenGLESCompatibility@^{__CFString=}$kCVPixelFormatOpenGLFormat@^{__CFString=}$kCVPixelFormatOpenGLInternalFormat@^{__CFString=}$kCVPixelFormatOpenGLType@^{__CFString=}$kCVPixelFormatPlanes@^{__CFString=}$kCVPixelFormatQDCompatibility@^{__CFString=}$kCVPixelFormatVerticalSubsampling@^{__CFString=}$kCVZeroTime@{_CVTime=qii}$"""
enums = """$COREVIDEO_INCLUDED_IOSURFACE_HEADER_FILE@1$kCVAttachmentMode_ShouldNotPropagate@0$kCVAttachmentMode_ShouldPropagate@1$kCVPixelBufferLock_ReadOnly@1$kCVPixelBufferPoolFlushExcessBuffers@1$kCVPixelFormatType_128RGBAFloat@1380410945$kCVPixelFormatType_14Bayer_BGGR@1650943796$kCVPixelFormatType_14Bayer_GBRG@1734505012$kCVPixelFormatType_14Bayer_GRBG@1735549492$kCVPixelFormatType_14Bayer_RGGB@1919379252$kCVPixelFormatType_16BE555@16$kCVPixelFormatType_16BE565@1110783541$kCVPixelFormatType_16Gray@1647392359$kCVPixelFormatType_16LE555@1278555445$kCVPixelFormatType_16LE5551@892679473$kCVPixelFormatType_16LE565@1278555701$kCVPixelFormatType_1IndexedGray_WhiteIsZero@33$kCVPixelFormatType_1Monochrome@1$kCVPixelFormatType_24BGR@842285639$kCVPixelFormatType_24RGB@24$kCVPixelFormatType_2Indexed@2$kCVPixelFormatType_2IndexedGray_WhiteIsZero@34$kCVPixelFormatType_30RGB@1378955371$kCVPixelFormatType_30RGBLEPackedWideGamut@1999843442$kCVPixelFormatType_32ABGR@1094862674$kCVPixelFormatType_32ARGB@32$kCVPixelFormatType_32AlphaGray@1647522401$kCVPixelFormatType_32BGRA@1111970369$kCVPixelFormatType_32RGBA@1380401729$kCVPixelFormatType_420YpCbCr10BiPlanarFullRange@2019963440$kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange@2016686640$kCVPixelFormatType_420YpCbCr8BiPlanarFullRange@875704422$kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange@875704438$kCVPixelFormatType_420YpCbCr8Planar@2033463856$kCVPixelFormatType_420YpCbCr8PlanarFullRange@1714696752$kCVPixelFormatType_420YpCbCr8VideoRange_8A_TriPlanar@1982882104$kCVPixelFormatType_422YpCbCr10@1983000880$kCVPixelFormatType_422YpCbCr10BiPlanarFullRange@2019963442$kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange@2016686642$kCVPixelFormatType_422YpCbCr16@1983000886$kCVPixelFormatType_422YpCbCr8@846624121$kCVPixelFormatType_422YpCbCr8FullRange@2037741158$kCVPixelFormatType_422YpCbCr8_yuvs@2037741171$kCVPixelFormatType_422YpCbCr_4A_8BiPlanar@1630697081$kCVPixelFormatType_4444AYpCbCr16@2033463606$kCVPixelFormatType_4444AYpCbCr8@2033463352$kCVPixelFormatType_4444YpCbCrA8@1983131704$kCVPixelFormatType_4444YpCbCrA8R@1916022840$kCVPixelFormatType_444YpCbCr10@1983131952$kCVPixelFormatType_444YpCbCr10BiPlanarFullRange@2019963956$kCVPixelFormatType_444YpCbCr10BiPlanarVideoRange@2016687156$kCVPixelFormatType_444YpCbCr8@1983066168$kCVPixelFormatType_48RGB@1647589490$kCVPixelFormatType_4Indexed@4$kCVPixelFormatType_4IndexedGray_WhiteIsZero@36$kCVPixelFormatType_64ARGB@1647719521$kCVPixelFormatType_64RGBAHalf@1380411457$kCVPixelFormatType_8Indexed@8$kCVPixelFormatType_8IndexedGray_WhiteIsZero@40$kCVPixelFormatType_ARGB2101010LEPacked@1815162994$kCVPixelFormatType_DepthFloat16@1751410032$kCVPixelFormatType_DepthFloat32@1717855600$kCVPixelFormatType_DisparityFloat16@1751411059$kCVPixelFormatType_DisparityFloat32@1717856627$kCVPixelFormatType_OneComponent16Half@1278226536$kCVPixelFormatType_OneComponent32Float@1278226534$kCVPixelFormatType_OneComponent8@1278226488$kCVPixelFormatType_TwoComponent16Half@843264104$kCVPixelFormatType_TwoComponent32Float@843264102$kCVPixelFormatType_TwoComponent8@843264056$kCVReturnAllocationFailed@-6662$kCVReturnDisplayLinkAlreadyRunning@-6671$kCVReturnDisplayLinkCallbacksNotSet@-6673$kCVReturnDisplayLinkNotRunning@-6672$kCVReturnError@-6660$kCVReturnFirst@-6660$kCVReturnInvalidArgument@-6661$kCVReturnInvalidDisplay@-6670$kCVReturnInvalidPixelBufferAttributes@-6682$kCVReturnInvalidPixelFormat@-6680$kCVReturnInvalidPoolAttributes@-6691$kCVReturnInvalidSize@-6681$kCVReturnLast@-6699$kCVReturnPixelBufferNotMetalCompatible@-6684$kCVReturnPixelBufferNotOpenGLCompatible@-6683$kCVReturnPoolAllocationFailed@-6690$kCVReturnRetry@-6692$kCVReturnSuccess@0$kCVReturnUnsupported@-6663$kCVReturnWouldExceedAllocationThreshold@-6689$kCVSMPTETimeRunning@2$kCVSMPTETimeType24@0$kCVSMPTETimeType25@1$kCVSMPTETimeType2997@4$kCVSMPTETimeType2997Drop@5$kCVSMPTETimeType30@3$kCVSMPTETimeType30Drop@2$kCVSMPTETimeType5994@7$kCVSMPTETimeType60@6$kCVSMPTETimeValid@1$kCVTimeIsIndefinite@1$kCVTimeStampBottomField@131072$kCVTimeStampHostTimeValid@2$kCVTimeStampIsInterlaced@196608$kCVTimeStampRateScalarValid@16$kCVTimeStampSMPTETimeValid@4$kCVTimeStampTopField@65536$kCVTimeStampVideoHostTimeValid@3$kCVTimeStampVideoRefreshPeriodValid@8$kCVTimeStampVideoTimeValid@1$kReturnRetry@-6692$"""
misc.update({})
functions = {
    "CVImageBufferGetEncodedSize": (
        sel32or64(b"{CGSize=ff}^{__CVBuffer=}", b"{CGSize=dd}^{__CVBuffer=}"),
    ),
    "CVOpenGLTextureRelease": (b"v^{__CVBuffer=}",),
    "CVPixelBufferPoolRelease": (b"v^{__CVPixelBufferPool=}",),
    "CVPixelBufferPoolGetTypeID": (sel32or64(b"L", b"Q"),),
    "CVYCbCrMatrixGetIntegerCodePointForString": (b"i^{__CFString=}",),
    "CVPixelBufferCreate": (
        sel32or64(
            b"i^{__CFAllocator=}LLL^{__CFDictionary=}^^{__CVBuffer=}",
            b"i^{__CFAllocator=}QQI^{__CFDictionary=}^^{__CVBuffer=}",
        ),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVOpenGLBufferPoolGetTypeID": (sel32or64(b"L", b"Q"),),
    "CVPixelBufferFillExtendedPixels": (b"i^{__CVBuffer=}",),
    "CVOpenGLTextureCacheRetain": (
        b"^{__CVOpenGLTextureCache=}^{__CVOpenGLTextureCache=}",
    ),
    "CVOpenGLBufferPoolCreateOpenGLBuffer": (
        b"i^{__CFAllocator=}^{__CVOpenGLBufferPool=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkSetCurrentCGDisplay": (b"i^{__CVDisplayLink=}I",),
    "CVBufferSetAttachment": (b"v^{__CVBuffer=}^{__CFString=}@I",),
    "CVGetCurrentHostTime": (b"Q", "", {"variadic": False}),
    "CVPixelBufferPoolCreate": (
        b"i^{__CFAllocator=}^{__CFDictionary=}^{__CFDictionary=}^^{__CVPixelBufferPool=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVPixelBufferGetHeightOfPlane": (
        sel32or64(b"L^{__CVBuffer=}L", b"Q^{__CVBuffer=}Q"),
    ),
    "CVBufferRetain": (b"^{__CVBuffer=}^{__CVBuffer=}",),
    "CVDisplayLinkTranslateTime": (
        sel32or64(
            b"i^{__CVDisplayLink=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}",
            b"i^{__CVDisplayLink=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
        ),
        "",
        {"arguments": {1: {"type_modifier": "n"}, 2: {"type_modifier": "o"}}},
    ),
    "CVPixelBufferRetain": (b"^{__CVBuffer=}^{__CVBuffer=}",),
    "CVPixelBufferGetPlaneCount": (sel32or64(b"L^{__CVBuffer=}", b"Q^{__CVBuffer=}"),),
    "CVOpenGLTextureCacheRelease": (b"v^{__CVOpenGLTextureCache=}",),
    "CVPixelBufferGetBaseAddress": (
        b"^v^{__CVBuffer=}",
        "",
        {"retval": {"c_array_of_variable_length": True}},
    ),
    "CVOpenGLBufferPoolRelease": (b"v^{__CVOpenGLBufferPool=}",),
    "CVPixelBufferLockBaseAddress": (b"i^{__CVBuffer=}Q",),
    "CVOpenGLTextureCacheGetTypeID": (sel32or64(b"L", b"Q"),),
    "CVPixelBufferUnlockBaseAddress": (b"i^{__CVBuffer=}Q",),
    "CVMetalTextureCacheCreateTextureFromImage": (
        b"i^{__CFAllocator=}^{__CVMetalTextureCache=}^{__CVBuffer=}^{__CFDictionary=}QQQQ^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {8: {"type_modifier": "o"}},
        },
    ),
    "CVOpenGLTextureIsFlipped": (b"Z^{__CVBuffer=}",),
    "CVMetalTextureCacheFlush": (b"v^{__CVMetalTextureCache=}Q",),
    "CVPixelBufferPoolCreatePixelBuffer": (
        b"i^{__CFAllocator=}^{__CVPixelBufferPool=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVPixelBufferGetTypeID": (sel32or64(b"L", b"Q"),),
    "CVDisplayLinkGetActualOutputVideoRefreshPeriod": (b"d^{__CVDisplayLink=}",),
    "CVPixelBufferGetWidth": (sel32or64(b"L^{__CVBuffer=}", b"Q^{__CVBuffer=}"),),
    "CVMetalTextureCacheGetTypeID": (b"Q",),
    "CVDisplayLinkCreateWithCGDisplay": (
        b"iI^^{__CVDisplayLink=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVBufferRelease": (b"v^{__CVBuffer=}",),
    "CVDisplayLinkStart": (b"i^{__CVDisplayLink=}",),
    "CVDisplayLinkGetCurrentTime": (
        sel32or64(
            b"i^{__CVDisplayLink=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssLLLssss}QQ}",
            b"i^{__CVDisplayLink=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
        ),
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes": (
        b"^{__CFArray=}^{__CFAllocator=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVPixelBufferPoolGetAttributes": (b"^{__CFDictionary=}^{__CVPixelBufferPool=}",),
    "CVBufferGetAttachments": (b"^{__CFDictionary=}^{__CVBuffer=}I",),
    "CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType": (
        sel32or64(b"v^{__CFDictionary=}L", b"v^{__CFDictionary=}I"),
    ),
    "CVOpenGLBufferPoolCreate": (
        b"i^{__CFAllocator=}^{__CFDictionary=}^{__CFDictionary=}^^{__CVOpenGLBufferPool=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkRetain": (b"^{__CVDisplayLink=}^{__CVDisplayLink=}",),
    "CVPixelBufferCreateWithIOSurface": (
        b"i^{__CFAllocator=}^{__IOSurface=}^{__CFDictionary=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkCreateWithOpenGLDisplayMask": (
        b"iI^^{__CVDisplayLink=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkSetOutputHandler": (
        b"i^{__CVDisplayLink=}@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"i"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "^{__CVDisplayLink=}"},
                            2: {
                                "type": "^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                                "type_modifier": "n",
                            },
                            3: {
                                "type": "^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                                "type_modifier": "n",
                            },
                            4: {"type": "Q"},
                            5: {"type": "o^Q"},
                        },
                    }
                }
            }
        },
    ),
    "CVYCbCrMatrixGetStringForIntegerCodePoint": (b"^{__CFString=}i",),
    "CVOpenGLBufferCreate": (
        sel32or64(
            b"i^{__CFAllocator=}LL^{__CFDictionary=}^^{__CVBuffer=}",
            b"i^{__CFAllocator=}QQ^{__CFDictionary=}^^{__CVBuffer=}",
        ),
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {4: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVPixelBufferPoolCreatePixelBufferWithAuxAttributes": (
        b"i^{__CFAllocator=}^{__CVPixelBufferPool=}^{__CFDictionary=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVOpenGLTextureCacheFlush": (b"v^{__CVOpenGLTextureCache=}Q",),
    "CVDisplayLinkCreateWithActiveCGDisplays": (
        b"i^^{__CVDisplayLink=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkGetNominalOutputVideoRefreshPeriod": (
        b"{_CVTime=qii}^{__CVDisplayLink=}",
    ),
    "CVPixelBufferCreateResolvedAttributesDictionary": (
        b"i^{__CFAllocator=}^{__CFArray=}^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkSetOutputCallback": (
        b"i^{__CVDisplayLink=}^?^v",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"i"},
                        "arguments": {
                            0: {"type": b"^{__CVDisplayLink=}"},
                            1: {
                                "type": b"^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                                "type_modifier": "n",
                            },
                            2: {
                                "type": b"^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                                "type_modifier": "N",
                            },
                            3: {"type": b"Q"},
                            4: {"type": b"^Q", "type_modifier": "o"},
                            5: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
    "CVOpenGLTextureGetName": (b"I^{__CVBuffer=}",),
    "CVOpenGLBufferRelease": (b"v^{__CVBuffer=}",),
    "CVOpenGLTextureRetain": (b"^{__CVBuffer=}^{__CVBuffer=}",),
    "CVOpenGLBufferPoolGetAttributes": (b"^{__CFDictionary=}^{__CVOpenGLBufferPool=}",),
    "CVPixelBufferGetWidthOfPlane": (
        sel32or64(b"L^{__CVBuffer=}L", b"Q^{__CVBuffer=}Q"),
    ),
    "CVBufferPropagateAttachments": (b"v^{__CVBuffer=}^{__CVBuffer=}",),
    "CVPixelBufferPoolRetain": (b"^{__CVPixelBufferPool=}^{__CVPixelBufferPool=}",),
    "CVPixelBufferGetHeight": (sel32or64(b"L^{__CVBuffer=}", b"Q^{__CVBuffer=}"),),
    "CVColorPrimariesGetIntegerCodePointForString": (b"i^{__CFString=}",),
    "CVOpenGLBufferGetTypeID": (sel32or64(b"L", b"Q"),),
    "CVDisplayLinkRelease": (b"v^{__CVDisplayLink=}",),
    "CVBufferGetAttachment": (
        b"@^{__CVBuffer=}^{__CFString=}^I",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "CVDisplayLinkStop": (b"i^{__CVDisplayLink=}",),
    "CVPixelFormatDescriptionCreateWithPixelFormatType": (
        sel32or64(
            b"^{__CFDictionary=}^{__CFAllocator=}L",
            b"^{__CFDictionary=}^{__CFAllocator=}I",
        ),
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVMetalTextureGetCleanTexCoords": (
        b"v^{__CVBuffer=}^f^f^f^f",
        "",
        {
            "arguments": {
                1: {"c_array_of_fixed_length": 2, "type_modifier": "o"},
                2: {"c_array_of_fixed_length": 2, "type_modifier": "o"},
                3: {"c_array_of_fixed_length": 2, "type_modifier": "o"},
                4: {"c_array_of_fixed_length": 2, "type_modifier": "o"},
            }
        },
    ),
    "CVPixelBufferGetIOSurface": (b"^{__IOSurface=}^{__CVBuffer=}",),
    "CVOpenGLTextureCacheCreateTextureFromImage": (
        b"i^{__CFAllocator=}^{__CVOpenGLTextureCache=}^{__CVBuffer=}^{__CFDictionary=}^^{__CVBuffer=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVDisplayLinkCreateWithCGDisplays": (
        sel32or64(b"i^Il^^{__CVDisplayLink=}", b"i^Iq^^{__CVDisplayLink=}"),
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                0: {"c_array_length_in_arg": 1, "type_modifier": "n"},
                2: {"already_cfretained": True, "type_modifier": "o"},
            },
        },
    ),
    "CVPixelBufferPoolGetPixelBufferAttributes": (
        b"^{__CFDictionary=}^{__CVPixelBufferPool=}",
    ),
    "CVOpenGLTextureGetTypeID": (sel32or64(b"L", b"Q"),),
    "CVImageBufferIsFlipped": (b"Z^{__CVBuffer=}",),
    "CVMetalTextureGetTexture": (b"@^{__CVBuffer=}",),
    "CVPixelBufferIsPlanar": (b"Z^{__CVBuffer=}",),
    "CVBufferRemoveAllAttachments": (b"v^{__CVBuffer=}",),
    "CVTransferFunctionGetIntegerCodePointForString": (b"i^{__CFString=}",),
    "CVPixelBufferCreateWithBytes": (
        sel32or64(
            b"i^{__CFAllocator=}LLL^vL^?^v^{__CFDictionary=}^^{__CVBuffer=}",
            b"i^{__CFAllocator=}QQI^vQ^?^v^{__CFDictionary=}^^{__CVBuffer=}",
        ),
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"^v"}},
                    }
                }
            },
        },
    ),
    "CVMetalTextureGetTypeID": (b"Q",),
    "CVOpenGLBufferPoolRetain": (b"^{__CVOpenGLBufferPool=}^{__CVOpenGLBufferPool=}",),
    "CVPixelBufferCreateWithPlanarBytes": (
        sel32or64(
            b"i^{__CFAllocator=}LLL^vLL^^v^L^L^L^?^v^{__CFDictionary=}^^{__CVBuffer=}",
            b"i^{__CFAllocator=}QQI^vQQ^^v^Q^Q^Q^?^v^{__CFDictionary=}^^{__CVBuffer=}",
        ),
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                11: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^v"},
                            2: {"type": b"Q"},
                            3: {"type": b"Q"},
                            4: {"type": b"^^v"},
                        },
                    }
                }
            },
        },
    ),
    "CVImageBufferGetCleanRect": (
        sel32or64(
            b"{CGRect={CGPoint=ff}{CGSize=ff}}^{__CVBuffer=}",
            b"{CGRect={CGPoint=dd}{CGSize=dd}}^{__CVBuffer=}",
        ),
    ),
    "CVImageBufferCreateColorSpaceFromAttachments": (
        b"^{CGColorSpace=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVPixelBufferGetBytesPerRowOfPlane": (
        sel32or64(b"L^{__CVBuffer=}L", b"Q^{__CVBuffer=}Q"),
    ),
    "CVColorPrimariesGetStringForIntegerCodePoint": (b"^{__CFString=}i",),
    "CVDisplayLinkGetTypeID": (sel32or64(b"L", b"Q"),),
    "CVImageBufferGetDisplaySize": (
        sel32or64(b"{CGSize=ff}^{__CVBuffer=}", b"{CGSize=dd}^{__CVBuffer=}"),
    ),
    "CVPixelBufferGetDataSize": (sel32or64(b"L^{__CVBuffer=}", b"Q^{__CVBuffer=}"),),
    "CVOpenGLBufferPoolGetOpenGLBufferAttributes": (
        b"^{__CFDictionary=}^{__CVOpenGLBufferPool=}",
    ),
    "CVOpenGLBufferAttach": (b"i^{__CVBuffer=}^{_CGLContextObject=}Iii",),
    "CVPixelBufferGetBaseAddressOfPlane": (
        sel32or64(b"^v^{__CVBuffer=}L", b"^v^{__CVBuffer=}Q"),
        "",
        {"retval": {"c_array_of_variable_length": True}},
    ),
    "CVDisplayLinkIsRunning": (b"Z^{__CVDisplayLink=}",),
    "CVPixelBufferGetPixelFormatType": (
        sel32or64(b"L^{__CVBuffer=}", b"I^{__CVBuffer=}"),
    ),
    "CVBufferRemoveAttachment": (b"v^{__CVBuffer=}^{__CFString=}",),
    "CVOpenGLBufferGetAttributes": (b"^{__CFDictionary=}^{__CVBuffer=}",),
    "CVDisplayLinkGetOutputVideoLatency": (b"{_CVTime=qii}^{__CVDisplayLink=}",),
    "CVPixelBufferGetBytesPerRow": (sel32or64(b"L^{__CVBuffer=}", b"Q^{__CVBuffer=}"),),
    "CVMetalTextureCacheCreate": (
        b"i^{__CFAllocator=}^{__CFDictionary=}@^{__CFDictionary=}^^{__CVMetalTextureCache=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVPixelBufferGetExtendedPixels": (
        sel32or64(b"v^{__CVBuffer=}^L^L^L^L", b"v^{__CVBuffer=}^Q^Q^Q^Q"),
        "",
        {
            "arguments": {
                1: {"type_modifier": "o"},
                2: {"type_modifier": "o"},
                3: {"type_modifier": "o"},
                4: {"type_modifier": "o"},
            }
        },
    ),
    "CVTransferFunctionGetStringForIntegerCodePoint": (b"^{__CFString=}i",),
    "CVImageBufferGetColorSpace": (b"^{CGColorSpace=}^{__CVBuffer=}",),
    "CVDisplayLinkGetCurrentCGDisplay": (b"I^{__CVDisplayLink=}",),
    "CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext": (
        b"i^{__CVDisplayLink=}^{_CGLContextObject=}^{_CGLPixelFormatObject=}",
    ),
    "CVPixelBufferRelease": (b"v^{__CVBuffer=}",),
    "CVBufferSetAttachments": (b"v^{__CVBuffer=}^{__CFDictionary=}I",),
    "CVOpenGLTextureGetTarget": (b"I^{__CVBuffer=}",),
    "CVGetHostClockFrequency": (b"d", "", {"variadic": False}),
    "CVGetHostClockMinimumTimeDelta": (b"I", "", {"variadic": False}),
    "CVOpenGLBufferRetain": (b"^{__CVBuffer=}^{__CVBuffer=}",),
    "CVMetalTextureIsFlipped": (b"Z^{__CVBuffer=}",),
    "CVOpenGLTextureCacheCreate": (
        b"i^{__CFAllocator=}^{__CFDictionary=}^{_CGLContextObject=}^{_CGLPixelFormatObject=}^{__CFDictionary=}^^{__CVOpenGLTextureCache=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVPixelBufferPoolFlush": (b"v^{__CVPixelBufferPool=}Q",),
    "CVOpenGLTextureGetCleanTexCoords": (b"v^{__CVBuffer=}[2f][2f][2f][2f]",),
}
aliases = {
    "COREVIDEO_USE_DERIVED_ENUMS_FOR_CONSTANTS": "COREVIDEO_TRUE",
    "COREVIDEO_SUPPORTS_PREFETCH": "COREVIDEO_TRUE",
    "CVImageBufferRef": "CVBufferRef",
    "COREVIDEO_SUPPORTS_DIRECT3D": "COREVIDEO_FALSE",
    "COREVIDEO_SUPPORTS_GLES_TEX_IMAGE_IOSURFACE": "COREVIDEO_SUPPORTS_IOSURFACE",
    "COREVIDEO_SUPPORTS_OPENGL": "COREVIDEO_TRUE",
    "COREVIDEO_DECLARE_NULLABILITY": "COREVIDEO_TRUE",
    "COREVIDEO_SUPPORTS_IOSURFACE_PREFETCH": "COREVIDEO_FALSE",
    "COREVIDEO_SUPPORTS_IOSURFACE": "COREVIDEO_TRUE",
    "COREVIDEO_SUPPORTS_OPENGLES": "COREVIDEO_FALSE",
    "COREVIDEO_SUPPORTS_COLORSPACE": "COREVIDEO_TRUE",
    "CV_INLINE": "CF_INLINE",
    "CV_RELEASES_ARGUMENT": "CF_RELEASES_ARGUMENT",
    "CV_RETURNS_RETAINED_PARAMETER": "CF_RETURNS_RETAINED",
    "COREVIDEO_SUPPORTS_DISPLAYLINK": "COREVIDEO_TRUE",
    "CV_NULLABLE": "__nullable",
    "COREVIDEO_USE_IOSURFACEREF": "COREVIDEO_FALSE",
    "CV_NONNULL": "__nonnull",
    "kCVReturnError": "kCVReturnFirst",
    "COREVIDEO_SUPPORTS_METAL": "COREVIDEO_TRUE",
}
cftypes = [
    ("CVBufferRef", b"^{__CVBuffer=}", "CVBufferGetTypeID", None),
    ("CVDisplayLinkRef", b"^{__CVDisplayLink=}", "CVDisplayLinkGetTypeID", None),
    ("CVMetalTextureCacheRef", b"^{__CVMetalTextureCache=}", None, None),
    (
        "CVOpenGLBufferPoolRef",
        b"^{__CVOpenGLBufferPool=}",
        "CVOpenGLBufferPoolGetTypeID",
        None,
    ),
    (
        "CVOpenGLTextureCacheRef",
        b"^{__CVOpenGLTextureCache=}",
        "CVOpenGLTextureCacheGetTypeID",
        None,
    ),
    (
        "CVPixelBufferPoolRef",
        b"^{__CVPixelBufferPool=}",
        "CVPixelBufferPoolGetTypeID",
        None,
    ),
    ("CVOpenGLBufferRef", b"^{__CVOpenGLBuffer=}", "CVOpenGLBufferGetTypeID", None),
    ("CVPixelBufferRef", b"^{__CVPixelBuffer=}", "CVPixelBufferGetTypeID", None),
    ("CVOpenGLTextureRef", b"^{__CVOpenGLTexture=}", "CVOpenGLTextureGetTypeID", None),
]
expressions = {}

# END OF FILE
