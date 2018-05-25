# Cameron Hardesty and Colton Spector
# cbs262 and crh445
# 11/2/17
# Section 3
# Lab 9
import turtle
filehandle = open('stars.txt', 'r')


def read_coords(file):
    coords_dict = {}
    mag_dict = {}
    names_dict = {}
    star_list = []
    for line in file:
        line = line.strip().split(' ', 6)
        star_list.append(line)
    # For loop to assign each value needed to a key
    for item in range(len(star_list)):
        x_coord = float(star_list[item][0])
        y_coord = float(star_list[item][1])
        draper = int(star_list[item][3])
        coords_dict[draper] = (x_coord, y_coord)
        mag = float(star_list[item][4])
        mag_dict[draper] = mag
        if len(star_list[item]) == 7:
            name = star_list[item][6].split(';')
            for i in range(len(name)):
                new_name = name[i].strip()
                names_dict[new_name] = draper
    star_dict = (coords_dict, mag_dict, names_dict)
    return star_dict


def plot_stars(picture_size, coordinates_dict):
    # Function that plots 2x2 stars using a turtle
    turtle.setup(picture_size, picture_size)
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.fillcolor("white")
    # For loop that creates 2x2 square stars on a turtle
    for key in coordinates_dict:
        x_coord = coordinates_dict[key][0]
        x_coord *= 500
        y_coord = coordinates_dict[key][1]
        y_coord *= 500
        turtle.penup()
        turtle.tracer(5)
        turtle.goto(x_coord, y_coord)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.forward(2)
        turtle.right(90)
        turtle.end_fill()
    turtle.exitonclick()


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    # Function that plots stars, size based on magnitude, using a turtle
    turtle.setup(picture_size, picture_size)
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.fillcolor("white")
    # For loop that creates stars size determined by magnitude in a turtle
    for key in magnitudes_dict:
        mag = magnitudes_dict[key]
        star_size = round(10/(mag + 2))
        if star_size > 8:
            star_size = 8
        x_coord = coordinates_dict[key][0]
        x_coord *= picture_size/2
        y_coord = coordinates_dict[key][1]
        y_coord *= picture_size/2
        turtle.penup()
        turtle.tracer(5)
        turtle.goto(x_coord, y_coord)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(star_size)
        turtle.right(90)
        turtle.forward(star_size)
        turtle.right(90)
        turtle.forward(star_size)
        turtle.right(90)
        turtle.forward(star_size)
        turtle.right(90)
        turtle.end_fill()
    turtle.exitonclick()


dictionaries = read_coords(filehandle)
plot_by_magnitude(1000, dictionaries[0], dictionaries[1])
