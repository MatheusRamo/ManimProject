from manim import *




class DivideAndConquerMax(Scene):
    def construct(self):
        elements = [3, 1, 4, 2]
        original_list = self.create_list(elements)
        self.play(Create(original_list))
        final_max = self.animate_divide_and_conquer(original_list)
        self.play(final_max.animate.scale(1.5).set_color(GOLD))
        self.wait(2)

    def create_list(self, elements):
        list_group = VGroup()
        for num in elements:
            box = Square(side_length=0.8)
            text = Text(str(num)).scale(0.7)
            group = VGroup(box, text)
            list_group.add(group)
        list_group.arrange(RIGHT, buff=1.0)
        return list_group

    def animate_divide_and_conquer(self, group):
        if len(group) == 1:
            self.play(group[0][1].animate.set_color(RED))
            return group[0][1]
        
        #Divide
        left, right = self.split_group(group)
        brace_left = Brace(left, UP)
        brace_right = Brace(right, UP)
        
        self.play(
            left.animate.shift(UP * 0.5 + LEFT),
            right.animate.shift(UP * 0.5 + RIGHT),
            FadeIn(brace_left),
            FadeIn(brace_right),
        )
        self.wait(0.5)
        
        #Recursion conquer
        left_max = self.animate_divide_and_conquer(left)
        right_max = self.animate_divide_and_conquer(right)
        
        #combine
        comparison_text = Text("Comparar:", font_size=24).next_to(group, DOWN * 2)
        arrow_left = Arrow(comparison_text.get_top(), left_max.get_center())
        arrow_right = Arrow(comparison_text.get_top(), right_max.get_center())
        
        self.play(
            FadeIn(comparison_text),
            Create(arrow_left),
            Create(arrow_right)
        )
        self.wait()
        
        max_text = left_max if int(left_max.text) > int(right_max.text) else right_max
        new_max = max_text.copy()
        self.play(
            new_max.animate.next_to(comparison_text, DOWN),
            FadeOut(arrow_left),
            FadeOut(arrow_right)
        )
        self.wait()
        
        #Fade Objects
        self.play(
            FadeOut(left),
            FadeOut(right),
            FadeOut(brace_left),
            FadeOut(brace_right),
            FadeOut(comparison_text),
            ReplacementTransform(new_max, group[0][1])
        )
        
        return group[0][1]

    def split_group(self, group):
        half = len(group) // 2
        left = VGroup(*group[:half]).copy()
        right = VGroup(*group[half:]).copy()
        return left, right