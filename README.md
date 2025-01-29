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

### Numerical Example 1


For the first numerical example, we consider the linear function:

$$ f(x) = 7(x - 11) + 13.$$

Using `bisection.py`, the user is first prompted to enter the function. In this case, they should input  `7*(x-11)+13`. Next, the user is asked to enter the lower and upper bounds, $a$ and $b$, respectively. For instance, if the user initially tries:

$$
a = 10, \quad b = 20,
$$

the code will display the message: 

**"A root in this interval is not guaranteed. Please try another interval."**

This occurs because $f(10)$ and $f(20)$ have the same sign, meaning the existence of a root in this interval cannot be assured. A better choice would be:

$$
a = 0, \quad b = 20.
$$

After specifying the interval, the user is prompted to define the tolerances $\epsilon_1$ and $\epsilon_2$. A valid selection could be:

$$
\epsilon_1 = \epsilon_2 = 0.001.
$$

With these parameters, the solver successfully finds a root at $c = 9.142456$ after $15$ iterations. Throughout the procedure, the solver also prints the convergence history, detailing the progress of the bisection method at each iteration.

### Numerical Example 2

For the second numerical example, we consider the quadratic function:

$$ f(x) = 5x^2 - 10.$$

Similar to the previous example, using `bisection.py`, the user should enter `5*x**2-10` to define the function. One possible set of bounds to get a root is:

$$
a = -20, \quad b = 0.
$$

When tolerances $\epsilon_1 = \epsilon_2 = 0.001$ are used, the solver successfully finds a root at $c = -1.414185$ after $15$ iterations.

As the equation is quadratic, we would expect that there is a second root. Using the same tolerances, another possible set of bounds to get the second root is:

$$
a = 0, \quad b = 20.
$$

The solver successfully finds the second root at $c = 1.414185$ after $15$ iterations.



### Numerical Example 3

In a similar fashion, using `bisection.py`, we consider the following cubic function:

$$ f(x) = x^3 - 4x^2-5x+6.$$

This example clearly shows the difficulty faced by the bisection method when there are multiple roots.

The user should enter `x**3-4*x**2-5*x+6` to define the function. One possible set of bounds to get a root is:

$$
a = -10, \quad b = 10.
$$

When tolerances $\epsilon_1 = \epsilon_2 = 0.001$ are used, the solver successfully finds a root at $c = -1.577759$ after $15$ iterations.

One needs to keep trial-and-error different bounds in order to attain the other two roots.

### Numerical Example 4

A cantilever beam with length $L$ is subjected to a uniformly distributed load $w$. A balance force $P$ is required to be applied in the opposite direction at some distance $x$ measured from the clamping point $A$, such that the bending moment reaction $M_A$, vanishes.

From simple static analysis, the summation of the moments at point $A$ is given by

$$ \Sigma M = M_A - (w)(L)(\frac{L}{2}) + (P)(x) = 0.$$

As it is required that $M_A=0$, the distance $x$ is given by:

$$x = \frac{wL^2}{2P},$$

and must fall within the interval $[0, L]$, as otherwise it would be physically impossible to apply the force on the beam.

A function $f(x)$ is formulated as follows:

$$f(x) = x - \frac{wL^2}{2P} = 0$$

Using `cantilever.py`, the lower and upper bounds $a$ and $b$ are automatically set to be $0$ and $L$, respectively.

The user is prompted to input $L$, $w$, and $P$, respectively. One could try

$$
L = 10, \quad w = 169, \quad P = 11.
$$

The code will display the message: 

**"Static balance with the entered parameters is impossible. Please try different values.**

The reason is that, even if the balance force is applied at the tip of the cantilever beam, the induced moment will not be sufficient to balance the moment due to the uniformly distributed load. Thus the user is prompted to enter another set of parameters.

A more sensible set of parameters is 

$$
L = 8, \quad w = 3, \quad P = 13.
$$

When using tolerances $\epsilon_1 = \epsilon_2 = 0.001$, the solver successfully finds that the balance force $P$ should be applied at $x = 7.384766$ after $12$ iterations.

In this example, it is important to make sure that the units of the entered valued are consistent.


### Numerical Example 5

Given $n$ point masses $m_1, m_2, \ldots, m_n$, positioned at $x_1, x_2, \ldots, x_n$, along a one-dimensional axis.

By definition, the sum of moments about the center of mass, $x_{COM}$​, must be zero. Mathematically, this condition is expressed as:

$$f(x_{COM} ) = \sum_i m_i (x_i-x_{COM} ) = 0.$$

Since the center of mass must lie within the range of the given positions, it follows that:

$$x_{COM} \in [x_1, x_n],$$

where  $x_1$  and  $x_n$  represent the positions of the first and  $n^{\text{th}}$ masses, respectively.

In `mass_center.py`, the user is prompted to input the number of involved masses, $n$. Then, the code prompts the user to enter each mass and its position, $m_i$ and $x_i$, respectively.

The lower and upper bounds $a$ and $b$ are automatically set to be $x_1$ and $x_n$, respectively, as physically, it cannot be otherwise.

For instance, when the masses and positions are given as in the following table:

<div align="center">

| Mass ($m$) | Position ($x$) |
|----------|-------------|
| $m_1 = 10$ | $x_1 = -5$ |
| $m_2 = 5$  | $x_2 = 0$  |
| $m_3 = 20$ | $x_3 = 5$  |
| $m_4 = 18$ | $x_4 = 7$  |

</div>

using the tolerances $\epsilon_1 = \epsilon_2 = 0.001$, the solver successfully finds that the center of mass $x_{COM}$ at $x = 3.321045$ after $14$ iterations.

In this example, it is important to make sure that the units of the entered valued are consistent.
