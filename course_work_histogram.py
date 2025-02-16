from graphics import GraphWin, Text, Line, Rectangle, Point, color_rgb


def get_rectangle(
    starting_point,
    ending_point,
    rectangle_color,
    window,
    frequency,
    topic,
    topic_color=color_rgb(129, 133, 144),
):
    """Get a rectangle with a topic in the middle

    Args:
        starting_point (tuple): starting point of the rectangle
        ending_point (tuple): ending point of the rectangle
        rectangle_color (tuple): color of the rectangle
        window (GraphWin): window to draw the rectangle
        topic (str): topic to be displayed in the middle of the rectangle
        topic_color (tuple, optional): color of the topic.
            Defaults to color_rgb(129, 133, 144).
    """

    # creating the rectangle
    rect = Rectangle(
        Point(starting_point[0], starting_point[1]),
        Point(ending_point[0], ending_point[1]),
    )

    # find the middle point for the topic
    topic_starting_point = (ending_point[0] + starting_point[0]) // 2

    rect_topic = Text(Point(topic_starting_point, 580), topic)
    rect_topic.setFill(topic_color)

    rect.setFill(rectangle_color)
    rect.draw(window)
    rect_topic.draw(window)

    total_text = Text(
        Point(topic_starting_point, starting_point[1] - 10), f"{frequency}"
    )
    total_text.setSize(18)
    total_text.setFill(color_rgb(129, 133, 144))
    total_text.draw(window)


def print_histogram(data, window_width=1000, window_height=700):
    """Prints a histogram based on the data

    Args:
        data (list): list of lists. Each list should have
            the following structure:
            [topic, frequency, color]
        window_width (int, optional): width of the window. Defaults to 1000.
        window_height (int, optional): height of the window. Defaults to 700.
    """
    histogram_title = "Histogram Results"
    win = GraphWin("Histogram", window_width, window_height)
    win.setBackground(color_rgb(237, 242, 236))

    heading = Text(Point(250, 50), histogram_title)
    heading.setTextColor(color_rgb(89, 88, 88))
    heading.setSize(28)
    heading.draw(win)
    aLine = Line(Point(100, 550), Point(800, 550))
    aLine.draw(win)

    # find the number of rectangles needed
    n_rectangles = len(data)

    total_frequency = 0
    max_frequency = 0

    for item in data:
        total_frequency += item[1]
        if max_frequency < item[1]:
            max_frequency = item[1]

    margin = 50
    margin_inbetween = 25
    # find the width of each rectangle
    rectangle_width = (
        window_width - (margin * 2) - (margin_inbetween * (n_rectangles - 1))
    ) // n_rectangles

    bottom_margin = 150
    top_margin = 25

    max_height = 450

    height_per_freq = max_height / max_frequency
    for i, item in enumerate(data):
        starting_point = [
            margin + (i * rectangle_width) + i * margin_inbetween,
            window_height - (height_per_freq * item[1] + top_margin) - bottom_margin,
        ]
        endinging_point = [
            margin + ((i + 1) * rectangle_width + i * margin_inbetween),
            window_height - bottom_margin,
        ]
        get_rectangle(
            starting_point=starting_point,
            ending_point=endinging_point,
            rectangle_color=color_rgb(item[2][0], item[2][1], item[2][2]),
            frequency=item[1],
            window=win,
            topic=item[0],
        )

    total_text = Text(Point(250, 600), f"Outcomes in Total: {total_frequency}")
    total_text.setSize(18)
    total_text.setFill(color_rgb(129, 133, 144))
    total_text.draw(win)

    win.getMouse()
    win.close()



def out_of_range (MK):
    range_remainder = MK%20
    if MK<=120 and range_remainder == 0:
         pass
    else:  
         print("Out of range")
         return "out of range"
    
    def total(pass_mk,defer_mk,fail_mk):
     total = pass_mk + defer_mk + fail_mk
    if total != 120:
          print("Total incorrect")

    else:
        
        if pass_mk == 120:
            print ("progress")

        elif pass_mk == 100:
            print("progress(module trailer)")

        elif fail_mk >= 80:
            print("exclude") 

        else:
            print("Do not progress - module retriever") 

        while True:
            print("Would you like to enter other set of data?")
            choice = input(("Enter 'Y' for yes or 'q' to quit and view results:"))
            if choice == "q":
                print_histogram(histogram_data)

            else:
                return



try:
    while True:
        pass_mk = int(input("please enter your credit at pass: "))
        while out_of_range(pass_mk) == "out of range":
            pass_mk = int(input("please enter your credit at pass: "))
            
        defer_mk = int(input("please enter your credit at pass: "))
        while out_of_range(defer_mk) == "out of range":
            defer_mk = int(input("please enter your credit at pass: "))
        
        fail_mk = int(input("please enter your credit at fail: "))
        while out_of_range(fail_mk) == "out of range":
            fail_mk = int(input("please enter your credit at fail: "))

        total(pass_mk,defer_mk,fail_mk)    


except ValueError:
  print("integer required")
 


