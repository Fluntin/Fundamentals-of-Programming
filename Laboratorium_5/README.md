## Amino Acids

In our cells, amino acids are a fundamental component where specific sequences of thousands of amino acids form proteins. Proteins can then further form hormones or neurotransmitters. Specifically, there are three "steps" on the DNA spiral (actually RNA) that code for an amino acid, where each step can be one of the nitrogen bases CGAT. This forms a number system with a base of 4, and with three "digits" (i.e., steps), we have 4^3 = 64 combinations. However, not all of these combinations are used, and we have 20 amino acids. Your task is to write a program that reads these amino acids from a text file named "aminosyror.txt" (available under Files/Laborationer) and stores them as a list of objects. Each object should have the following properties (instance variables):

- Code (e.g., "K")
- Name (e.g., "Lysine")
- Group (e.g., "Basic")
- Molecular weight (e.g., 146.19)

The user should then be able to get a sorted printout of the list, where the user chooses which property to sort on. A sample run could look like this (program output is shown in red, user input is shown in green):

```
Reading amino acids...
...done.
1 - Print table of amino acids sorted by code
2 - Print table of amino acids sorted by name
3 - Print table of amino acids sorted by group
4 - Print table of amino acids sorted by molecular weight

Enter your choice: 3
H Histidine Basic 155.16
K Lysine Basic 146.19
R Arginine Basic 174.2
C Cysteine Hydrophilic 121.16
N Asparagine Hydrophilic 132.12
Q Glutamine Hydrophilic 146.15
S Serine Hydrophilic 105.09
T Threonine Hydrophilic 119.12
Y Tyrosine Hydrophilic 181.19
A Alanine Hydrophobic 89.09
F Phenylalanine Hydrophobic 165.19
G Glycine Hydrophobic 75.07
I Isoleucine Hydrophobic 131.17
L Leucine Hydrophobic 131.17
M Methionine Hydrophobic 149.21
P Proline Hydrophobic 115.13
V Valine Hydrophobic 117.15
W Tryptophan Hydrophobic 204.23
D Aspartic Acid Acidic 133.1
E Glutamic Acid Acidic 147.13
```

Please note that the order of the amino acids may differ depending on the chosen property to sort on.

Tips:
- Implement a method for printing the objects using the `__str__` method.
- Create a function to read the list of objects from the file.
- Implement the main program to handle user input and call the appropriate functions/methods.
