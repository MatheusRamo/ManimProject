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


class BinarySearch(MovingCameraScene):
    def construct(self):

        #Create a list of numbers
        items = np.linspace(1, 10, 10)
          
        table = IntegerTable([items], include_outer_lines=True)
        table.scale(0.7)

        
        mid = len(items)//2
        #Add the table to the scene
        table.move_to(UP)
        self.play(Write(table))

        #Create an arrow
        arrow = Arrow(start=UP, end=DOWN)
        arrow.scale(0.8)
        
        arrow.next_to(table.get_cell((1,mid)), UP)
        
        #Add arrow to scene
        self.play(Create(arrow))
        self.wait()



        table_low = IntegerTable([items[0:mid]], include_outer_lines=True)
        table_low.scale(0.7)

        table_high = IntegerTable([items[mid::]], include_outer_lines=True)
        table_high.scale(0.7)



        table_low.move_to(3*LEFT+DOWN)
        self.play(Write(table_low))

        table_high.move_to(3*RIGHT+DOWN)
        self.play(Write(table_high))
        


        #Get items from the table
        entries = table_low.get_entries()

        #Take the middle of the cell
        mid_cell = (entries[1].get_center() - entries[0].get_center() )/2
        
        #Move the arrow through the list elements
        for item in entries:
            cross = Cross().scale(0.5)
            self.play(cross.animate.move_to(item.get_center() + mid_cell, RIGHT), run_time=0.5)

        self.wait()


        #Move the camera to the high table
        self.play(self.camera.frame.animate.move_to(table_high).set(width=table_high.width * 1.05 ))
        self.wait(1)

        #Get items from the table
        entries_high = table_high.get_entries()
        mid_table = int(len(entries_high)/2)
        arrow.next_to(table_high.get_cell((1,mid_table+1)).get_center(), UP)
        self.wait(1)