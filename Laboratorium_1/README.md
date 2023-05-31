## Program 1: Savings Over Time

Write a program that prompts the user to:

1. Enter an amount to deposit.
2. Enter a time period (in years) for which the amount will be compounded.
3. Enter an interest rate in percentage.

The program should then calculate and display the final value of the deposit.

Requirements: Use a function to calculate the final value. The function should have appropriate input parameters and return the calculated value.

## Program 2: Calculate Earth's Mass

By knowing the satellite's orbital period and distance from Earth, we can calculate Earth's mass. Earth has a natural satellite (the Moon) and thousands of artificial satellites. The formula to calculate the distance is as follows:

If we know the orbital period and distance to a satellite orbiting a planet, it's possible to calculate the planet's mass.

$$
\begin{aligned}
& m_p=\text{Mass of the planet} \quad(\text{kg}) \\
& m_s=\text{Mass of the satellite} \quad(\text{kg}) \\
& r=\text{Distance between the satellite and the planet} \quad(10^6 \text{ m}) \\
& T=\text{Satellite's orbital period (hours)} \\
& v=\text{Satellite's orbital velocity} \quad(\text{m/s}) \\
& G=\text{Gravitational constant}=6.67 \times 10^{-11} \quad(\text{Nm}^2/\text{kg}^2) \\
\end{aligned}
$$

The satellite's velocity v is calculated as follows:

$$
v=\frac{2 \pi r}{T}
$$

According to the law of gravitation:

$$
\frac{m_s v^2}{r}=G \cdot \frac{m_s m_p}{r^2}
$$

Substituting the formula for velocity v, we obtain the following expression for the planet's mass:

$$
m_p=\frac{4 \pi^2 r^3}{G T^2}
$$

Write a program that asks for the distance and orbital period (considering the appropriate units) and then calls a function to calculate the mass using the formula above. Look up the value for the Moon or the ISS (International Space Station) and see if it matches.
Earth's mass should be approximately $6$ x $10^{24}$ kg.
