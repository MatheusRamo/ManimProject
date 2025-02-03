from manim import *


class StackAnimation(Scene):
    def construct(self):
        #Initial settings
        self.camera.background_color = "#5F28C2"
        element_color = BLUE_D
        arrow_color = GOLD_D

        #Title
        title = Text("Funcionamento de uma Pilha", color=BLACK).to_edge(UP)
        self.play(Write(title))
        self.wait()

        #Stack base
        stack_base = Rectangle(
            width=2, height=0.5,
            color=element_color,
            fill_color=element_color,
            fill_opacity=0.7
        ).shift(DOWN*2)
        
        #Operations text
        op_text = Text("", color=BLACK, font_size=24).to_edge(UP).shift(DOWN*0.5)
        self.add(op_text)

        #Stack elements
        elements = VGroup()
        self.play(Create(stack_base))
        self.wait()

        #Function to update operation text
        def update_op_text(text):
            new_text = Text(text, color=BLACK, font_size=24).to_edge(UP).shift(DOWN*0.7)
            self.play(Transform(op_text, new_text))

        #Push Operations
        values = ["3", "5", "2"]
        current_top = stack_base.get_top()
        
        for val in values:
            #Create Element
            element = Rectangle(
                width=2, height=0.5,
                color=element_color,
                fill_color=element_color,
                fill_opacity=0.5
            )
            text = Text(val, color=WHITE, font_size=32)
            box = VGroup(element, text)
            
            #Positions element
            box.move_to(current_top + UP*0.5)
            
            #Push animation
            update_op_text(f"Push({val})")
            # arrow = Arrow(
            #     LEFT, RIGHT, 
            #     color=arrow_color,
            #     tip_length=0.2
            # ).next_to(box, LEFT, buff=0.5)
            
            self.play(
                box.animate.shift(LEFT*3),
                run_time=0.5
            )
            self.play(
                box.animate.shift(RIGHT*3),
                run_time=0.5
            )
            # self.play(FadeOut(arrow))
            
            elements.add(box)
            current_top = box.get_top()
            self.wait(0.5)

        #pop operations
        while len(elements) > 0:
            element = elements[-1]
            val = element[1].text
            
            #Pop animation
            update_op_text(f"Pop() → {val}")
            # arrow = Arrow(
            #     RIGHT, LEFT, 
            #     color=arrow_color,
            #     tip_length=0.2
            # ).next_to(element, RIGHT, buff=0.5)
            
            # self.play(GrowArrow(arrow))
            self.play(
                element.animate.shift(RIGHT*3),
                run_time=0.5
            )
            elements.remove(element)
            self.wait(0.5)

        self.wait(2)

