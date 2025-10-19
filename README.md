# Perfect Numbers via the σ-Rectangle *(ex “beautiful numbers”; historical label only, no distinct class)*

## Overview
This project presents a **new algorithm** for identifying perfect numbers using the **sigma-rectangle (SR)** built from triangular numbers. The algorithm **starts by enumerating triangular numbers** $T_k=\frac{k(k+1)}{2}$ and, for each $k$, tests the SR pattern on the $k\times(k+1)$ rectangle with parameters $k$ and $L=\frac{k+1}{2}$ (with $\gcd(k,L)=1$). The SR framework distinguishes the **SR median** from the **middle column** and uses the divisor pairing $d\mapsto M/d$ within the rectangle to validate $\sigma(M)=2M$. Crucially, this method **does not rely on Mersenne primes**; it couples divisibility with the SR structural constraints to efficiently and incrementally reveal perfect numbers. *(Formerly called “beautiful numbers”; this was only a working label and does not denote a different class of integers.)*


## Concept and Structure

### 1. Triangular Numbers and Sigma Rectangle
The foundation of this algorithm is the **triangular number** \( T \), calculated as the sum \( T = 1 + 2 + 3 + ... + n \), where **side length** \( n \) represents the last integer in the sequence. This triangle is aligned along the x-axis, with one vertex at the origin \(0, 0\).

To analyze and validate the properties of a triangular number, we mirror the triangular shape to form a **sigma rectangle** \( R \) by combining two triangles of length \( T \) (i.e., \( T + T = R \)). This rectangle provides a structured framework to verify if a triangular number is perfect by examining both its geometric and divisional properties.

### 2. Incremental Filtering and Section Creation
- **Incremental Verification:** We apply filters to eliminate numbers that don’t meet the criteria, focusing computational resources only on promising candidates.
- **Columns and Rows in the Sigma Rectangle:** The rectangle’s structure is derived from the triangle’s side length. The **rows** are equal to the side length plus 1 (to account for vertical alignment), while half of the x-axis represents the **median length** of the triangle.
- **Sections in the Rectangle:** Each section within the sigma rectangle is incrementally validated based on rows and columns:
  - The **columns** of the first section are calculated as \( \text{median length} / \text{first divisor} \).
  - The **rows** of the first section are set to the triangle’s side length minus 1.
  - Each subsequent section is refined step-by-step, based on the remaining length, to build up the divisor properties until the last columns are reached.

### 3. Divisors Before and After the Median
- **Incremental Divisor Validation:** Divisors are calculated only after each section is created, to avoid unnecessary computations. The number of dots in each section is checked against the divisors before the median, proceeding one section at a time until only two columns remain.
- **Final Check with Divisors After Median:** The last column in the rectangle, located at the midpoint, serves as a symmetry point for verifying divisors after the median, ensuring the number's perfection according to the sigma properties.

## Key Features of the Algorithm
- **New Geometric Pattern:** This algorithm is based on a newly identified geometric pattern in triangular numbers that aids in identifying perfect numbers more efficiently.
- **Redefined Perfect Numbers:** Beautiful triangular numbers redefine perfect numbers by combining divisibility with structural geometry, aiming to uncover all perfect numbers through an incremental approach.
- **Median Length as a Symmetry Reference:** The sum of all divisors is used as a median reference, ensuring symmetry within the sigma rectangle.
- **Efficient, Step-by-Step Divisor Verification:** Divisors are computed only as needed, minimizing unnecessary calculations and providing a streamlined method for identifying perfect numbers.

## Project Goals
This project redefines the concept of perfect numbers by:
1. Using beautiful triangular numbers as an incremental framework to identify all perfect numbers.
2. Leveraging geometric symmetry and divisibility to create a structured, computationally efficient verification process.
3. Ensuring that each candidate number meets stringent criteria through a layered, section-based approach within the sigma rectangle.

## Usage and Application

### Running the Code
This repository includes Python scripts to:
- Efficiently generate and filter triangular numbers.
- Construct sigma rectangles and verify each section incrementally.
- Perform divisor checks to confirm conformity with the criteria for beautiful triangular numbers, aiding in the discovery of perfect numbers.

### Important Notes
1. **Range Adjustment**: The variable `limit_T` determines the range of numbers tested. By default, `limit_T = 34000000` is set to identify the first 5 beautiful triangular numbers. Users can adjust `limit_T` as needed.
   
2. **Drawing the Structure**: The code includes optional drawing functions to visualize the structure of beautiful triangular numbers. By default, these drawing lines are **commented out** to optimize performance. To view the geometric structure, simply **uncomment** the relevant lines in the code.

3. **Performance Optimization**: This code currently runs on a CPU. A version optimized for GPU computation is under development and will be released in a future update.

4. **Note on the Inclusion of the Number 6**

One interesting exception in the results of this algorithm is the number 6. Although the algorithm identifies 6 as a "beautiful triangular number," it does not strictly align with the geometric and divisor-based structure expected of such numbers. The inclusion of 6 occurs because:

- Semiprime Structure: As the product of two primes, 6=2×3, 6 satisfies the initial divisibility checks without requiring additional sections in the sigma rectangle structure.
- Triangular Properties: 6 is a triangular number that also happens to be the smallest perfect number, as 6=1+2+3. These properties allow 6 to meet the initial checks set by the algorithm, even though it bypasses the layered structure needed for larger beautiful triangular numbers.

This behavior is not a bug but rather an artifact of 6’s simplicity. Its inclusion provides insight into the algorithm's behavior with small numbers and highlights the unique mathematical characteristics of 6.

This project not only redefines perfect numbers through beautiful triangular structures but also opens a pathway for further exploration of efficient, incremental methods in number theory.
