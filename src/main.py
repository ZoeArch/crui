import os
import shutil

# terminology
# frame = the current array to draw
# window = the individual parts of the frame to be drawn

thin_dict = {
    "horizontal": "─",
    "vertical": "│",
    "corner_top_left": "┌",
    "corner_top_right": "┐",
    "corner_bottom_left": "└",
    "corner_bottom_right": "┘",
    "left_t": "├",
    "right_t": "┤",
    "top_t": "┬",
    "bottom_t": "┴",
    "crossing": "┼",
}
thick_dict = {
    "horizontal": "━",
    "vertical": "┃",
    "corner_top_left": "┏",
    "corner_top_right": "┓",
    "corner_bottom_left": "┗",
    "corner_bottom_right": "┛",
    "left_t": "┣",
    "right_t": "┫",
    "top_t": "┳",
    "bottom_t": "┻",
    "crossing": "╋",
}
double_line_dict = {
    "horizontal": "═",
    "vertical": "║",
    "corner_top_left": "╔",
    "corner_top_right": "╗",
    "corner_bottom_left": "╚",
    "corner_bottom_right": "╝",
    "left_t": "╠",
    "right_t": "╣",
    "top_t": "╦",
    "bottom_t": "╩",
    "crossing": "╬",
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

    for i in range(len(array_to_be_added)):
        for j in range(len(array_to_be_added[0])):
            # replace the corresponding elements in the target array at the specified offset
            array_to_add_to[i + offset_height][j + offset_width] = array_to_be_added[i][
                j
            ]
    return array_to_add_to


def print_to_console(frame_to_print):
    for i in frame_to_print:
        local_array = i
        for x in range(len(local_array)):
            print(local_array[x], end="", sep="")
        print("\n", end="", sep="")


def make_window(border: str, box_height: int, box_width: int):
    box_height = box_height - 2
    box_width = box_width - 2
    output = []
    match border:
        case "thin":
            local_dict = thin_dict
        case "thick":
            local_dict = thick_dict
        case "double_thin":
            local_dict = double_line_dict
        case _:
            raise ValueError("needs to be an acceptable type of border")

    top_edge = []
    top_edge.append(local_dict["corner_top_left"])
    for i in range(box_width):
        top_edge.append(local_dict["horizontal"])
    top_edge.append(local_dict["corner_top_right"])

    output.append(top_edge.copy())  # copy the top edge to preserve it

    middle = []
    middle.append(local_dict["vertical"])
    for i in range(box_width):
        middle.append(fill_char)
    middle.append(local_dict["vertical"])

    for i in range(box_height - 2):
        output.append(middle.copy())  # copy the middle row

    bottom_edge = []
    bottom_edge.append(local_dict["corner_bottom_left"])
    for i in range(box_width):
        bottom_edge.append(local_dict["horizontal"])
    bottom_edge.append(local_dict["corner_bottom_right"])

    output.append(bottom_edge.copy())  # copy the bottom edge
    return output


def add_window_title(window: list, title: str, left_beauty: str, right_beauty: str):
    if (len(window[0]) - 2) <= len(title) + len(left_beauty) + len(right_beauty):
        raise ValueError("title + beautys is too long")
    top_edge = window[0]
    space_to_write = len(top_edge)
    text_with_beauty = left_beauty + title + right_beauty
    spacing = space_to_write - len(text_with_beauty)
    spacing = spacing // 2
    window = draw_window_over_window(window, [list(text_with_beauty)], 0, spacing + 1)
    return window


window = make_window("thin", term_height, term_width)
window = add_window_title(window, "testestestestest", "🞀[", "]🞂")
print_to_console(window)
