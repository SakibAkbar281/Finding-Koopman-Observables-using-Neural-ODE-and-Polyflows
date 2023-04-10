# learning-dynamics-from-data

## Introduction
The aim of this project is to use Neural Ordinary Differential Equations (Neural ODE) to learn the unknown dynamics of a system from time series data. 


## Problem Statement

The problem at hand concerns discovering the unknown dynamics of a given dynamical system, represented by the equation $\dot{x} =f(x)$ with a specified initial condition $x(0)=x_{0}$. The data available for analysis is the time series data of $x(t)$ for the aforementioned initial condition $x_{0}$.

To address this problem, we have selected the Lotka-Volterra or Predator-Prey dynamical system, described by the equations:

$$\begin{align*}
\begin{bmatrix}
\dot{x}_{1}\\
\dot{x}_{2}
\end{bmatrix} & =\begin{bmatrix}
ax_{1} -bx_{1} x_{2}\\
cx_{1} x_{2} -dx_{2}
\end{bmatrix} =f( x) ,\\
\begin{bmatrix}
x_{1}( 0)\\
x_{2}( 0)
\end{bmatrix} & =\begin{bmatrix}
1\\
1
\end{bmatrix}
\end{align*}$$

Here, the values of $a,b,c,$ and $d$ are predefined as $1.5,1,1,$ and $0.5$ respectively. However, the governing dynamics function $f(x)$ is unknown.

The objective of this project is to develop a neural network that can approximate $\dot{x}\_{1}$ and $\dot{x}\_{2}$ from the given time series data of $x_{1} (t)$ and $x_{2} (t)$, thus allowing us to discover the unknown dynamics $f(x)$.

