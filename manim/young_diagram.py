from manim import *

class YoungDiagram(Scene):
    def construct(self):
        # Title for the scene
        title = Text("Young Diagrams for Integer Partition", font_size=24, color=WHITE)
        title.to_edge(UP, buff=0.5)

        # Define partitions of 4
        partitions = [
            [4],
            [3, 1],
            [2, 2],
            [2, 1, 1],
            [1, 1, 1, 1]
        ]

        diagrams = VGroup()  # Group to hold all diagrams
        labels = VGroup()    # Group to hold all labels

        for i, partition in enumerate(partitions):
            # Create each diagram
            diagram = VGroup()
            for j, part in enumerate(partition):
                # Create a square for each part of the partition
                row = VGroup(*[Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.5, stroke_color=WHITE) for _ in range(part)])
                row.arrange(RIGHT, buff=0)  # Arrange squares in a row
                row.shift(j * DOWN * 0.6)  # Shift each row down
                diagram.add(row)

            diagram.arrange(DOWN, buff=0.05, aligned_edge=LEFT)  # Arrange rows

            if i == 0:
                # First diagram positioning
                diagram.to_edge(LEFT, buff=1)
            else:
                # Position based on the previous diagram's position
                diagram.next_to(diagrams[i - 1], RIGHT, buff=0.5)

            diagrams.add(diagram)

            # Add label below each diagram
            label = Text(f"Partition: {'+'.join(map(str, partition))}", font_size=16, color='Yellow').next_to(diagram, DOWN)
            labels.add(label)

        # Animate title, diagrams, and labels creation
        self.play(Write(title))
        self.wait(0.5)
        for diagram, label in zip(diagrams, labels):
            self.play(FadeIn(diagram), Write(label))
            self.wait(0.5)

        self.wait(2)

# To run this script, use the following command line:
# manim -pql file_name.py YoungDiagram
