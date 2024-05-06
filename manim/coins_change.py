# Use Python Manim to demenstarte the Coins Change Problem
# Ethan Li


from manim import *

class CoinCombination(Scene):
    def construct(self):
        # Title text
        title_text = Text("How many ways can you change one dollar?", font_size=36, color=BLUE)
        title_text.to_edge(UP)

        # Create coin representations and labels
        coins = VGroup()
        values = [1, 5, 10, 25, 50]
        labels = ["1 cent", "5 cents", "10 cents", "25 cents", "50 cents"]
        for i, (value, label) in enumerate(zip(values, labels)):
            # Coin circle
            coin = Circle(radius=0.5, color=GOLD_E, fill_opacity=0.5)
            coin_text = Text(label, font_size=24).move_to(coin.get_center())
            coin_group = VGroup(coin, coin_text).shift(RIGHT * i * 1.5)

            # Question mark for each coin type
            question_mark = Text("?", font_size=36, color=RED).next_to(coin, UP)

            # Grouping the coin with the question mark
            coins.add(VGroup(coin_group, question_mark))

        # Arrange all coins in a line
        coins.arrange(RIGHT, buff=0.75)

        # Display title and coins
        self.play(Write(title_text), run_time=2)
        self.wait(1)
        self.play(FadeIn(coins), run_time=2)
        self.wait(1)

        # Create '+' signs and position them
        plus_signs = VGroup()
        for i in range(len(coins) - 1):
            plus = Text("+", font_size=36).next_to(coins[i], RIGHT, buff=0.2)
            plus_signs.add(plus)

        # Display '+' signs
        self.play(*[Write(sign) for sign in plus_signs], run_time=1)
        self.wait(1)

        # '=' sign and total
        equals_sign = Text("=", font_size=36).next_to(coins[-1], RIGHT, buff=0.2)
        total_dollar = Text("1 dollar", font_size=36).next_to(equals_sign, RIGHT, buff=0.2)

        # Display '=' and total
        self.play(Write(equals_sign), Write(total_dollar))
        self.wait(2)

# To execute this animation, save the script and run the following command:
# manim -pql coin_combination.py CoinCombination
