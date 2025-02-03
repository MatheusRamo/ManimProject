from manim import *


class FactorialRecursion(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stack_vg = VGroup()
        self.popped_vg = VGroup()
        self.base_position = np.array([-3, -3, 0])
        self.size_scale = 1
        self.disk_height = 1
        self.side_position = np.array([3, 0, 0])

    def get_color(self, value):
        colors = [BLUE, GREEN, YELLOW, RED, PINK, ORANGE]
        return colors[value % len(colors)]
    
    def calculate_stack_position(self, index):
        x = self.base_position[0]
        y = self.base_position[1] + index * self.disk_height
        return np.array([x, y, 0])
    
    def calculate_pop_position(self, index):
        x = self.side_position[0]
        y = self.side_position[1] - index * self.disk_height
        return np.array([x, y, 0])

    def create_disk(self, value):
        width = (value + 1) * self.size_scale
        t = "Factorial {}".format(value)
        text = Text(str(t), color=BLACK, font_size=32)
        
        disk = Rectangle(
            width=width,
            height=self.disk_height,
            fill_color=self.get_color(value),
            fill_opacity=1,
            color=BLACK
        )
        box = VGroup(disk, text)
        disk.value = value
        return box
    
    def push(self, value):
        disk = self.create_disk(value)
        disk.move_to(UP * 3)
        self.add(disk)
        target_pos = self.calculate_stack_position(len(self.stack_vg))
        self.play(disk.animate.move_to(target_pos), run_time=0.5)
        self.stack_vg.add(disk)

    def pop(self):
        if len(self.stack_vg) == 0:
            return
        disk = self.stack_vg[-1]
        self.stack_vg.remove(disk)
        target_pos = self.calculate_pop_position(len(self.popped_vg))
        self.play(disk.animate.move_to(target_pos), run_time=0.5)
        self.popped_vg.add(disk)
    

    def construct(self):
        self.push(4)
        self.wait(1)

        self.push(3)
        self.wait(1)

        self.push(2)
        self.wait(1)

        self.push(1)
        self.wait(1)

        self.pop()
        self.wait(2)
        self.pop()
        self.wait(2)
        self.pop()
        self.wait(2)


