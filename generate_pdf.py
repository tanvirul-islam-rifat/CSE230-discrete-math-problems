"""
Generates: CSE230_Discrete_Mathematics_Problem_Set.pdf
A professionally formatted solved problem set covering all major
CSE230 Discrete Mathematics topics with full working shown.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ── Page Setup ──────────────────────────────────────────
doc = SimpleDocTemplate(
    "CSE230_Discrete_Mathematics_Problem_Set.pdf",
    pagesize=A4,
    rightMargin=2.2*cm, leftMargin=2.2*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm
)

W, H = A4
styles = getSampleStyleSheet()

# ── Custom Styles ────────────────────────────────────────
BRAND   = colors.HexColor("#1a1a2e")
ACCENT  = colors.HexColor("#16213e")
BLUE    = colors.HexColor("#0f3460")
LIGHT   = colors.HexColor("#e8f0fe")
SOLVED  = colors.HexColor("#f0f7f0")
BORDER  = colors.HexColor("#c5d5e8")

def style(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = style("DocTitle",
    fontSize=22, fontName="Helvetica-Bold",
    textColor=BRAND, alignment=TA_CENTER, spaceAfter=4)

subtitle_style = style("DocSubtitle",
    fontSize=12, fontName="Helvetica",
    textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=2)

author_style = style("Author",
    fontSize=10, fontName="Helvetica",
    textColor=colors.HexColor("#777777"), alignment=TA_CENTER, spaceAfter=20)

section_style = style("Section",
    fontSize=14, fontName="Helvetica-Bold",
    textColor=colors.white, spaceAfter=0, spaceBefore=16)

problem_style = style("Problem",
    fontSize=11, fontName="Helvetica-Bold",
    textColor=BRAND, spaceBefore=10, spaceAfter=4)

body_style = style("Body",
    fontSize=10.5, fontName="Helvetica",
    textColor=colors.HexColor("#222222"),
    leading=16, spaceAfter=3, alignment=TA_JUSTIFY)

step_style = style("Step",
    fontSize=10.5, fontName="Helvetica",
    textColor=colors.HexColor("#1a1a2e"),
    leading=16, spaceAfter=2, leftIndent=14)

answer_style = style("Answer",
    fontSize=11, fontName="Helvetica-Bold",
    textColor=colors.HexColor("#1a6630"),
    spaceBefore=4, spaceAfter=4, leftIndent=14)

note_style = style("Note",
    fontSize=9.5, fontName="Helvetica-Oblique",
    textColor=colors.HexColor("#555555"),
    leading=14, spaceAfter=2, leftIndent=14)

toc_style = style("TOC",
    fontSize=10.5, fontName="Helvetica",
    textColor=BLUE, leading=18, leftIndent=10)


def section_header(title, number):
    """Renders a colored section banner."""
    data = [[Paragraph(f"Section {number}: {title}", section_style)]]
    t = Table(data, colWidths=[W - 4.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BLUE),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("RIGHTPADDING",  (0,0), (-1,-1), 12),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return t


def solution_box(content_rows):
    """Wraps solution steps in a light-blue tinted box."""
    data = [[item] for item in content_rows]
    t = Table(data, colWidths=[W - 4.4*cm - 0.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), LIGHT),
        ("TOPPADDING",    (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("LINEBELOW",     (0,-1), (-1,-1), 0.5, BORDER),
        ("LINEABOVE",     (0,0),  (-1,0),  0.5, BORDER),
        ("LINEBEFORE",    (0,0),  (0,-1),  2,   BLUE),
    ]))
    return t


def answer_box(text):
    """Green-tinted final answer box."""
    data = [[Paragraph(text, answer_style)]]
    t = Table(data, colWidths=[W - 4.4*cm - 0.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), SOLVED),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("LINEBEFORE",    (0,0), (0,-1),  2, colors.HexColor("#2e7d32")),
    ]))
    return t


# ════════════════════════════════════════════════════════
# DOCUMENT CONTENT
# ════════════════════════════════════════════════════════
story = []

# ── Cover ────────────────────────────────────────────────
story.append(Spacer(1, 1.8*cm))
story.append(Paragraph("Discrete Mathematics", title_style))
story.append(Paragraph("Solved Problem Set", subtitle_style))
story.append(Spacer(1, 0.3*cm))
story.append(HRFlowable(width="60%", thickness=1.5, color=BLUE, hAlign="CENTER"))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("CSE230 — Discrete Mathematics", subtitle_style))
story.append(Paragraph("BRAC University", subtitle_style))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("Md. Tanvirul Islam Rifat &nbsp;&nbsp;|&nbsp;&nbsp; ID: 22101311", author_style))
story.append(Spacer(1, 1.0*cm))

# TOC
toc_data = [
    ["Section", "Topic", "Problems"],
    ["1", "Logic and Propositional Calculus", "1 – 2"],
    ["2", "Set Theory", "3 – 4"],
    ["3", "Relations and Functions", "5 – 6"],
    ["4", "Proof by Induction", "7 – 8"],
    ["5", "Recursion and Recurrence Relations", "9 – 10"],
    ["6", "Combinatorics and Counting", "11 – 12"],
    ["7", "Tower of Hanoi", "13"],
]
toc_table = Table(toc_data, colWidths=[2.2*cm, 10.5*cm, 3.2*cm])
toc_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0),  BLUE),
    ("TEXTCOLOR",     (0,0), (-1,0),  colors.white),
    ("FONTNAME",      (0,0), (-1,0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 10),
    ("FONTNAME",      (0,1), (-1,-1), "Helvetica"),
    ("TEXTCOLOR",     (0,1), (-1,-1), BRAND),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.white, LIGHT]),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("ALIGN",         (1,0), (1,-1),  "LEFT"),
    ("LEFTPADDING",   (1,0), (1,-1),  10),
    ("TOPPADDING",    (0,0), (-1,-1), 7),
    ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ("GRID",          (0,0), (-1,-1), 0.5, BORDER),
    ("ROUNDEDCORNERS",[4]),
]))
story.append(toc_table)
story.append(PageBreak())


# ════════════════════════════════════════════════════════
# SECTION 1: LOGIC
# ════════════════════════════════════════════════════════
story.append(section_header("Logic and Propositional Calculus", 1))
story.append(Spacer(1, 0.3*cm))

# Problem 1
story.append(KeepTogether([
    Paragraph("Problem 1 — Truth Table and Classification", problem_style),
    Paragraph(
        "Construct the truth table for the proposition: <b>(P → Q) ↔ (¬P ∨ Q)</b>. "
        "Classify the result as a tautology, contradiction, or contingency.",
        body_style),
    Spacer(1, 0.15*cm),
]))

tt_data = [
    ["P", "Q", "P → Q", "¬P", "¬P ∨ Q", "(P → Q) ↔ (¬P ∨ Q)"],
    ["F", "F", "T",     "T",  "T",       "T"],
    ["F", "T", "T",     "T",  "T",       "T"],
    ["T", "F", "F",     "F",  "F",       "T"],
    ["T", "T", "T",     "F",  "T",       "T"],
]
tt = Table(tt_data, colWidths=[1.4*cm]*6)
tt.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0),  BLUE),
    ("TEXTCOLOR",     (0,0), (-1,0),  colors.white),
    ("FONTNAME",      (0,0), (-1,0),  "Helvetica-Bold"),
    ("FONTNAME",      (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE",      (0,0), (-1,-1), 10),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID",          (0,0), (-1,-1), 0.5, BORDER),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(tt)
story.append(Spacer(1, 0.15*cm))
story.append(solution_box([
    Paragraph("Recall that P → Q is defined as ¬P ∨ Q. Therefore the biconditional (P → Q) ↔ (¬P ∨ Q) compares a formula with its own definition.", step_style),
    Paragraph("Since P → Q ≡ ¬P ∨ Q by definition, both sides are identical for all truth value assignments.", step_style),
    Paragraph("All four rows evaluate to TRUE.", step_style),
]))
story.append(answer_box("∴ The proposition is a TAUTOLOGY — it is True for all possible truth values of P and Q."))
story.append(Spacer(1, 0.3*cm))

# Problem 2
story.append(KeepTogether([
    Paragraph("Problem 2 — Logical Equivalence", problem_style),
    Paragraph(
        "Prove that <b>¬(P ∧ Q) ≡ ¬P ∨ ¬Q</b> (De Morgan's Law) using a truth table.",
        body_style),
    Spacer(1, 0.15*cm),
]))
dm_data = [
    ["P", "Q", "P ∧ Q", "¬(P ∧ Q)", "¬P", "¬Q", "¬P ∨ ¬Q", "≡?"],
    ["F", "F", "F",     "T",         "T",  "T",  "T",        "✓"],
    ["F", "T", "F",     "T",         "T",  "F",  "T",        "✓"],
    ["T", "F", "F",     "T",         "F",  "T",  "T",        "✓"],
    ["T", "T", "T",     "F",         "F",  "F",  "F",        "✓"],
]
dm = Table(dm_data, colWidths=[1.1*cm, 1.1*cm, 1.5*cm, 2.0*cm, 1.1*cm, 1.1*cm, 2.2*cm, 1.1*cm])
dm.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0),  BLUE),
    ("TEXTCOLOR",     (0,0), (-1,0),  colors.white),
    ("FONTNAME",      (0,0), (-1,0),  "Helvetica-Bold"),
    ("FONTNAME",      (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE",      (0,0), (-1,-1), 9.5),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID",          (0,0), (-1,-1), 0.5, BORDER),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("TEXTCOLOR",     (7,1), (7,-1),  colors.HexColor("#2e7d32")),
]))
story.append(dm)
story.append(Spacer(1, 0.1*cm))
story.append(answer_box("∴ ¬(P ∧ Q) ≡ ¬P ∨ ¬Q — columns 4 and 7 are identical for all rows. De Morgan's Law is verified."))
story.append(PageBreak())


# ════════════════════════════════════════════════════════
# SECTION 2: SET THEORY
# ════════════════════════════════════════════════════════
story.append(section_header("Set Theory", 2))
story.append(Spacer(1, 0.3*cm))

# Problem 3
story.append(KeepTogether([
    Paragraph("Problem 3 — Set Operations", problem_style),
    Paragraph(
        "Let <b>A = {1, 2, 3, 4, 5}</b> and <b>B = {3, 4, 5, 6, 7}</b>. "
        "Find: (a) A ∪ B, (b) A ∩ B, (c) A − B, (d) B − A, (e) A △ B. "
        "Verify the inclusion-exclusion principle.",
        body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("<b>(a)</b> A ∪ B = {1, 2, 3, 4, 5, 6, 7}  (all elements in A or B)", step_style),
    Paragraph("<b>(b)</b> A ∩ B = {3, 4, 5}  (elements in both)", step_style),
    Paragraph("<b>(c)</b> A − B = {1, 2}  (in A but not B)", step_style),
    Paragraph("<b>(d)</b> B − A = {6, 7}  (in B but not A)", step_style),
    Paragraph("<b>(e)</b> A △ B = (A − B) ∪ (B − A) = {1, 2, 6, 7}  (in exactly one set)", step_style),
    Paragraph("<b>Inclusion-Exclusion:</b> |A ∪ B| = |A| + |B| − |A ∩ B| = 5 + 5 − 3 = 7  ✓", step_style),
]))
story.append(answer_box("∴ A ∪ B = {1,2,3,4,5,6,7}, A ∩ B = {3,4,5}, A△B = {1,2,6,7}. Inclusion-exclusion verified: 7 = 5 + 5 − 3."))
story.append(Spacer(1, 0.3*cm))

# Problem 4
story.append(KeepTogether([
    Paragraph("Problem 4 — Power Set", problem_style),
    Paragraph("Find the power set <b>P(A)</b> for <b>A = {a, b, c}</b>. State its cardinality.", body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("For a set with |A| = n elements, |P(A)| = 2<super>n</super>. Here n = 3, so |P(A)| = 2<super>3</super> = 8.", step_style),
    Paragraph("Listing all subsets by cardinality:", step_style),
    Paragraph("  |S| = 0: ∅", step_style),
    Paragraph("  |S| = 1: {a}, {b}, {c}", step_style),
    Paragraph("  |S| = 2: {a,b}, {a,c}, {b,c}", step_style),
    Paragraph("  |S| = 3: {a,b,c}", step_style),
]))
story.append(answer_box("∴ P(A) has 8 subsets. The number of subsets always equals 2^n where n = |A|."))
story.append(PageBreak())


# ════════════════════════════════════════════════════════
# SECTION 3: RELATIONS
# ════════════════════════════════════════════════════════
story.append(section_header("Relations and Functions", 3))
story.append(Spacer(1, 0.3*cm))

# Problem 5
story.append(KeepTogether([
    Paragraph("Problem 5 — Properties of Relations", problem_style),
    Paragraph(
        "Let <b>A = {1, 2, 3}</b> and <b>R = {(1,1), (2,2), (3,3), (1,2), (2,1), (2,3), (3,2)}</b>. "
        "Determine whether R is reflexive, symmetric, antisymmetric, and transitive. Classify R.",
        body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("<b>Reflexive:</b> Check (a,a) ∈ R for all a ∈ A.", step_style),
    Paragraph("  (1,1) ∈ R ✓,  (2,2) ∈ R ✓,  (3,3) ∈ R ✓  →  R is REFLEXIVE.", step_style),
    Paragraph("<b>Symmetric:</b> For every (a,b) ∈ R, check (b,a) ∈ R.", step_style),
    Paragraph("  (1,2) ∈ R and (2,1) ∈ R ✓;  (2,3) ∈ R and (3,2) ∈ R ✓  →  R is SYMMETRIC.", step_style),
    Paragraph("<b>Antisymmetric:</b> (a,b) ∈ R and (b,a) ∈ R requires a = b.", step_style),
    Paragraph("  (1,2) ∈ R and (2,1) ∈ R but 1 ≠ 2  →  R is NOT ANTISYMMETRIC.", step_style),
    Paragraph("<b>Transitive:</b> For every (a,b) and (b,c) in R, check (a,c) ∈ R.", step_style),
    Paragraph("  (1,2) ∈ R and (2,3) ∈ R → need (1,3) ∈ R. But (1,3) ∉ R  →  R is NOT TRANSITIVE.", step_style),
]))
story.append(answer_box("∴ R is Reflexive and Symmetric, but NOT Antisymmetric and NOT Transitive. R is not an equivalence relation (fails transitivity) and not a partial order (fails antisymmetry)."))
story.append(Spacer(1, 0.3*cm))

# Problem 6
story.append(KeepTogether([
    Paragraph("Problem 6 — Equivalence Relation", problem_style),
    Paragraph(
        "Define a relation R on integers by <b>aRb if and only if a ≡ b (mod 3)</b>. "
        "Prove R is an equivalence relation and state its equivalence classes.",
        body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("<b>Reflexive:</b> a − a = 0 = 0 × 3, so 3 | (a − a). Thus aRa for all integers a. ✓", step_style),
    Paragraph("<b>Symmetric:</b> If aRb then 3 | (a − b). Since a − b = −(b − a), we have 3 | (b − a), so bRa. ✓", step_style),
    Paragraph("<b>Transitive:</b> If aRb and bRc then 3|(a−b) and 3|(b−c).", step_style),
    Paragraph("  So a − c = (a − b) + (b − c). Since 3 divides both terms, 3 | (a − c), so aRc. ✓", step_style),
    Paragraph("<b>Equivalence Classes:</b>", step_style),
    Paragraph("  [0] = {..., −6, −3, 0, 3, 6, ...}  (multiples of 3)", step_style),
    Paragraph("  [1] = {..., −5, −2, 1, 4, 7, ...}  (remainder 1 when divided by 3)", step_style),
    Paragraph("  [2] = {..., −4, −1, 2, 5, 8, ...}  (remainder 2 when divided by 3)", step_style),
]))
story.append(answer_box("∴ R is an equivalence relation (reflexive + symmetric + transitive). It partitions Z into 3 equivalence classes: [0], [1], [2]."))
story.append(PageBreak())


# ════════════════════════════════════════════════════════
# SECTION 4: PROOF BY INDUCTION
# ════════════════════════════════════════════════════════
story.append(section_header("Proof by Mathematical Induction", 4))
story.append(Spacer(1, 0.3*cm))

# Problem 7
story.append(KeepTogether([
    Paragraph("Problem 7 — Sum of First n Natural Numbers", problem_style),
    Paragraph(
        "Prove by mathematical induction: "
        "<b>1 + 2 + 3 + ... + n = n(n+1)/2</b> for all positive integers n.",
        body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("<b>Step 1 — Base Case (n = 1):</b>", step_style),
    Paragraph("  LHS = 1", step_style),
    Paragraph("  RHS = 1(1+1)/2 = 1", step_style),
    Paragraph("  LHS = RHS ✓  Base case holds.", step_style),
    Paragraph("<b>Step 2 — Inductive Hypothesis:</b>", step_style),
    Paragraph("  Assume the formula holds for some arbitrary k ≥ 1:", step_style),
    Paragraph("  1 + 2 + ... + k = k(k+1)/2", step_style),
    Paragraph("<b>Step 3 — Inductive Step (prove for n = k+1):</b>", step_style),
    Paragraph("  1 + 2 + ... + k + (k+1)  =  k(k+1)/2 + (k+1)  [by hypothesis]", step_style),
    Paragraph("                            =  (k+1)[k/2 + 1]", step_style),
    Paragraph("                            =  (k+1)(k+2)/2", step_style),
    Paragraph("  This is exactly the formula with n = k+1. ✓", step_style),
]))
story.append(answer_box("∴ By the Principle of Mathematical Induction, 1+2+...+n = n(n+1)/2 holds for all n ≥ 1."))
story.append(Spacer(1, 0.3*cm))

# Problem 8
story.append(KeepTogether([
    Paragraph("Problem 8 — Sum of Geometric Series", problem_style),
    Paragraph(
        "Prove by induction: <b>1 + 2 + 2<super>2</super> + ... + 2<super>n</super> = 2<super>n+1</super> − 1</b> "
        "for all n ≥ 0.",
        body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("<b>Base Case (n = 0):</b>  LHS = 1,  RHS = 2<super>1</super> − 1 = 1  ✓", step_style),
    Paragraph("<b>Inductive Hypothesis:</b>  Assume 1 + 2 + ... + 2<super>k</super> = 2<super>k+1</super> − 1 for some k ≥ 0.", step_style),
    Paragraph("<b>Inductive Step (n = k+1):</b>", step_style),
    Paragraph("  (1 + 2 + ... + 2<super>k</super>) + 2<super>k+1</super>  =  (2<super>k+1</super> − 1) + 2<super>k+1</super>  [by hypothesis]", step_style),
    Paragraph("                                    =  2 × 2<super>k+1</super> − 1", step_style),
    Paragraph("                                    =  2<super>k+2</super> − 1  ✓", step_style),
]))
story.append(answer_box("∴ By induction, the geometric series sum 1 + 2 + 2^2 + ... + 2^n = 2^(n+1) − 1 holds for all n ≥ 0."))
story.append(PageBreak())


# ════════════════════════════════════════════════════════
# SECTION 5: RECURSION & RECURRENCES
# ════════════════════════════════════════════════════════
story.append(section_header("Recursion and Recurrence Relations", 5))
story.append(Spacer(1, 0.3*cm))

# Problem 9
story.append(KeepTogether([
    Paragraph("Problem 9 — Solving a Recurrence Relation", problem_style),
    Paragraph(
        "Solve the recurrence relation <b>T(n) = 2·T(n−1) + 1</b> with <b>T(1) = 1</b>. "
        "Find a closed-form expression and verify for n = 1 to 5.",
        body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("<b>Iterative unrolling:</b>", step_style),
    Paragraph("  T(n) = 2·T(n−1) + 1", step_style),
    Paragraph("       = 2[2·T(n−2) + 1] + 1  =  4·T(n−2) + 3", step_style),
    Paragraph("       = 2<super>2</super>·T(n−2) + 2<super>1</super> + 2<super>0</super>", step_style),
    Paragraph("       = 2<super>k</super>·T(n−k) + 2<super>k−1</super> + ... + 2<super>0</super>", step_style),
    Paragraph("  Setting k = n−1:  T(n) = 2<super>n−1</super>·T(1) + (2<super>n−1</super> − 1) = 2<super>n−1</super> + 2<super>n−1</super> − 1 = 2<super>n</super> − 1", step_style),
    Paragraph("<b>Verification:</b>  T(1)=1, T(2)=3, T(3)=7, T(4)=15, T(5)=31", step_style),
    Paragraph("  All match 2<super>n</super> − 1:  1, 3, 7, 15, 31  ✓", step_style),
]))
story.append(answer_box("∴ Closed-form solution: T(n) = 2^n − 1. (This is also the exact number of moves in the Tower of Hanoi problem!)"))
story.append(Spacer(1, 0.3*cm))

# Problem 10
story.append(KeepTogether([
    Paragraph("Problem 10 — Fibonacci Recurrence", problem_style),
    Paragraph(
        "The Fibonacci sequence is defined by <b>F(0) = 0, F(1) = 1, F(n) = F(n−1) + F(n−2)</b>. "
        "List the first 10 terms and prove that F(1)+F(2)+...+F(n) = F(n+2) − 1.",
        body_style),
    Spacer(1, 0.1*cm),
]))
fib_data = [
    ["n",    "0","1","2","3","4","5","6","7","8","9"],
    ["F(n)", "0","1","1","2","3","5","8","13","21","34"],
]
fib_t = Table(fib_data, colWidths=[1.5*cm]+[1.3*cm]*10)
fib_t.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0),  BLUE),
    ("TEXTCOLOR",     (0,0), (-1,0),  colors.white),
    ("BACKGROUND",    (0,1), (0,-1),  ACCENT),
    ("TEXTCOLOR",     (0,1), (0,-1),  colors.white),
    ("FONTNAME",      (0,0), (-1,-1), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 9.5),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("GRID",          (0,0), (-1,-1), 0.5, BORDER),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(fib_t)
story.append(Spacer(1, 0.1*cm))
story.append(solution_box([
    Paragraph("<b>Proof by induction that F(1)+F(2)+...+F(n) = F(n+2) − 1:</b>", step_style),
    Paragraph("<b>Base Case (n=1):</b>  F(1) = 1,  F(3) − 1 = 2 − 1 = 1  ✓", step_style),
    Paragraph("<b>Inductive Step:</b>  Assume F(1)+...+F(k) = F(k+2)−1.", step_style),
    Paragraph("  F(1)+...+F(k)+F(k+1) = F(k+2)−1+F(k+1) = [F(k+1)+F(k+2)]−1 = F(k+3)−1  ✓", step_style),
]))
story.append(answer_box("∴ First 10 Fibonacci terms: 0,1,1,2,3,5,8,13,21,34. Sum identity F(1)+...+F(n) = F(n+2)−1 proven by induction."))
story.append(PageBreak())


# ════════════════════════════════════════════════════════
# SECTION 6: COMBINATORICS
# ════════════════════════════════════════════════════════
story.append(section_header("Combinatorics and Counting", 6))
story.append(Spacer(1, 0.3*cm))

# Problem 11
story.append(KeepTogether([
    Paragraph("Problem 11 — Permutations and Combinations", problem_style),
    Paragraph(
        "(a) In how many ways can 5 students be arranged in a row? "
        "(b) How many 3-member committees can be chosen from 8 students? "
        "(c) How many 4-digit PINs can be made from digits 1–9 if digits cannot repeat?",
        body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("<b>(a) Permutation — order matters, no repetition:</b>", step_style),
    Paragraph("  P(5,5) = 5! = 5 × 4 × 3 × 2 × 1 = 120 arrangements", step_style),
    Paragraph("<b>(b) Combination — order does NOT matter:</b>", step_style),
    Paragraph("  C(8,3) = 8! / (3! × 5!) = (8 × 7 × 6) / (3 × 2 × 1) = 336 / 6 = 56 committees", step_style),
    Paragraph("<b>(c) Permutation from 9 digits, choosing 4:</b>", step_style),
    Paragraph("  P(9,4) = 9! / (9−4)! = 9! / 5! = 9 × 8 × 7 × 6 = 3024 PINs", step_style),
]))
story.append(answer_box("∴ (a) 120 arrangements  (b) 56 committees  (c) 3,024 PINs"))
story.append(Spacer(1, 0.3*cm))

# Problem 12
story.append(KeepTogether([
    Paragraph("Problem 12 — Pigeonhole Principle", problem_style),
    Paragraph(
        "A drawer contains socks of 4 colors. "
        "(a) How many socks must you pick (in the dark) to guarantee a matching pair? "
        "(b) How many to guarantee 3 socks of the same color? "
        "(c) A class has 367 students — prove at least two share a birthday.",
        body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("<b>Pigeonhole Principle:</b> If n items are placed in k containers, at least one container has ⌈n/k⌉ items.", step_style),
    Paragraph("<b>(a) Guarantee a pair (2 of same color):</b>  4 colors = 4 pigeonholes.", step_style),
    Paragraph("  Worst case: pick one of each color (4 socks). The 5th sock must match one.", step_style),
    Paragraph("  Answer: 4 + 1 = <b>5 socks</b>  (general formula: k + 1)", step_style),
    Paragraph("<b>(b) Guarantee 3 of same color:</b>  Worst case: 2 of each color = 8 socks.", step_style),
    Paragraph("  The 9th sock must give 3 of one color.  Answer: <b>9 socks</b>  (general: k(m−1) + 1)", step_style),
    Paragraph("<b>(c) 367 students, 366 possible birthdays (including Feb 29):</b>", step_style),
    Paragraph("  By Pigeonhole: 367 pigeons, 366 holes → at least ⌈367/366⌉ = 2 share a birthday.  ✓", step_style),
]))
story.append(answer_box("∴ (a) 5 socks  (b) 9 socks  (c) With 367 students and only 366 possible birthdays, at least two must share a birthday by the Pigeonhole Principle."))
story.append(PageBreak())


# ════════════════════════════════════════════════════════
# SECTION 7: TOWER OF HANOI
# ════════════════════════════════════════════════════════
story.append(section_header("Tower of Hanoi", 7))
story.append(Spacer(1, 0.3*cm))

story.append(KeepTogether([
    Paragraph("Problem 13 — Tower of Hanoi: Recurrence, Proof, and Move Sequence", problem_style),
    Paragraph(
        "(a) State the recurrence relation for the minimum number of moves T(n) to solve "
        "the Tower of Hanoi with n disks. (b) Prove by induction that T(n) = 2<super>n</super> − 1. "
        "(c) Write out all moves for n = 3 disks (Pegs: A → C using B as auxiliary).",
        body_style),
    Spacer(1, 0.1*cm),
]))
story.append(solution_box([
    Paragraph("<b>(a) Recurrence Relation:</b>", step_style),
    Paragraph("  T(1) = 1                      (base case: one disk, one move)", step_style),
    Paragraph("  T(n) = 2·T(n−1) + 1           (move n−1 disks to aux, move largest, move n−1 disks to target)", step_style),
    Spacer(1, 0.1*cm),
    Paragraph("<b>(b) Proof by Induction that T(n) = 2<super>n</super> − 1:</b>", step_style),
    Paragraph("  Base Case (n=1): T(1) = 1 = 2<super>1</super> − 1 = 1  ✓", step_style),
    Paragraph("  Inductive Hypothesis: Assume T(k) = 2<super>k</super> − 1 for some k ≥ 1.", step_style),
    Paragraph("  Inductive Step: T(k+1) = 2·T(k) + 1 = 2·(2<super>k</super>−1) + 1 = 2<super>k+1</super> − 2 + 1 = 2<super>k+1</super> − 1  ✓", step_style),
]))
story.append(Spacer(1, 0.15*cm))

hanoi_data = [
    ["Step", "Disk", "From", "To", "Explanation"],
    ["1", "Disk 1", "A", "C", "Move smallest disk A → C"],
    ["2", "Disk 2", "A", "B", "Move middle disk A → B"],
    ["3", "Disk 1", "C", "B", "Move smallest disk C → B"],
    ["4", "Disk 3", "A", "C", "Move largest disk A → C"],
    ["5", "Disk 1", "B", "A", "Move smallest disk B → A"],
    ["6", "Disk 2", "B", "C", "Move middle disk B → C"],
    ["7", "Disk 1", "A", "C", "Move smallest disk A → C"],
]
ht = Table(hanoi_data, colWidths=[1.4*cm, 2.2*cm, 1.6*cm, 1.6*cm, 7.6*cm])
ht.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0),  BLUE),
    ("TEXTCOLOR",     (0,0), (-1,0),  colors.white),
    ("FONTNAME",      (0,0), (-1,0),  "Helvetica-Bold"),
    ("FONTNAME",      (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE",      (0,0), (-1,-1), 10),
    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ("ALIGN",         (4,1), (4,-1),  "LEFT"),
    ("LEFTPADDING",   (4,0), (4,-1),  8),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID",          (0,0), (-1,-1), 0.5, BORDER),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(ht)
story.append(Spacer(1, 0.1*cm))
story.append(answer_box("∴ T(3) = 2^3 − 1 = 7 moves. Every move is forced — this is the unique optimal solution."))

# ── Footer note ──
story.append(Spacer(1, 0.8*cm))
story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph(
    "Md. Tanvirul Islam Rifat  |  ID: 22101311  |  BSc Computer Science  |  BRAC University",
    style("Footer", fontSize=9, fontName="Helvetica", textColor=colors.HexColor("#888888"),
          alignment=TA_CENTER)))

# ── Build ────────────────────────────────────────────────
doc.build(story)
print("PDF generated: CSE230_Discrete_Mathematics_Problem_Set.pdf")
