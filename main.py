import shutil

# terminology
# frame = the current array to draw
# window = the individual parts of the frame to be drawn

thin_dict = {
    "horizontal": "\u2500",  # ─
    "vertical": "\u2502",  # │
    "corner_top_left": "\u250c",  # ┌
    "corner_top_right": "\u2510",  # ┐
    "corner_bottom_left": "\u2514",  # └
    "corner_bottom_right": "\u2518",  # ┘
    "left_t": "\u251c",  # ├
    "right_t": "\u2524",  # ┤
    "top_t": "\u252c",  # ┬
    "bottom_t": "\u2534",  # ┴
    "crossing": "\u253c",  # ┼
}
thick_dict = {
    "horizontal": "\u2501",  # ━
    "vertical": "\u2503",  # ┃
    "corner_top_left": "\u250f",  # ┏
    "corner_top_right": "\u2513",  # ┓
    "corner_bottom_left": "\u2517",  # ┗
    "corner_bottom_right": "\u251b",  # ┛
    "left_t": "\u2523",  # ┣
    "right_t": "\u252b",  # ┫
    "top_t": "\u2533",  # ┳
    "bottom_t": "\u253b",  # ┻
    "crossing": "\u254b",  # ╋
}
double_line_dict = {
    "horizontal": "\u2550",  # ═
    "vertical": "\u2551",  # ║
    "corner_top_left": "\u2554",  # ╔
    "corner_top_right": "\u2557",  # ╗
    "corner_bottom_left": "\u255a",  # ╚
    "corner_bottom_right": "\u255d",  # ╝
    "left_t": "\u2560",  # ╠
    "right_t": "\u2563",  # ╣
    "top_t": "\u2566",  # ╦
    "bottom_t": "\u2569",  # ╩
    "crossing": "\u256c",  # ╬
}

dicts = {
    "thin": thin_dict,
    "thick": thick_dict,
    "thin_double": double_line_dict
}

# get terminal size and store it in the variable temp
term_size = shutil.get_terminal_size()

# access the width and height
term_width = term_size.columns
term_height = term_size.lines

# create the "frame" array
fill_char = " "
width_fill = []
frame = []
for i in range(term_width):
    width_fill.append(str(fill_char))
for i in range(term_height):
    frame.append(width_fill)


def draw_window_over_window(
        array_to_add_to: list,
        array_to_be_added: list,
        offset_height: int,
        offset_width: int,
):
    if len(array_to_add_to) < len(array_to_be_added) + offset_height:
        raise ValueError("added array with this height offset is out of bounds")
    if len(array_to_add_to[0]) < len(array_to_be_added[0]) + offset_width:
        raise ValueError("added array with this width offset is out of bounds")

    for x in range(len(array_to_be_added)):
        for y in range(len(array_to_be_added[0])):
            # replace the corresponding elements in the target array at the specified offset
            array_to_add_to[x + offset_height][y + offset_width] = array_to_be_added[x][y]
    return array_to_add_to


def print_to_console(frame_to_print):
    print('\n'.join(''.join(str(x) for x in i) for i in frame_to_print))


def make_window(border: str, box_height: int, box_width: int):
    box_height = box_height - 2
    box_width = box_width - 2
    output = []

    local_dict = dicts.get(border, None)
    if local_dict is None: raise ValueError("needs to be an acceptable type of border")

    # header
    header = [local_dict["horizontal"] for _ in range(box_width + 1)]
    header[0] = local_dict["corner_top_left"]
    header.append(local_dict["corner_top_right"])

    # footer
    footer = [local_dict["horizontal"] for _ in range(box_width + 1)]
    footer[0] = local_dict["corner_bottom_left"]
    footer.append(local_dict["corner_bottom_right"])

    output.append(header.copy())
    row = [local_dict["vertical"], fill_char * box_width, local_dict["vertical"]]
    for _ in range(box_height - 2): output.append(row.copy())
    output.append(footer.copy())

    return output


def add_window_title(window: list, title: str, left_beauty: str, right_beauty: str):
    if (len(window[0]) - 2) <= len(title) + len(left_beauty) + len(right_beauty):
        raise ValueError("title + beauties is too long")
    top_edge = window[0]
    space_to_write = len(top_edge)
    text_with_beauty = left_beauty + title + right_beauty
    spacing = space_to_write - len(text_with_beauty)
    spacing = spacing // 2
    return draw_window_over_window(window, [list(text_with_beauty)], 0, spacing + 1)


window = add_window_title(
    make_window("thin", term_height, term_width),
    "woah, hellow :D",
    "🞀[", "]🞂"
)
print_to_console(window)
