# 🧮 Python GUI Calculator

A desktop calculator built with Python and Tkinter, featuring a customized dark interface, interactive buttons, sound effects, and a restricted AST-based expression evaluator.

## ✨ Features

Basic Arithmetic: Addition (+), subtraction (-), multiplication (*), and division (/).

Power Operations: Calculate exponents using the ** operator (e.g., 2**3 = 8).

Modulo: Supports modulo operations (%).

Parentheses: Supports expressions with brackets for controlling calculation order.

Automatic Bracket Handling: Automatically inserts closing brackets where appropriate.

Cursor-Aware Backspace: Deletes characters based on the current cursor position.

AST-Based Evaluation: Uses Python's Abstract Syntax Tree to evaluate expressions without relying on unsafe eval().

Error Handling: Handles invalid expressions, division by zero, and unsupported operations.

Sound Effects: Provides audio feedback for calculator interactions.

Dark Theme: Features a customized dark interface.

## 🛠️ Technologies Used

- Python
- Tkinter
- ttk and ttkthemes
- AST (Abstract Syntax Tree)
- Math module
- Winsound

## 📦 Installation

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd Calculator
```

**3. Install the required external dependency**

```bash
pip install ttkthemes
```

**4. Run the application**

```bash
python main.py
```

## 🔊 Sound Effects

The calculator uses WAV audio files through Python's built-in `winsound` module.

Keep the sound files in a `sounds` directory:

```text
Calculator/
│
├── main.py
├── sounds/
│   ├── number.wav
│   ├── cross.wav
│   ├── empty.wav
│   └── equal.wav
│
└── README.md
```

## 🧠 How Expression Evaluation Works

Instead of using Python's `eval()`, this calculator uses the `ast` module to parse mathematical expressions.

The custom recursive evaluator supports selected AST nodes and operators:

- `ast.Constant`
- `ast.BinOp`
- `ast.UnaryOp`
- Addition, subtraction, multiplication, division, modulo and exponentiation.

Unsupported expressions and values are rejected.

## 📚 What I Learned

Building this project helped me practise:

- GUI development with Tkinter.
- Grid-based layout management.
- Event handling and callback functions.
- Lambda functions.
- Recursion and AST traversal.
- Exception handling.
- String manipulation.
- Working with external Python libraries.
- Integrating sound effects into a GUI application.

## 👨‍💻 Author

**Junaid**

Built as a hands-on Python project to strengthen my programming and GUI development skills.

---

*Feedback and suggestions are welcome!*
