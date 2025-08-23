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

class Some4(Scene):
    def construct(self):
        # settings
        Line.set_default(stroke_width=0.9)

        # pascal diagram
        self.wait()
        pascal = VGroup()
        radius = 2.0
        unitcircle = Circle(radius=radius, color=WHITE, stroke_width=1.1)
        self.play(Create(unitcircle))
        pascal.add(unitcircle)
        self.wait()
        a, b, c, d, e, f = 20, 50, 110, 160, 200, 290
        A = Dot(point=(radius * cos(a * pi / 180), radius * sin(a * pi / 180), 0), radius=0.05)
        B = Dot(point=(radius * cos(b * pi / 180), radius * sin(b * pi / 180), 0), radius=0.05)
        C = Dot(point=(radius * cos(c * pi / 180), radius * sin(c * pi / 180), 0), radius=0.05)
        D = Dot(point=(radius * cos(d * pi / 180), radius * sin(d * pi / 180), 0), radius=0.05)
        E = Dot(point=(radius * cos(e * pi / 180), radius * sin(e * pi / 180), 0), radius=0.05)
        F = Dot(point=(radius * cos(f * pi / 180), radius * sin(f * pi / 180), 0), radius=0.05)
        self.play(Create(A), Create(B), Create(C), Create(D), Create(E), Create(F))
        pascal.add(A, B, C, D, E, F)
        tex_labels = []
        for str, v, angle in [("A", A, a), ("B", B, b), ("C", C, c), ("D", D, d), ("E", E, e), ("F", F, f)]:
            label = (MathTex(str).scale(0.75).move_to(v.get_center() + 0.5 * (RIGHT * cos(angle * pi / 180) + UP * sin(angle * pi / 180))))
            tex_labels.append(label)
        self.play(Create(VGroup(*tex_labels)))
        pascal.add(*tex_labels)
        self.wait()

        abcdef = MathTex("A", "B", "C", "D", "E", "F").scale(0.5).to_edge(UR)
        self.play(pascal.animate.scale(0.5).shift(DOWN), Write(abcdef))
        self.wait(3)

        pascal_tex = VGroup()

        X = extension(A, B, D, E).scale(0.5)
        x_angle = 90
        x_label = (MathTex("X").scale(0.75).scale(0.5).move_to(X.get_center() + 0.3 * (RIGHT * cos(x_angle * pi / 180) + UP * sin(x_angle * pi / 180))))
        ax = Line(A.get_center(), X.get_center())
        ex = Line(E.get_center(), X.get_center())
        abcdefx = abcdef.copy()
        self.add(abcdefx)
        self.play(Create(ax), Create(ex), abcdefx.animate.shift(4.0 * DOWN))
        x_text = MathTex(r"X=AB\cap DE \leftarrow").scale(0.5).move_to(abcdefx, LEFT).shift(2 * LEFT)
        self.play(Create(X), Create(x_label), Write(x_text), abcdefx[0:2].animate.set_fill(color=PURE_BLUE), abcdefx[3:5].animate.set_fill(color=PURE_GREEN))
        self.wait(2)
        pascal.add(X, x_label, ax, ex)
        pascal_tex.add(abcdefx, x_text)

        Y = extension(B, C, E, F).scale(0.5)
        y_angle = 90
        y_label = (MathTex("Y").scale(0.75).scale(0.5).move_to(Y.get_center() + 0.3 * (RIGHT * cos(y_angle * pi / 180) + UP * sin(y_angle * pi / 180))))
        by = Line(B.get_center(), Y.get_center())
        fy = Line(F.get_center(), Y.get_center())
        abcdefy = abcdef.copy()
        self.add(abcdefy)
        self.play(Create(by), Create(fy), abcdefy.animate.shift(4.5 * DOWN))
        y_text = MathTex(r"Y=BC\cap EF \leftarrow").scale(0.5).move_to(abcdefy, LEFT).shift(2 * LEFT)
        self.play(Create(Y), Create(y_label), Write(y_text), abcdefy[1:3].animate.set_fill(color=PURE_BLUE), abcdefy[4:6].animate.set_fill(color=PURE_GREEN))
        self.wait(2)
        pascal.add(Y, y_label, by, fy)
        pascal_tex.add(abcdefy, y_text)

        Z = extension(C, D, F, A).scale(0.5)
        z_angle = 90
        z_label = (MathTex("Z").scale(0.75).scale(0.5).move_to(Z.get_center() + 0.3 * (RIGHT * cos(z_angle * pi / 180) + UP * sin(z_angle * pi / 180))))
        dz = Line(D.get_center(), Z.get_center())
        fz = Line(F.get_center(), Z.get_center())
        abcdefz = abcdef.copy()
        self.add(abcdefz)
        self.play(Create(dz), Create(fz), abcdefz.animate.shift(5.0 * DOWN))
        z_text = MathTex(r"Z=CD\cap FA \leftarrow").scale(0.5).move_to(abcdefz, LEFT).shift(2 * LEFT)
        self.play(Create(Z), Create(z_label), Write(z_text), abcdefz[0].animate.set_fill(color=PURE_GREEN), abcdefz[2:4].animate.set_fill(color=PURE_BLUE), abcdefz[5].animate.set_fill(color=PURE_GREEN))
        self.wait(2)
        pascal.add(Z, z_label, dz, fz)
        pascal_tex.add(abcdefz, z_text)

        xyz = DashedLine(Y.get_center(), Z.get_center())
        self.play(Create(xyz))
        self.wait(2)
        pascal.add(xyz)

        animations_out = [
            FadeOut(*tex_labels, shift=LEFT),
            FadeOut(*[A, B, C, D, E, F], shift=LEFT),
            FadeOut(*[X, Y, Z], shift=LEFT),
            FadeOut(*[x_label, y_label, z_label], shift=LEFT),
            FadeOut(*[ax, ex, by, fy, dz, fz], shift=LEFT),
            FadeOut(*[unitcircle, xyz], shift=LEFT)
        ]

        self.play(AnimationGroup(animations_out), FadeOut(pascal_tex, shift=RIGHT), run_time=2.0)
        self.wait(2)


        # pascal diagram 2
        pascal = VGroup()
        radius = 2.0
        unitcircle = Circle(radius=radius, color=WHITE, stroke_width=1.1)
        self.play(Create(unitcircle))
        pascal.add(unitcircle)
        self.wait()
        f, c, e, a, d, b = 20, 50, 110, 160, 200, 290
        A = Dot(point=(radius * cos(a * pi / 180), radius * sin(a * pi / 180), 0), radius=0.05)
        B = Dot(point=(radius * cos(b * pi / 180), radius * sin(b * pi / 180), 0), radius=0.05)
        C = Dot(point=(radius * cos(c * pi / 180), radius * sin(c * pi / 180), 0), radius=0.05)
        D = Dot(point=(radius * cos(d * pi / 180), radius * sin(d * pi / 180), 0), radius=0.05)
        E = Dot(point=(radius * cos(e * pi / 180), radius * sin(e * pi / 180), 0), radius=0.05)
        F = Dot(point=(radius * cos(f * pi / 180), radius * sin(f * pi / 180), 0), radius=0.05)
        self.play(Create(A), Create(B), Create(C), Create(D), Create(E), Create(F))
        pascal.add(A, B, C, D, E, F)
        tex_labels = []
        for str, v, angle in [("A", A, a), ("B", B, b), ("C", C, c), ("D", D, d), ("E", E, e), ("F", F, f)]:
            label = (MathTex(str).scale(0.75).move_to(v.get_center() + 0.5 * (RIGHT * cos(angle * pi / 180) + UP * sin(angle * pi / 180))))
            tex_labels.append(label)
        self.play(Create(VGroup(*tex_labels)))
        pascal.add(*tex_labels)
        self.wait()

        pascal_tex = VGroup()

        X = extension(A, B, D, E)
        x_angle = 200
        x_label = (MathTex("X").scale(0.75).move_to(X.get_center() + 0.3 * (RIGHT * cos(x_angle * pi / 180) + UP * sin(x_angle * pi / 180))))
        ab = Line(A.get_center(), B.get_center())
        de = Line(D.get_center(), E.get_center())
        abcdefx = abcdef.copy()
        self.add(abcdefx)
        self.play(Create(ab), Create(de), abcdefx.animate.shift(4.0 * DOWN))
        x_text = MathTex(r"X=AB\cap DE \leftarrow").scale(0.5).move_to(abcdefx, LEFT).shift(2 * LEFT)
        self.play(Create(X), Create(x_label), Write(x_text), abcdefx[0:2].animate.set_fill(color=PURE_BLUE), abcdefx[3:5].animate.set_fill(color=PURE_GREEN))
        self.wait(2)
        pascal.add(X, x_label, ab, de)
        pascal_tex.add(abcdefx, x_text)

        Y = extension(B, C, E, F)
        y_angle = 30
        y_label = (MathTex("Y").scale(0.75).move_to(Y.get_center() + 0.3 * (RIGHT * cos(y_angle * pi / 180) + UP * sin(y_angle * pi / 180))))
        bc = Line(B.get_center(), C.get_center())
        ef = Line(E.get_center(), F.get_center())
        abcdefy = abcdef.copy()
        self.add(abcdefy)
        self.play(Create(bc), Create(ef), abcdefy.animate.shift(4.5 * DOWN))
        y_text = MathTex(r"Y=BC\cap EF \leftarrow").scale(0.5).move_to(abcdefy, LEFT).shift(2 * LEFT)
        self.play(Create(Y), Create(y_label), Write(y_text), abcdefy[1:3].animate.set_fill(color=PURE_BLUE), abcdefy[4:6].animate.set_fill(color=PURE_GREEN))
        self.wait(2)
        pascal.add(Y, y_label, bc, ef)
        pascal_tex.add(abcdefy, y_text)

        Z = extension(C, D, F, A)
        z_angle = 100
        z_label = (MathTex("Z").scale(0.75).move_to(Z.get_center() + 0.3 * (RIGHT * cos(z_angle * pi / 180) + UP * sin(z_angle * pi / 180))))
        cd = Line(C.get_center(), D.get_center())
        fa = Line(F.get_center(), A.get_center())
        abcdefz = abcdef.copy()
        self.add(abcdefz)
        self.play(Create(cd), Create(fa), abcdefz.animate.shift(5.0 * DOWN))
        z_text = MathTex(r"Z=CD\cap FA \leftarrow").scale(0.5).move_to(abcdefz, LEFT).shift(2 * LEFT)
        self.play(Create(Z), Create(z_label), Write(z_text), abcdefz[0].animate.set_fill(color=PURE_GREEN), abcdefz[2:4].animate.set_fill(color=PURE_BLUE), abcdefz[5].animate.set_fill(color=PURE_GREEN))
        self.wait(2)
        pascal.add(Z, z_label, cd, fa)
        pascal_tex.add(abcdefz, z_text)

        xyz = DashedLine(X.get_center(), Y.get_center())
        self.play(Create(xyz))
        self.wait(2)
        pascal.add(xyz)

        animations_out = [
            FadeOut(*tex_labels, shift=LEFT),
            FadeOut(*[A, B, C, D, E, F], shift=LEFT),
            FadeOut(*[X, Y, Z], shift=LEFT),
            FadeOut(*[x_label, y_label, z_label], shift=LEFT),
            FadeOut(*[ab, de, bc, ef, cd, fa], shift=LEFT),
            FadeOut(*[unitcircle, xyz], shift=LEFT)
        ]

        self.play(AnimationGroup(animations_out), FadeOut(pascal_tex, shift=RIGHT), FadeOut(abcdef, shift=UP), run_time=2.0)
        self.wait(2)


        # pascal
        self.wait(3)
        pascal_text = Text("Pascal's Theorem", font_size=60)
        self.play(Write(pascal_text), run_time=2)
        self.wait(2)
        latin_text = Text("hexagrammum mysticum", font_size=24, slant=ITALIC, color=BLUE).shift(DOWN * 1)
        self.play(FadeIn(latin_text))
        self.wait()
        eng_text = Text("mystical hexagram", font_size=24, slant=ITALIC, color=GREEN).shift(DOWN * 1.5)
        self.play(FadeIn(eng_text))
        self.wait()
        self.play(FadeOut(pascal_text), FadeOut(latin_text), FadeOut(eng_text))
        self.wait(2)


        # possible proofs
        self.wait()

        bezout_group = VGroup()
        bezout = Text("Bézout's Theorem")
        bezout_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        bezout_box.surround(bezout)
        bezout_group.add(bezout_box, bezout)
        self.add(bezout_group)
        self.wait()

        isogonal_group = VGroup()
        isogonal = Text("Isogonal Conjugates")
        isogonal_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        isogonal_box.surround(isogonal)
        isogonal_group.add(isogonal_box, isogonal)
        isogonal_group.rotate(40)
        self.add(isogonal_group)
        self.wait()

        cross_group = VGroup()
        cross = Text("Cross Ratio")
        cross_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        cross_box.surround(cross)
        cross_group.add(cross_box, cross)
        cross_group.rotate(100)
        self.add(cross_group)
        self.wait()

        menelaus_group = VGroup()
        menelaus = Text("Menelaus")
        menelaus_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        menelaus_box.surround(menelaus)
        menelaus_group.add(menelaus_box, menelaus)
        menelaus_group.rotate(400)
        self.add(menelaus_group)
        self.wait()

        homothety_group = VGroup()
        homothety = Text("Homothety")
        homothety_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        homothety_box.surround(homothety)
        homothety_group.add(homothety_box, homothety)
        homothety_group.rotate(220)
        self.add(homothety_group)
        self.wait()

        self.wait()
        self.play(
            ChangeSpeed(
                homothety_group.animate.shift(RIGHT * 10),
                speedinfo={0.0: 0.1, 1.5: 1.0},
                rate_func=linear,
            )
        )
        self.play(
            ChangeSpeed(
                menelaus_group.animate.shift(LEFT * 10),
                speedinfo={0.0: 0.1, 1.5: 1.0},
                rate_func=linear,
            )
        )
        self.play(
            ChangeSpeed(
                cross_group.animate.shift(UP * 10),
                speedinfo={0.0: 0.1, 1.5: 1.0},
                rate_func=linear,
            )
        )
        self.play(
            ChangeSpeed(
                isogonal_group.animate.shift(DOWN * 10),
                speedinfo={0.0: 0.1, 1.5: 1.0},
                rate_func=linear,
            )
        )
        self.wait()
        self.play(bezout_group.animate.scale(2.0))
        self.play(FadeOut(bezout_group))
        self.clear()
        self.wait()


        # curves
        title = Tex(r"What is an algebraic curve?", font_size=48)
        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(title.animate.shift(UP))

        curve = Tex(r"$\mathcal{C}=\{(x,y):P(x,y)=0\}$", font_size=30)
        self.play(Write(curve), run_time=2)
        self.wait(2)
        self.play(title.animate.shift(UP), curve.animate.shift(UP))

        degree = Tex(r"$\deg(\mathcal{C})=\deg(P)=\max(i+j:P(x,y)=\cdots+c_{i,j}x^iy^j+\cdots,\;c_{i,j}\neq 0)$", font_size=30)
        self.play(Write(degree), run_time=2)
        self.wait(2)
        self.play(title.animate.shift(UP), curve.animate.shift(UP), degree.animate.shift(UP))

        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            }
        )
        number_plane.set_z_index(-10)

        elliptic = Tex(r"$P(x,y)=y^2-x^3-3$", font_size=30)
        elliptic_group = VGroup()
        elliptic_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        elliptic_box.surround(elliptic)
        elliptic_group.add(elliptic_box, elliptic)
        elliptic_graph = ImplicitFunction(lambda x, y: y * y - x ** 3 - 3, color=YELLOW)
        self.play(Write(elliptic), run_time=2)
        self.wait(2)
        self.play(elliptic_group.animate.shift(2 * UP + 3 * LEFT), FadeOut(title, shift=RIGHT), FadeOut(curve, shift=RIGHT), FadeOut(degree, shift=RIGHT))
        self.wait(2)
        self.play(Create(elliptic_graph))
        self.play(FadeIn(number_plane))
        self.wait(2)

        circle = Tex(r"$P(x,y)=x^2+y^2-1$", font_size=30).shift(2 * UP + 3 * LEFT)
        circle_group = VGroup()
        circle_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        circle_box.surround(circle)
        circle_group.add(circle_box, circle)
        circle_graph = ImplicitFunction(lambda x, y: x ** 2 + y ** 2 - 1, color=YELLOW)
        self.play(FadeOut(number_plane, shift=LEFT), FadeOut(elliptic_graph, shift=LEFT), FadeOut(elliptic_group, shift=LEFT))
        self.play(Write(circle_group), FadeIn(number_plane, shift=LEFT), FadeIn(circle_graph, shift=LEFT))
        self.wait(2)

        line = Tex(r"$P(x,y)=y-2x-3$", font_size=30).shift(2 * UP + 3 * LEFT)
        line_group = VGroup()
        line_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        line_box.surround(line)
        line_group.add(line_box, line)
        line_graph = ImplicitFunction(lambda x, y: y - 2 * x - 3, color=YELLOW)
        self.play(FadeOut(number_plane, shift=LEFT), FadeOut(circle_graph, shift=LEFT), FadeOut(circle_group, shift=LEFT))
        self.play(Write(line_group), FadeIn(number_plane, shift=LEFT), FadeIn(line_graph, shift=LEFT))
        self.wait(2)

        line2 = Tex(r"$P(x,y)=(y-2x-3)^2$", font_size=30).shift(2 * UP + 3 * LEFT)
        line2[0][15:16].set_color(RED)
        line2_group = VGroup()
        line2_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        line2_box.surround(line2)
        line2_group.add(line2_box, line2)
        self.play(Transform(line_group, line2_group))
        self.wait(2)

        two_lines = Tex(r"$P(x,y)=(y-2x-3)(3y-x+1)$", font_size=30).shift(2 * UP + 3.6 * LEFT)
        two_lines_group = VGroup()
        two_lines_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        two_lines_box.surround(two_lines)
        two_lines_box = Rectangle(height=two_lines_box.height / 2, width=two_lines_box.width, fill_color=BLACK, fill_opacity=1.0).move_to(two_lines.get_center())
        two_lines_group.add(two_lines_box, two_lines)
        two_lines_graph = ImplicitFunction(lambda x, y: (y - 2 * x - 3) * (3 * y - x + 1), color=YELLOW)
        self.play(FadeOut(number_plane, shift=LEFT), FadeOut(line_graph, shift=LEFT), FadeOut(*[line_group, line2_group], shift=LEFT))
        self.play(Write(two_lines_group), FadeIn(number_plane, shift=LEFT), FadeIn(two_lines_graph, shift=LEFT))
        self.wait(2)
        self.play(FadeOut(number_plane), FadeOut(two_lines_group, shift=LEFT), FadeOut(two_lines_graph, shift=LEFT))
        self.wait(2)


        # intersection of curves
        self.play(FadeIn(number_plane))
        self.wait(2)

        p = Tex(r"$P(x,y)=y-2x-3$", font_size=30, color=YELLOW).shift(2 * UP + 3.6 * LEFT)
        p_group = VGroup()
        p_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        p_box.surround(p)
        p_group.add(p_box, p)
        p_graph = ImplicitFunction(lambda x, y: y - 2 * x - 3, color=YELLOW)
        self.play(FadeIn(p_group, shift=RIGHT), FadeIn(p_graph))
        self.wait()

        q = Tex(r"$Q(x,y)=3y-x+1$", font_size=30, color=BLUE).shift(0.4 * UP + 3.6 * LEFT)
        q_group = VGroup()
        q_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        q_box.surround(q)
        q_group.add(q_box, q)
        q_graph = ImplicitFunction(lambda x, y: 3 * y - x + 1, color=BLUE)
        self.play(FadeIn(q_group, shift=RIGHT), FadeIn(q_graph))
        self.wait()

        pq = Dot([-2, -1, 0], radius=0.1)
        self.play(Create(pq))
        self.wait()
        self.play(FocusOn(pq))
        self.wait()

        self.play(FadeOut(p_group, shift=LEFT), FadeOut(p_graph), FadeOut(pq))

        circle = Tex(r"$P(x,y)=x^2+y^2-1$", font_size=30, color=YELLOW).shift(2 * UP + 3.6 * LEFT)
        circle_group = VGroup()
        circle_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        circle_box.surround(circle)
        circle_box = Rectangle(height=0.7 * circle_box.height, width=circle_box.width, fill_color=BLACK, fill_opacity=1.0).move_to(circle.get_center())
        circle_group.add(circle_box, circle)
        circle_graph = ImplicitFunction(lambda x, y: x ** 2 + y ** 2 - 1, color=YELLOW)
        self.play(FadeIn(circle_group, shift=RIGHT), FadeIn(circle_graph))
        self.wait()

        u = Dot([1, 0, 0], radius=0.1)
        v = Dot([-0.8, -0.6, 0], radius=0.1)
        self.play(Create(u), Create(v))
        self.wait()
        self.play(FocusOn(u), FocusOn(v))
        self.wait()

        self.play(FadeOut(q_group, shift=LEFT), FadeOut(q_graph), FadeOut(u), FadeOut(v))

        elliptic = Tex(r"$Q(x,y)=y^2-8x^3+3x-1$", font_size=30, color=BLUE).shift(0.4 * UP + 3.6 * LEFT)
        elliptic_group = VGroup()
        elliptic_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        elliptic_box.surround(elliptic)
        elliptic_box = Rectangle(height=elliptic_box.height / 2, width=elliptic_box.width, fill_color=BLACK, fill_opacity=1.0).move_to(elliptic.get_center())
        elliptic_group.add(elliptic_box, elliptic)
        elliptic_graph = ImplicitFunction(lambda x, y: y ** 2 - 8 * x ** 3 + 3 * x - 1, color=BLUE)
        self.play(FadeIn(elliptic_group, shift=RIGHT), FadeIn(elliptic_graph))
        self.wait()

        p1 = Dot([0.553, 0.833, 0], radius=0.1)
        p2 = Dot([0, 1.0, 0], radius=0.1)
        p3 = Dot([-0.678, 0.735, 0], radius=0.1)
        p4 = Dot([0.553, -0.833, 0], radius=0.1)
        p5 = Dot([0, -1.0, 0], radius=0.1)
        p6 = Dot([-0.678, -0.735, 0], radius=0.1)
        self.play(Create(p1), Create(p2), Create(p3), Create(p4), Create(p5), Create(p6))
        self.wait()
        self.play(FocusOn(p1), FocusOn(p2), FocusOn(p3), FocusOn(p4), FocusOn(p5), FocusOn(p6))
        self.wait()

        self.play(FadeOut(elliptic_group, shift=LEFT), FadeOut(circle_group, shift=LEFT), FadeOut(elliptic_graph), FadeOut(circle_graph), FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4), FadeOut(p5), FadeOut(p6), ) # FadeOut(number_plane)


        a = Tex(r"$P(x,y)=y-3x^3+3x$", font_size=30, color=YELLOW).shift(2 * UP + 3.6 * LEFT)
        a_group = VGroup()
        a_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        a_box.surround(a)
        a_box = Rectangle(height=a_box.height / 2, width=a_box.width, fill_color=BLACK, fill_opacity=1.0).move_to(a.get_center())
        a_group.add(a_box, a)
        a_graph = ImplicitFunction(lambda x, y: y - 3 * (x ** 3) + 3 * x, color=YELLOW)
        self.play(FadeIn(a_group, shift=RIGHT), FadeIn(a_graph))
        self.wait()

        b = Tex(r"$Q(x,y)=x-3y^3+3y$", font_size=30, color=BLUE).shift(0.4 * UP + 3.6 * LEFT)
        b_group = VGroup()
        b_box = Rectangle(fill_color=BLACK, fill_opacity=1.0)
        b_box.surround(b)
        b_box = Rectangle(height=b_box.height / 2, width=b_box.width, fill_color=BLACK, fill_opacity=1.0).move_to(b.get_center())
        b_group.add(b_box, b)
        b_graph = ImplicitFunction(lambda x, y: x - 3 * (y ** 3) + 3 * y, color=BLUE)
        self.play(FadeIn(b_group, shift=RIGHT), FadeIn(b_graph))
        self.wait()

        p1 = Dot([-0.816, 0.816, 0], radius=0.1)
        p2 = Dot([-0.357, 0.934, 0], radius=0.1)
        p3 = Dot([1.155, 1.155, 0], radius=0.1)
        p4 = Dot([-0.934, 0.357, 0], radius=0.1)
        p5 = Dot([0, 0, 0], radius=0.1)
        p6 = Dot([0.934, -0.357, 0], radius=0.1)
        p7 = Dot([-1.155, -1.155, 0], radius=0.1)
        p8 = Dot([0.357, -0.934, 0], radius=0.1)
        p9 = Dot([0.816, -0.816, 0], radius=0.1)
        self.play(Create(p1), Create(p2), Create(p3), Create(p4), Create(p5), Create(p6), Create(p7), Create(p8), Create(p9))
        self.wait()
        self.play(FocusOn(p1), FocusOn(p2), FocusOn(p3), FocusOn(p4), FocusOn(p5), FocusOn(p6), FocusOn(p7), FocusOn(p8), FocusOn(p9))
        self.wait()

        self.play(FadeOut(a_group, shift=LEFT), FadeOut(b_group, shift=LEFT), FadeOut(a_graph), FadeOut(b_graph), FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4), FadeOut(p5), FadeOut(p6), FadeOut(p7), FadeOut(p8), FadeOut(p9), FadeOut(number_plane))

        self.wait(2)

        title = Tex(r"Bézout's Theorem", font_size=48)
        sep = Line([-2.3, 0.6, 0], [2.3, 0.6, 0], stroke_width=2.0)
        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(title.animate.shift(UP))
        self.play(Create(sep))

        poly_p = Tex(r"$$\mathcal{C}:\quad P(x,y)=\sum_{i+j\leq n}c_{i,j}x^iy^j$$", font_size=30, color=YELLOW)
        self.play(Write(poly_p), run_time=2)
        self.wait(2)
        self.play(title.animate.shift(UP), sep.animate.shift(UP), poly_p.animate.shift(UP))
        self.wait()

        poly_q = Tex(r"$$\mathcal{D}:\quad Q(x,y)=\sum_{i+j\leq m}d_{i,j}x^iy^j$$", font_size=30, color=BLUE)
        self.play(Write(poly_q), run_time=2)
        self.wait(2)
        self.play(title.animate.shift(UP), sep.animate.shift(UP), poly_p.animate.shift(UP), poly_q.animate.shift(UP))
        self.wait()

        pq = Tex(r"$$|\mathcal{C}\cap\mathcal{D}|\leq nm$$", font_size=30)
        pq_box = Rectangle()
        pq_box.surround(pq)
        self.play(Write(pq), Create(pq_box), run_time=2)
        self.wait() # (eğer nm den fazla ise tek bir olasılık var, bu curvelerin common componenti var, o zaman da zaten sonsuz)
        self.play(LaggedStart(
            Unwrite(title),
            FadeOut(sep),
            Unwrite(poly_p),
            Unwrite(poly_q),
            FadeOut(pq_box),
            Unwrite(pq),
            lag_ratio=0.25,
            run_time=3
        ))
        self.wait()


        # proof of pascal using bezout
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
            label = (MathTex(str).scale(0.75).move_to(v.get_center() + 0.5 * (RIGHT * cos(angle * pi / 180) + UP * sin(angle * pi / 180))))
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

        self.play(FadeIn(pascal))
        self.wait(2)
        self.play(pascal.animate.shift(3 * RIGHT).scale(1.2))
        self.wait()

        title = Tex(r"Proof", font_size=48, color=RED).shift(5 * LEFT + 3.2 * UP)
        sep = Line(stroke_width=2.0, color=RED).move_to(title.get_center() + 0.3 * DOWN)
        self.play(Write(title), Create(sep))
        self.wait(2)
        c = Tex(r"$$\mathcal{C}:\quad P_3(x,y)=AB\times CD\times EF$$", font_size=30, color=YELLOW).shift(4 * LEFT + 2.5 * UP)
        ab.stroke_width = 3.0
        cd.stroke_width = 3.0
        ef.stroke_width = 3.0
        self.play(ab.animate.set_color(YELLOW), cd.animate.set_color(YELLOW), ef.animate.set_color(YELLOW), Write(c))
        self.wait(2)
        d = Tex(r"$$\mathcal{D}:\quad Q_3(x,y)=BC\times DE\times FA$$", font_size=30, color=BLUE).shift(3 * LEFT + 2.0 * UP)
        d.align_to(c, LEFT)
        bc.stroke_width = 3.0
        de.stroke_width = 3.0
        fa.stroke_width = 3.0
        self.play(bc.animate.set_color(BLUE), de.animate.set_color(BLUE), fa.animate.set_color(BLUE), Write(d))
        self.wait(2)
        cd = Tex(r"$$\mathcal{C}\cap\mathcal{D}=\{A,B,C,D,E,F,X,Y,Z\}$$", font_size=30).shift(3 * LEFT + 1.5 * UP)
        self.play(Write(cd))
        self.wait(2)
        self.play(Unwrite(cd))
        e = Tex(r"$$\mathcal{E}:\quad R_2(x,y)=\text{Circle}$$", font_size=30, color=PINK).shift(3 * LEFT + 1.5 * UP)
        e.align_to(c, LEFT)
        unitcircle.stroke_width = 3.0
        self.play(unitcircle.animate.set_color(PINK), Write(e))
        self.wait(2)
        ce = Tex(r"$$\mathcal{C}\cap\mathcal{E}=\{A,B,C,D,E,F\}$$", font_size=30).shift(3 * LEFT + 1.0 * UP)
        self.play(Write(ce))
        self.wait(2)
        self.play(Unwrite(ce))
        de = Tex(r"$$\mathcal{D}\cap\mathcal{E}=\{A,B,C,D,E,F\}$$", font_size=30).shift(3 * LEFT + 1.0 * UP)
        self.play(Write(de))
        self.wait(2)
        self.play(Unwrite(de))
        g = 340
        G = Dot([radius * 1.2 * cos(g * pi / 180), radius * 1.2 * sin(g * pi / 180), 0]).shift(3 * RIGHT)
        g_label = MathTex("G").scale(0.75).scale(1.2).move_to(G.get_center() + 0.5 * (RIGHT * cos(g * pi / 180) + UP * sin(g * pi / 180)))
        self.play(Create(G), Create(g_label))
        self.wait()
        lmbd = Tex(r"$$\lambda=-P_3(G)/Q_3(G)$$", font_size=30).shift(3 * LEFT + 1.0 * UP)
        lmbd.align_to(c, LEFT)
        self.play(Write(lmbd))
        self.wait()
        f = Tex(r"$$\mathcal{F}:\quad S_3(x,y)=P_3(x,y)+\lambda Q_3(x,y)$$", font_size=30).shift(3 * LEFT + 0.5 * UP)
        f.align_to(c, LEFT)
        self.play(Write(f))
        self.wait()
        fe = Tex(r"$$\{A,B,C,D,E,F,G\}\subset\mathcal{F}\cap\mathcal{E}$$", font_size=30).shift(3 * LEFT + 0.0 * UP)
        fe.align_to(c, LEFT)
        self.play(Write(fe))
        self.wait(2)
        fet = Tex(r"$$S_3(x,y)=R_2(x,y)T_1(x,y)$$", font_size=30).shift(3 * LEFT + -0.5 * UP)
        fet.align_to(c, LEFT)
        self.play(Write(fet))
        self.wait(2)
        xyz = Tex(r"$$X,Y,Z\not\in \mathcal{E}$$", font_size=30).shift(3 * LEFT + -1.0 * UP)
        xyz.align_to(c, LEFT)
        self.play(Write(xyz))
        self.wait(2)
        xyzt = Tex(r"$$T_1(X)=T_1(Y)=T_1(Z)=0$$", font_size=30).shift(3 * LEFT + -1.5 * UP)
        xyzt.align_to(c, LEFT)
        self.play(Write(xyzt))
        self.wait(3)

        self.play(LaggedStart(
            Unwrite(title),
            FadeOut(sep),
            Unwrite(c),
            Unwrite(d),
            Unwrite(e),
            Unwrite(lmbd),
            Unwrite(f),
            Unwrite(fe),
            Unwrite(fet),
            Unwrite(xyz),
            Unwrite(xyzt),
            FadeOut(*[G, g_label]),
            lag_ratio=0.25,
            run_time=5
        ))
        self.wait()
        self.play(pascal.animate.shift(LEFT * 3))
        self.wait()
        pascal.remove(unitcircle)
        self.add(unitcircle)
        self.play(FadeOut(pascal))
        self.wait()


        # pappus
        pappus = VGroup()
        two_lines = ImplicitFunction(lambda x, y: (x + y - 3) * (x - y + 3), color=PINK)
        pappus.add(two_lines)
        self.play(Transform(unitcircle, two_lines))
        self.wait()
        title = Text("Pappus's Theorem", font_size=30)
        self.play(FadeIn(title, shift=LEFT))
        self.wait()
        a, b, c, d, e, f = 1.7, -3.4, 5.9, -1.5, 4.1, -6.4
        A = Dot([a, 3 - a, 0], radius=0.05)
        B = Dot([b, 3 + b, 0], radius=0.05)
        C = Dot([c, 3 - c, 0], radius=0.05)
        D = Dot([d, 3 + d, 0], radius=0.05)
        E = Dot([e, 3 - e, 0], radius=0.05)
        F = Dot([f, 3 + f, 0], radius=0.05)
        self.play(Create(A), Create(B), Create(C), Create(D), Create(E), Create(F))
        self.wait()
        pappus.add(A, B, C, D, E, F)
        tex_labels = []
        for str, v, angle in [("A", A, 45), ("B", B, 135), ("C", C, 45), ("D", D, 135), ("E", E, 45), ("F", F, 135)]:
            label = (MathTex(str).scale(0.75).move_to(v.get_center() + 0.5 * (RIGHT * cos(angle * pi / 180) + UP * sin(angle * pi / 180))))
            tex_labels.append(label)
        self.play(Create(VGroup(*tex_labels)))
        pappus.add(*tex_labels)
        self.wait()
        self.play(FadeOut(title))
        self.wait()

        X = extension(A, B, D, E)
        x_angle = 90
        x_label = (MathTex("X").scale(0.75).move_to(X.get_center() + 0.3 * (RIGHT * cos(x_angle * pi / 180) + UP * sin(x_angle * pi / 180))))
        ab = Line(A.get_center(), B.get_center())
        de = Line(D.get_center(), E.get_center())
        self.play(Create(ab), Create(de))
        self.play(Create(X), Create(x_label))
        pappus.add(X, x_label, ab, de)

        Y = extension(B, C, E, F)
        y_angle = 270
        y_label = (MathTex("Y").scale(0.75).move_to(Y.get_center() + 0.3 * (RIGHT * cos(y_angle * pi / 180) + UP * sin(y_angle * pi / 180))))
        bc = Line(B.get_center(), C.get_center())
        ef = Line(E.get_center(), F.get_center())
        self.play(Create(bc), Create(ef))
        self.play(Create(Y), Create(y_label))
        pappus.add(Y, y_label, bc, ef)

        Z = extension(C, D, F, A)
        z_angle = 240
        z_label = (MathTex("Z").scale(0.75).move_to(Z.get_center() + 0.3 * (RIGHT * cos(z_angle * pi / 180) + UP * sin(z_angle * pi / 180))))
        cd = Line(C.get_center(), D.get_center())
        fa = Line(F.get_center(), A.get_center())
        self.play(Create(cd), Create(fa))
        self.play(Create(Z), Create(z_label))
        pappus.add(Z, z_label, cd, fa)

        xyz = DashedLine(X.get_center(), Y.get_center())
        pappus.add(xyz)
        self.play(Create(xyz))
        self.wait(2)
        self.play(FadeOut(pappus, shift=DOWN), FadeOut(unitcircle, shift=DOWN), FadeOut(two_lines, shift=DOWN))


        # thank you
        thx = Text("Thank You!", font_size=60)
        self.play(Write(thx), run_time=2)
        self.wait(2)
        self.play(FadeOut(thx))
