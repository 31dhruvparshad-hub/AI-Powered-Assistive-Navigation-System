def get_position(center_x, frame_width):

    if center_x < frame_width / 3:
        return "left"

    elif center_x < 2 * frame_width / 3:
        return "center"

    return "right"


def estimate_distance(area):

    if area > 120000:
        return "very close"

    elif area > 50000:
        return "close"

    return "far"