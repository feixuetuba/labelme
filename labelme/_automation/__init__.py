from ._types import AiOutputFormat


def __getattr__(name: str):
    """懒加载所有模块，避免启动时导入 skimage/scipy/osam/onnxruntime"""
    if name == "shape_to_xyxy_bbox":
        from ._geometry import shape_to_xyxy_bbox
        return shape_to_xyxy_bbox
    elif name == "MASK_REQUIRED_SHAPE_TYPES":
        from ._shape_builders import MASK_REQUIRED_SHAPE_TYPES
        return MASK_REQUIRED_SHAPE_TYPES
    elif name == "Detection":
        from ._shape_builders import Detection
        return Detection
    elif name == "shapes_from_detections":
        from ._shape_builders import shapes_from_detections
        return shapes_from_detections
    elif name == "suppress_detections_greedy":
        from ._suppression import suppress_detections_greedy
        return suppress_detections_greedy
    elif name == "suppress_detections_overlapping_existing_shapes":
        from ._suppression import suppress_detections_overlapping_existing_shapes
        return suppress_detections_overlapping_existing_shapes
    elif name == "AiAssistSession":
        from ._ai_assist import AiAssistSession
        return AiAssistSession
    elif name == "OsamSession":
        from ._osam_session import OsamSession
        return OsamSession
    elif name == "get_bboxes_from_texts":
        from ._text_detection import get_bboxes_from_texts
        return get_bboxes_from_texts
    elif name == "nms_bboxes":
        from ._text_detection import nms_bboxes
        return nms_bboxes
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
