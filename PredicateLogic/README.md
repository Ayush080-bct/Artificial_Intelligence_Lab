# Prolog Knowledge Base Engine

This project contains a logic programming implementation using **Prolog**. It leverages predicate logic to build a structured knowledge base, allowing an inference engine to reason over facts and deduce new conclusions automatically.

## What is a Prolog File (`.pl`)?

In this repository, files ending in `.pl` are **Prolog Source Code files** (not to be confused with Perl scripts). 

A Prolog file functions as a declarative **Knowledge Base**. Unlike traditional procedural programming languages (like Python or C++) that tell a computer *how* to solve a problem step-by-step, a Prolog file describes *what* the world looks like using two main components:
1. **Facts**: Explicit ground truths about entities (e.g., `parent(bob, charlie).`).
2. **Rules**: Conditional logical relationships that allow the system to infer new knowledge (e.g., `grandparent(X, Z) :- parent(X, Y), parent(Y, Z).`).

When you load this file into a Prolog interpreter, you do not "run" it like a standard script. Instead, you **query** it, and the interpreter uses automated reasoning (backtracking and unification) to answer your questions.

---

## Prerequisites

To load and interact with these files, you must have a Prolog compiler installed. **SWI-Prolog** is the recommended runtime environment.

### Installation on Linux

Open your terminal and run the command matching your Linux distribution:

* **Ubuntu / Debian / Linux Mint:**
  ```bash
  sudo apt update && sudo apt install swi-prolog
  ```
* **Fedora:**
  ```bash
  sudo dnf install pl
  ```
* **Arch Linux / Manjaro:**
  ```bash
  sudo pacman -S swi-prolog
  ```

---

## How to Run and Query the File

Follow these steps to load your `.pl` file into the interpreter and execute queries:

### 1. Launch the Interpreter
Navigate to the directory containing your file and start the SWI-Prolog shell:
```bash
swipl
```
Your terminal prompt will change to `?-`, indicating that Prolog is ready for input.

### 2. Load (Consult) Your File
Assuming your file is named `main.pl`, load it into the engine by running:
```prolog
?- [main].
```
*Note: Do not include the `.pl` extension inside the brackets, and **always end your command with a period (`.`)**.*

### 3. Issue Queries (Inference Testing)
You can now ask the engine questions based on your defined rules. For example, to find out who a specific entity relates to, use a capitalized letter as a variable:
```prolog
?- grandparent(bob, X).
```
* Press `Spacebar` or `;` to cycle through alternative solutions if multiple answers exist.
* Press `Enter` to stop searching.

### 4. Exit the Interpreter
To close the Prolog environment and return to your standard Linux shell, type:
```prolog
?- halt.
```
