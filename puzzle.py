from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    # Background info
    # A is either a knight or a knave and never both: XOR = (A v B) ∧ ¬(A ∧ B)
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # Puzzle
    # Statement is True if said by a knight: A -> (A v B)
    Implication(AKnight, And(AKnight, AKnave)),
    # Statement is False if said by a knave
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    # Background info
    # A is either a knight or a knave and never both: XOR = (A v B) ∧ ¬(A ∧ B)
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B is either a knight or a knave and never both: XOR = (A v B) ∧ ¬(A ∧ B)
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # Puzzle
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    # Background info
    # A is either a knight or a knave and never both: XOR = (A v B) ∧ ¬(A ∧ B)
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B is either a knight or a knave and never both: XOR = (A v B) ∧ ¬(A ∧ B)
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # Puzzle
    Implication(AKnight, And(AKnight, BKnight)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
    Implication(BKnight, And(AKnave, BKnight)),
    Implication(BKnave, Not(And(AKnight, BKnave))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    # Background info
    # A is either a knight or a knave and never both: XOR = (A v B) ∧ ¬(A ∧ B)
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B is either a knight or a knave and never both: XOR = (A v B) ∧ ¬(A ∧ B)
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # B is either a knight or a knave and never both: XOR = (A v B) ∧ ¬(A ∧ B)
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    # Puzzle 3
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    # No inclusion, already included in the background info section
    # B says "A said 'I am a knave'."
    Implication(
        BKnight, And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
    ),
    Implication(
        BKnave, Not(And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))))
    ),
    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")
        print("\n\n")


if __name__ == "__main__":
    main()
