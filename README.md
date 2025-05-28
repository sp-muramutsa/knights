# Knights and Knaves Logic Puzzle Solver

This project demonstrates the use of propositional logic and model checking to solve classic Knights and Knaves puzzles—an important example of knowledge-based reasoning in artificial intelligence. Knights always tell the truth, and knaves always lie. By formalizing statements as logical expressions and applying model checking, the solver deduces the true identity of each character.

## Project Structure

* `knights/`
  Contains the core logic and puzzle definitions in `puzzle.py`.
* `logic.py`
  Provides foundational propositional logic constructs, inference rules, and a model checker to evaluate logical statements against possible truth assignments.

## Core Concepts

### Knowledge-Based Agent

The solver acts as a knowledge-based agent that uses background knowledge (rules about knights and knaves) and new observations (statements made by characters) to infer hidden facts. This approach illustrates key AI principles such as symbolic reasoning and knowledge representation.

### Model Checking

Model checking is employed to exhaustively evaluate all possible truth assignments to the logical symbols and determine which assignments satisfy the entire knowledge base. This enables automated deduction of each character’s identity.

## Puzzles Implemented

* **Puzzle 0:** A says, "I am both a knight and a knave."
* **Puzzle 1:** A says, "We are both knaves."
* **Puzzle 2:** A says, "We are the same kind." B says, "We are of different kinds."
* **Puzzle 3:** A says either "I am a knight." or "I am a knave." (unknown which). B says, "A said 'I am a knave'." B also says, "C is a knave." C says, "A is a knight."

Each puzzle encodes the statements and constraints as propositional formulas, combined with rules enforcing that each character is exclusively a knight or a knave.

## Usage

Run the solver via:

```bash
python knights/puzzle.py
```

The program outputs which characters are knights and which are knaves for each puzzle based on logical inference.

## Dependencies

* Python 3.x
* `logic.py` — implements propositional logic classes, logical connectives, and the `model_check` function used to verify if a formula is entailed by the knowledge base. This module is essential for representing knowledge and performing inference.

## Authors

CS50 & Sandrin Muramutsa
