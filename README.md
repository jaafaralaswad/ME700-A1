# ME700 Assignment 1: Warm-up

This repository presents a bisection method solver developed for the first assignment in the ME700 course. The first three numerical examples demonstrate solving algebraic equations. The fourth example applies the method to find the position of a balance force in a cantilever beam, while the fifth example computes a center of mass for a given number of masses on a 1D axis.

# The Bisection Method

The bisection method is a classical numerical technique for finding real roots of algebraic equations. It is based on the intermediate value theorem from calculus, which states that if a continuous function takes on opposite signs at two points, there must be at least one root between them. The method's name reflects how it works: in each iteration, the interval is bisected, and the half containing a sign change is retained for the next iteration, while the other half is discarded.

The user must define the function, $f(x)$, and specify the lower and upper bounds of the interval, $a$ and $b$, respectively. To ensure the presence of a root, the function values at these bounds must have opposite signs. If both values share the same sign, the existence of a root within the interval is not guaranteed. In such cases, an error message is displayed, prompting the user to select a different set of boundaries.

The bisection method is an iterative process, and the user determines the termination criteria based on the required accuracy, which depends on the specific application. This solver employs two termination criteria, ending the iterations when either is satisfied. The first criterion is when $|c-a|< \epsilon_1$, meaning the half-interval size becomes smaller than a predefined threshold. The second criterion is when $|f(c)|< \epsilon_2$, indicating that the function value is sufficiently close to zero. The user must specify both $\epsilon_1$ and $\epsilon_2$, with tighter tolerances providing greater accuracy at the cost of additional iterations.

The concept of the bisection method is straightforward. However, the method has significant limitations. First, the user must identify an interval that contains a root.  Second, the method can only find a single root at a time; for equations with multiple roots, the user must test different intervals to locate each one. Third, the method has a relatively slow convergence rate, often requiring more iterations compared to more advanced numerical techniques.

# Conda environment, install, and testing

This procedure is very similar to what we did in the last class. First, you need to download the repository and unzip it. Then, to install the package:

```bash
conda create --name bisection-method-env python=3.12
