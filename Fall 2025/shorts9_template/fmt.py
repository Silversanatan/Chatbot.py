def fmt(spec, values):
    if spec == "":
        return ""
    if spec[0:2] == "{}":
        return str(values[0]) + fmt(spec[2:], values[1:])
    if spec[0:2] != "{}":
        return spec[0] + fmt(spec[1:], values)
    return ""