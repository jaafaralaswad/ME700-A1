# ME700 Assignment 1: Warm-up

This repository presents a bisection method solver developed for the first assignment in the ME700 course. It begins with a brief introduction to the bisection method, followed by five numerical examples. The first three examples demonstrate solving algebraic equations using `bisection.py`. The fourth example applies the method to find the position of a balance force in a cantilever beam using `cantilever.py`, while the fifth example computes a center of mass using `mass_center.py`.

# The Bisection Method

The bisection method is a classical numerical technique for finding real roots of algebraic equations. It is based on the intermediate value theorem from calculus, which states that if a continuous function takes on opposite signs at two points, there must be at least one root between them. The method's name reflects how it works: in each iteration, the interval is bisected, and the half containing a sign change is retained for the next iteration, while the other half is discarded.

In `bisection.py`, the user must define the function, $f(x)$, and specify the lower and upper bounds of the interval, $a$ and $b$, respectively. To ensure the presence of a root, the function values at these bounds must have opposite signs. If both values share the same sign, the existence of a root within the interval is not guaranteed. In such cases, an error message is displayed, prompting the user to select a different set of boundaries.

The bisection method is an iterative process, and the user determines the termination criteria based on the required accuracy, which depends on the specific application. This solver employs two termination criteria, ending the iterations when either is satisfied. The first criterion is when $|c-a|< \epsilon_1$, meaning the half-interval size becomes smaller than a predefined threshold. The second criterion is when $|f(c)|< \epsilon_2$, indicating that the function value is sufficiently close to zero. The user must specify both $\epsilon_1$ and $\epsilon_2$, with tighter tolerances providing greater accuracy at the cost of additional iterations.

The concept of the bisection method is straightforward. However, the method has significant limitations. First, the user must identify an interval that contains a root.  Second, the method can only find a single root at a time; for equations with multiple roots, the user must test different intervals to locate each one. Third, the method has a relatively slow convergence rate, often requiring more iterations compared to more advanced numerical techniques.

## Numerical Examples

The bisection method solver outlined above is used to solve five numerical examples. The first three examples involve algebraic equations: the first is a linear equation with a single root, the second is a quadratic equation with two distinct real roots, and the third is a cubic equation with three distinct real roots. The focus then shifts to mechanics for the final two examples: the fourth involves finding the position of a balance force in a cantilever beam, while the fifth calculates a center of mass for several masses.

The solver outputs a table displaying the iteration number, the interval boundaries $a$ and $b$, the mid-point $c$, and the absolute value of the function at the midpoint, $|f(c)|$, for each iteration in the procedure
