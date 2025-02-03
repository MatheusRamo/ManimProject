from manim import *

class LinearSearch(Scene):
    def construct(self):

        #Create a list of numbers
        items = np.linspace(1,10, 10)    
        table = IntegerTable([items], include_outer_lines=True)
        table.scale(0.7)

        #Add the table to the scene
        self.play(Write(table))
        
        #Create an arrow
        arrow = Arrow(start=UP, end=DOWN)
        arrow.scale(0.8)
        arrow.next_to(table.get_cell((1,1)), UP)
        
        #Add arrow to scene
        self.play(Create(arrow))
        
        #Move the arrow through the list elements
        for item in table.get_entries():
            arrow.set_color(RED)
            self.play(arrow.animate.next_to(item, UP))
            self.wait(0.5)

