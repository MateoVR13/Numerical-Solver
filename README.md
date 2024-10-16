# Numerical Methods Solver

A Python-based application for solving various numerical methods. This project implements algorithms for solving equations using techniques such as Bisection, Newton-Raphson, Secant, Muller, False Position, and Taylor and Maclaurin series.

## Features

- **Bisection Method**: A root-finding method that divides an interval and selects a subinterval in which a root must lie.
- **Newton-Raphson Method**: A method that uses tangents to find roots of real-valued functions.
- **Secant Method**: A method that uses a succession of roots of secant lines to approximate a root of a function.
- **Muller Method**: A method that finds roots by interpolating a quadratic polynomial through three points.
- **False Position Method**: A combination of the bisection and secant methods for root finding.
- **Taylor Series**: Approximates functions using Taylor polynomials.
- **Maclaurin Series**: A special case of the Taylor series centered at zero.

## Installation

To get started with the Numerical Methods Solver, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/numerical-methods-solver.git
   cd numerical-methods-solver
   ```

2. Install the required libraries using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Requirements

Make sure you have the following Python libraries installed:

- `seaborn`
- `plotly`
- `matplotlib`
- `sympy`
- `scipy`
- `math`

The `requirements.txt` file in this repository includes all necessary dependencies.

## Usage

After installation, you can run the solver by executing the main script:

```bash
python main.py
```

You can then input the function and parameters for the desired numerical method, and the program will output the solution and graphical representations where applicable.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add new features, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thanks to the creators of the libraries used in this project, including Seaborn, Plotly, Matplotlib, SymPy, SciPy, and the mathematical concepts behind the numerical methods implemented.
