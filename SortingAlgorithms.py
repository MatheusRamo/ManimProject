from manim import *
import random

class BubbleSortAnimation(Scene):

    def construct(self):
        #initial settings
        num_cards = 6
        card_width = 1.0
        card_height = 1.5
        spacing = 0.2
        
        #values = [7, 6, 5, 4, 1]  #Fixed example for easier visualization
        #Generate random numbers
        values = random.sample(range(1, num_cards+1), num_cards)
        
        #Create cards
        cards = VGroup(*[
            VGroup(
                Rectangle(width=card_width, height=card_height,
                        fill_color=BLUE_D, fill_opacity=0.8,
                        stroke_color=WHITE, stroke_width=2),
                Text(str(n), font_size=36)
            ).arrange(IN, buff=0.2)
            for n in values
        ])
        
        #Position cards
        cards.arrange(RIGHT, buff=spacing).shift(UP*0.5)
        
        #Title
        title = Text("Bubble Sort", font_size=40).to_edge(UP)
        self.add(title, cards)
        self.wait(0.5)
        
        #Bubble Sort Algorithm
        n = len(values)
        
        for i in range(n-1):
            for j in range(n-i-1):
                #Highlight elements being compared
                self.play(
                    cards[j].animate.set_fill(YELLOW),
                    cards[j+1].animate.set_fill(YELLOW),
                    run_time=0.5
                )
                self.wait(0.2)
                
                if values[j] > values[j+1]:
                    #Swap values ​​in the list
                    values[j], values[j+1] = values[j+1], values[j]
                    
                    #Swap card positions on screen
                    self.play(
                        cards[j].animate.move_to(cards[j+1].get_center()),
                        cards[j+1].animate.move_to(cards[j].get_center()),
                        run_time=1.0
                    )
                    
                    #Swap card references in VGroup
                    cards[j], cards[j+1] = cards[j+1], cards[j]
                    
                    #highlight swap cards
                    self.play(
                        cards[j].animate.set_fill(RED),
                        cards[j+1].animate.set_fill(RED),
                        run_time=0.5
                    )
                else:
                    #show element not sorting
                    self.play(
                        cards[j].animate.set_fill(ORANGE),
                        cards[j+1].animate.set_fill(ORANGE),
                        run_time=0.5
                    )
                
                #reset color
                self.play(
                    cards[j].animate.set_fill(BLUE_D),
                    cards[j+1].animate.set_fill(BLUE_D),
                    run_time=0.5
                )
                self.wait(0.2)
            
            #Set the color of the sorting element
            self.play(
                cards[n-i-1].animate.set_fill(GREEN),
                run_time=0.5
            )
        
        #Set the color of the sorting elements
        self.play(
            LaggedStart(*[card.animate.set_fill(GREEN) for card in cards], lag_ratio=0.2),
            run_time=2
        )
        self.play(cards.animate, run_time=1)
        self.wait(2)



class InsertionSortAnimation(Scene):

    def construct(self):
        #initial settings
        num_cards = 6
        card_width = 1.0
        card_height = 1.5
        spacing = 0.2
        
        #values = [7, 6, 5, 4, 1]  #Fixed example for easier visualization
        #Generate random numbers
        values = random.sample(range(1, num_cards+1), num_cards)
        
        #Create cards
        cards = VGroup(*[
            VGroup(
                Rectangle(width=card_width, height=card_height,
                        fill_color=BLUE_D, fill_opacity=0.8,
                        stroke_color=WHITE, stroke_width=2),
                Text(str(n), font_size=36)
            ).arrange(IN, buff=0.2)
            for n in values
        ])

        #Position cards
        cards.arrange(RIGHT, buff=spacing).shift(UP*0.5)
        
        #Title
        title = Text("Insertion Sort", font_size=40).to_edge(UP)
        self.add(title, cards)
        self.wait(0.5)
        
        #Algorithm Insertion Sorting
        n = len(values)
        
        for i in range(1, n):
            key_card = cards[i]

            key = values[i]
            #select key
            self.play(
                cards[i].animate.set_fill(RED),
                run_time=0.5
            )
            j = i - 1

            while j >= 0 and key < values[j]:
                #Highlight elements being compared
                self.play(
                    cards[j].animate.set_fill(YELLOW),
                    cards[j+1].animate.set_fill(YELLOW),
                    run_time=0.5
                )

                #Swap card positions on screen
                self.play(
                    cards[j].animate.move_to(cards[j+1].get_center()),
                    cards[j+1].animate.move_to(cards[j].get_center()),
                    run_time=1.0
                )
                self.wait(1.0)

                #reset colors
                self.play(
                    cards[j].animate.set_fill(BLUE_D),
                    cards[j+1].animate.set_fill(BLUE_D),
                    run_time=0.5
                )


                if ((j) > 0):                
                    #change key value color
                    key_card = cards[j+1]
                    self.play(
                        key_card.animate.set_fill(RED),
                        run_time=0.5
                    ) 
                    self.wait(0.5) 

                #Swap card references in VGroup
                cards[j], cards[j+1] = cards[j+1], cards[j]



                #exchange values ​​in the list
                values[j+1] = values[j]
                j -= 1
            values[j+1] = key

            #Reset key color
            self.play(
                cards[j+1].animate.set_fill(BLUE_D),
                run_time=0.5
            )
            self.wait(0.2)

        
        #Highlight all ordered elements
        self.play(
            LaggedStart(*[card.animate.set_fill(GREEN) for card in cards], lag_ratio=0.2),
            run_time=2
        )
        self.play(cards.animate, run_time=1)
        self.wait(2)