from manim import *
import numpy as np

def hardy_ramanujan_formula(n):
    return (1 / (4 * n * np.sqrt(3))) * np.exp(np.pi * np.sqrt(2 * n / 3))

class HardyRamanujanDemo(Scene):
    def construct(self):
        title = Text("Hardy-Ramanujan Asymptotic Expression for Partitions", font_size=24)
        title.to_edge(UP)

        explanation = Text(
            "Displays p(n) and approximations for values of n using the Hardy-Ramanujan formula",
            font_size=18,
            line_spacing=1.2
        )
        explanation.next_to(title, DOWN, buff=0.5)

        formula_text = Text(
            "p(n) ≈ 1 / (4n√3) * e^(π√(2n/3))",
            font_size=18,
            t2c={"n": YELLOW}  # highlighting mathematical symbols
        )
        formula_text.next_to(explanation, DOWN, buff=0.5)

        n_values = [20, 50, 100]
        actual_pn = [627, 204226, 190569292]  # hypothetical actual values for demonstration

        headers = ["n", "p(n) actual", "p(n) formula", "Ratio"]
        rows = [headers]

        for n, actual in zip(n_values, actual_pn):
            approx = hardy_ramanujan_formula(n)
            ratio = approx / actual
            rows.append([str(n), str(actual), f"{approx:.2f}", f"{ratio:.2f}"])

        # Create a table
        table = Table(rows, include_outer_lines=True)
        table.scale(0.7)
        table.next_to(formula_text, DOWN, buff=1)

        # Color the first column yellow
        for i in range(2, len(n_values)+2):  # Starting from 2 to skip header
            table.add_highlighted_cell((i, 1), color=YELLOW)

        self.play(Write(title))
        self.play(FadeIn(explanation))
        self.play(FadeIn(formula_text))
        self.play(Create(table))
        self.wait(2)

        # More detailed information or further calculations can be displayed here
        self.wait(2)

# To run this scene from the command line:
# manim -pql script_name.py HardyRamanujanDemo
