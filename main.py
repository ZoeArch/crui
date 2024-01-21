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
        raise ValueError("Added array with this height offset is out of bounds")
    if len(array_to_add_to[0]) < len(array_to_be_added[0]) + offset_width:
        raise ValueError("Added array with this width offset is out of bounds")

    for i in range(len(array_to_be_added)):
        for j in range(len(array_to_be_added[0])):
            # Replace the corresponding elements in the target array at the specified offset
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
# print_frame(make_window("thin", 10, 10))
# input("")
# print("next")
# print_frame(make_window("thick", term_height, term_width))

main_frame = make_window("double_thin", term_height, term_width)
print_to_console(main_frame)
subframe1 = make_window("thick", 10, 10)
print_to_console(subframe1)
subframe2 = make_window("thin", 10, 10)
print_to_console(subframe2)

main_frame = draw_window_over_window(main_frame, subframe1, 3, 3)
main_frame = draw_window_over_window(main_frame, subframe2, 20, 20)
print_to_console(main_frame)
