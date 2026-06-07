class SimpleLERP:
    """Linear interpolation: map a value from an input range to an output range."""

    @classmethod
    def INPUT_TYPES(cls):
        flt = {"default": 0.0, "min": -1e9, "max": 1e9, "step": 0.01}
        return {
            "required": {
                "value": ("FLOAT", flt),
                "in_min": ("FLOAT", {**flt, "default": 0.0}),
                "in_max": ("FLOAT", {**flt, "default": 1.0}),
                "out_min": ("FLOAT", {**flt, "default": 0.0}),
                "out_max": ("FLOAT", {**flt, "default": 1.0}),
                "clamp": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "lerp"
    CATEGORY = "math"

    def lerp(self, value, in_min, in_max, out_min, out_max, clamp):
        in_span = in_max - in_min
        if in_span == 0:
            # Degenerate input range: nothing to interpolate across.
            result = out_min
        else:
            t = (value - in_min) / in_span
            result = out_min + t * (out_max - out_min)

        if clamp:
            lo, hi = min(out_min, out_max), max(out_min, out_max)
            result = max(lo, min(hi, result))

        return (result,)


NODE_CLASS_MAPPINGS = {"SimpleLERP": SimpleLERP}
NODE_DISPLAY_NAME_MAPPINGS = {"SimpleLERP": "Simple LERP"}
