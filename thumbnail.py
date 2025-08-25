from manim import *
from math import sin, cos, pi

def extension(p1, p2, p3, p4):
    x1, y1 = p1.get_x(), p1.get_y()
    x2, y2 = p2.get_x(), p2.get_y()
    x3, y3 = p3.get_x(), p3.get_y()
    x4, y4 = p4.get_x(), p4.get_y()
    px = ((x1 * y2 - x2 * y1) * (x3 - x4) - (x3 * y4 - x4 * y3) * (x1 - x2)) / ((x1 - x2) * (y3 - y4) - (x3 - x4) * (y1 - y2))
    py = ((x1 * y2 - x2 * y1) * (y3 - y4) - (x3 * y4 - x4 * y3) * (y1 - y2)) / ((x1 - x2) * (y3 - y4) - (x3 - x4) * (y1 - y2))
    return Dot(point=(px, py, 0), radius=0.05)

class Some4Thumbnail(Scene):
    def construct(self):
        pascal = VGroup()
        radius = 2.0
        unitcircle = Circle(radius=radius, color=WHITE, stroke_width=1.1)
        pascal.add(unitcircle)
        f, c, e, a, d, b = 20, 50, 110, 160, 200, 290
        A = Dot(point=(radius * cos(a * pi / 180), radius * sin(a * pi / 180), 0), radius=0.05)
        B = Dot(point=(radius * cos(b * pi / 180), radius * sin(b * pi / 180), 0), radius=0.05)
        C = Dot(point=(radius * cos(c * pi / 180), radius * sin(c * pi / 180), 0), radius=0.05)
        D = Dot(point=(radius * cos(d * pi / 180), radius * sin(d * pi / 180), 0), radius=0.05)
        E = Dot(point=(radius * cos(e * pi / 180), radius * sin(e * pi / 180), 0), radius=0.05)
        F = Dot(point=(radius * cos(f * pi / 180), radius * sin(f * pi / 180), 0), radius=0.05)
        pascal.add(A, B, C, D, E, F)
        tex_labels = []
        for str, v, angle in [("A", A, a), ("B", B, b), ("C", C, c), ("D", D, d), ("E", E, e), ("F", F, f)]:
            label = (MathTex(str).scale(0.75).move_to(v.get_center() + 0.3 * (RIGHT * cos(angle * pi / 180) + UP * sin(angle * pi / 180))))
            tex_labels.append(label)
        pascal.add(*tex_labels)

        X = extension(A, B, D, E)
        x_angle = 200
        x_label = (MathTex("X").scale(0.75).move_to(X.get_center() + 0.3 * (RIGHT * cos(x_angle * pi / 180) + UP * sin(x_angle * pi / 180))))
        ab = Line(A.get_center(), B.get_center())
        de = Line(D.get_center(), E.get_center())
        pascal.add(X, x_label, ab, de)

        Y = extension(B, C, E, F)
        y_angle = 30
        y_label = (MathTex("Y").scale(0.75).move_to(Y.get_center() + 0.3 * (RIGHT * cos(y_angle * pi / 180) + UP * sin(y_angle * pi / 180))))
        bc = Line(B.get_center(), C.get_center())
        ef = Line(E.get_center(), F.get_center())
        pascal.add(Y, y_label, bc, ef)

        Z = extension(C, D, F, A)
        z_angle = 100
        z_label = (MathTex("Z").scale(0.75).move_to(Z.get_center() + 0.3 * (RIGHT * cos(z_angle * pi / 180) + UP * sin(z_angle * pi / 180))))
        cd = Line(C.get_center(), D.get_center())
        fa = Line(F.get_center(), A.get_center())
        pascal.add(Z, z_label, cd, fa)

        xyz = DashedLine(X.get_center(), Y.get_center())
        pascal.add(xyz)

        ab.stroke_width = 3.0
        cd.stroke_width = 3.0
        ef.stroke_width = 3.0
        ab.set_color(YELLOW)
        cd.set_color(YELLOW)
        ef.set_color(YELLOW)
        bc.stroke_width = 3.0
        de.stroke_width = 3.0
        fa.stroke_width = 3.0
        bc.set_color(BLUE)
        de.set_color(BLUE)
        fa.set_color(BLUE)
        unitcircle.stroke_width = 3.0
        unitcircle.set_color(PINK)
        pascal.scale(1.2).shift(0.5 * DOWN)
        self.add(pascal)

        pascal_text = Text("Pascal's Theorem", font_size=120)
        pascal_text.shift(3 * UP)
        self.add(pascal_text)
    
