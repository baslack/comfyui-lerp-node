# comfyui-lerp-node
A simple math node that performs linear interpolation between a base range and a mapped range.

## SimpleLERP

Maps an input `value` from an input range `[in_min, in_max]` onto an output range
`[out_min, out_max]`:

```
t      = (value - in_min) / (in_max - in_min)
output = out_min + t * (out_max - out_min)
```

Found in the node browser under the **math** category as **Simple LERP**.

### Inputs

| Name      | Type    | Default | Description                                                        |
|-----------|---------|---------|--------------------------------------------------------------------|
| `value`   | FLOAT   | 0.0     | The value to map.                                                  |
| `in_min`  | FLOAT   | 0.0     | Lower bound of the input range.                                    |
| `in_max`  | FLOAT   | 1.0     | Upper bound of the input range.                                    |
| `out_min` | FLOAT   | 0.0     | Lower bound of the output range.                                   |
| `out_max` | FLOAT   | 1.0     | Upper bound of the output range.                                   |
| `clamp`   | BOOLEAN | False   | If true, hold the result within the output range instead of extrapolating. |

### Output

| Name    | Type  | Description                |
|---------|-------|----------------------------|
| `value` | FLOAT | The interpolated result.   |

Notes:
- With `clamp` off, inputs outside `[in_min, in_max]` extrapolate beyond the output range.
- Inverted ranges (e.g. `out_min > out_max`) are supported.
- If `in_min == in_max`, the result is `out_min` (no division by zero).
