from manim import *


class DisplayCode(Scene):
    def construct(self):
        #Code to shown on display
        code = '''
        def pesquisa_binaria(lista, item):
            baixo = 0
            alto = len(lista) - 1
            while baixo <=alto:
                meio = (baixo + alto) / 2
                chute = lista[meio]
                if chute == item:
                    return meio
                if chute > item:
                    alto = meio - 1
                else:
                    baixo = meio + 1
            return None
        '''

        color = "#5F28C2"
        rendered_code = Code(code=code, tab_width=4, background_stroke_color=color, background="window", language="Python", font="Monospace")

        #Animation Letter for Letter
        for i, letter in enumerate(rendered_code):
            self.play(Create(letter, run_time=1))
        self.wait(2)

        #Animation line for line
        for i, line in enumerate(rendered_code.code):
            self.play(Indicate(line, color=DARK_BLUE), run_time=1)
            self.wait(0.5)

