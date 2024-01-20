import os
import shutil

# Terminology
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


# Get terminal size and store it in the variable temp
term_size = shutil.get_terminal_size()

# Access the width and height
term_width = term_size.columns
term_height = term_size.lines

# create the "frame" array
fill_char = "0"
width_fill = []
frame = []
for i in range(term_width):
    width_fill.append(str(fill_char))
for i in range(term_height):
    frame.append(width_fill)


def array_add_with_offset(
    array_to_add_to: list,
    array_to_be_added: list,
    offset_height: int,
    offset_width: int,
):
    if len(array_to_add_to) < len(array_to_be_added) + offset_height:
        raise ValueError("Added array with this height offset is out of bounds")
    if len(array_to_add_to[0]) < len(array_to_be_added[0]) + offset_width:
        raise ValueError("Added array with this width offset is out of bounds")


def print_frame2(frame_to_print):
    for i in frame_to_print:
        local_array = i
        current_location = 0
        for i in local_array:
            print(local_array[current_location], end="", sep="")
            current_location = +1
        print("\n", end="", sep="")


def print_frame(frame_to_print):
    for i in frame_to_print:
        local_array = i
        current_location = 0
        for j in local_array:
            print(j, end="", sep="")
            current_location += 1  # Fix the increment here
        print("\n", end="", sep="")


def print_frame3(frame_to_print):
    for i in frame_to_print:
        local_array = i
        for x in range(len(local_array)):
            print(local_array[x], end="", sep="")
        print("\n", end="", sep="")


def make_box(border: str, box_height: int, box_width: int):
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
            raise ValueError("Needs to be an acceptable type of border")

    top_edge = []
    top_edge.append(local_dict["corner_top_left"])
    for i in range(box_width):
        top_edge.append(local_dict["horizontal"])
    top_edge.append(local_dict["corner_top_right"])

    output.append(top_edge.copy())  # Copy the top edge to preserve it

    middle = []
    middle.append(local_dict["vertical"])
    for i in range(box_width):
        middle.append(fill_char)
    middle.append(local_dict["vertical"])

    for i in range(box_height - 2):
        output.append(middle.copy())  # Copy the middle row

    bottom_edge = []
    bottom_edge.append(local_dict["corner_bottom_left"])
    for i in range(box_width):
        bottom_edge.append(local_dict["horizontal"])
    bottom_edge.append(local_dict["corner_bottom_right"])

    output.append(bottom_edge.copy())  # Copy the bottom edge
    return output


# print_frame(frame)
print_frame3(make_box("thin", 10, 10))
input("")
print("next")
print_frame3(make_box("thick", term_height, term_width))
