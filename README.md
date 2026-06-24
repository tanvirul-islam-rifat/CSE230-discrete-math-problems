# CSE230 — Discrete Mathematics: Solved Problem Set

A solved problem set covering all major topics from **CSE230 – Discrete Mathematics**. Each problem includes the full mathematical working, step-by-step reasoning, and a clearly stated conclusion — not just the final answer.

> CSE230 is a pure mathematics course with no coding component. This repository contains a formal written problem set that represents the mathematical work done in the course, alongside a Python script that generates the PDF programmatically.

---

## Contents

The problem set covers 13 problems across 7 sections:

| Section | Topic | Problems |
|---------|-------|---------|
| 1 | Logic and Propositional Calculus | Truth tables, De Morgan's Law |
| 2 | Set Theory | Set operations, Power set, Inclusion-Exclusion |
| 3 | Relations and Functions | Relation properties, Equivalence relations |
| 4 | Proof by Mathematical Induction | Sum formulas, Geometric series |
| 5 | Recursion and Recurrence Relations | Solving T(n), Fibonacci |
| 6 | Combinatorics and Counting | P(n,r), C(n,r), Pigeonhole Principle |
| 7 | Tower of Hanoi | Recurrence, induction proof, full move sequence |

---

## Files

```
cse230-discrete-math-problems/
├── CSE230_Discrete_Mathematics_Problem_Set.pdf   # The formatted problem set
├── generate_pdf.py                                # Python script that generates the PDF
└── README.md
```

---

## How to View

Download `CSE230_Discrete_Mathematics_Problem_Set.pdf` directly from this repository.

To regenerate the PDF yourself:

```bash
# Install dependency
pip install reportlab

# Generate
python3 generate_pdf.py
```

---

## Sample Problems

**Problem 7 — Proof by Induction:**
Prove that 1 + 2 + 3 + ... + n = n(n+1)/2 for all positive integers n.
Full three-step induction proof included (base case, hypothesis, inductive step).

**Problem 13 — Tower of Hanoi:**
State the recurrence T(n) = 2·T(n−1) + 1, prove T(n) = 2^n − 1 by induction,
and list all 7 moves for n = 3 disks with peg labels.

**Problem 12 — Pigeonhole Principle:**
Prove that in any group of 367 students, at least two must share a birthday.

---

## Technical Architecture

- **Language:** Python 3.x
- **PDF Generation:** ReportLab (Platypus layout engine with custom styles)
- **Document Format:** A4, multi-section with cover page, table of contents, color-coded solution boxes, and truth tables

## Core Engineering Practices Demonstrated

- **Programmatic Document Generation:** The entire PDF — cover page, table of contents, truth tables, solution boxes, and section headers — is generated from a single Python script using ReportLab's Platypus layout engine, with no manual word processor formatting
- **Structured Mathematical Writing:** Every problem follows a consistent format: problem statement → step-by-step working → boxed conclusion, mirroring the structure expected in formal mathematical proofs
- **Reusable Layout Components:** Section headers, solution boxes, and answer boxes are implemented as reusable Python functions, demonstrating clean separation between content and presentation

## Author

**Md. Tanvirul Islam Rifat**

* **GitHub:** [@tanvirul-islam-rifat](https://github.com/tanvirul-islam-rifat)
* **LinkedIn:** [Tanvirul Islam Rifat](https://www.linkedin.com/in/tanvirul-islam-rifat)
