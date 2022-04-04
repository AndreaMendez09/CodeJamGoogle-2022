# CodeJamGoogle-2022
 Ejercicios realizados en las rondas que participe de la CodeJam 2022


# Enunciado ejercicio Punched Cards

A secret team of programmers is plotting to disrupt the programming language landscape and bring punched cards back by introducing a new language called Punched Card Python that lets people code in Python using punched cards! Like good disrupters, they are going to launch a viral campaign to promote their new language before even having the design for a prototype. For the campaign, they want to draw punched cards of different sizes in ASCII art.

The ASCII art of a punched card they want to draw is similar to an R×C
matrix without the top-left cell. That means, it has (R⋅C)−1

cells in total. Each cell is drawn in ASCII art as a period (.) surrounded by dashes (-) above and below, pipes (|) to the left and right, and plus signs (+) for each corner. Adjacent cells share the common characters in the border. Periods (.) are used to align the cells in the top row.

For example, the following is a punched card with R=3
rows and C=4

columns:

..+-+-+-+
..|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+

There are more examples with other sizes in the samples below. Given the integers R and C describing the size of a punched card, print the ASCII art drawing of it as described above.

## Input

The first line of the input gives the number of test cases, T.T lines follow, each describing a different test case with two integers R and C: the number of rows and columns of the punched card that must be drawn.

## Output

For each test case, output one line containing Case #x:, where x is the test case number (starting from 1). Then, output (2*R)+1 additional lines with the ASCII art drawing of a punched card with R rows and C columns.

## Limits

Time limit: 5 seconds.
Memory limit: 1 GB.

## Test Set 1 (Visible Verdict)

1≤T≤81
2≤R≤10
2≤C≤10

## Sample input

3
3 4
2 2
2 3

## Sample output

Case #1:
..+-+-+-+
..|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
|.|.|.|.|
+-+-+-+-+
Case #2:
..+-+
..|.|
+-+-+
|.|.|
+-+-+
Case #3:
..+-+-+
..|.|.|
+-+-+-+
|.|.|.|
+-+-+-+

# 3D Printing

You are part of the executive committee of the Database Design Day festivities. You are in charge of promotions and want to print three D's to create a logo of the contest. You can choose any color you want to print them, but all three have to be printed in the same color.

You were given three printers and will use each one to print one of the D's. All printers use ink from 4
individual cartridges of different colors (cyan, magenta, yellow, and black) to form any color. For these printers, a color is uniquely defined by 4 non-negative integers c, m, y, and k, which indicate the number of ink units of cyan, magenta, yellow, and black ink (respectively) needed to make the color.

The total amount of ink needed to print a single D is exactly 106 units. For example, printing a D in pure yellow would use 106 units of yellow ink and 0 from all others. Printing a D in the Code Jam red uses 0 units of cyan ink, 500000 units of magenta ink, 450000 units of yellow ink, and 50000 units of black ink.

To print a color, a printer must have at least the required amount of ink for each of its 4 color cartridges. Given the number of units of ink each printer has in each cartridge, output any color, defined as 4 non-negative integers that add up to 106, such that all three printers have enough ink to print it.

## Input

The first line of the input gives the number of test cases, T.T test cases follow. Each test case consists of 3 lines. The i-th line of a test case contains 4 integers Ci, Mi, Yi, and Ki, representing the number of ink units in the i-th printer's cartridge for the colors cyan, magenta, yellow, and black, respectively.

##Output

For each test case, output one line containing Case #x
: r, where x is the test case number (starting from 1) and r is IMPOSSIBLE if there is no color that can be printed by all 3 printers. Otherwise, r must be equal to "c m y k" where c, m, y, and k are non-negative integers that add up to 106 and c≤Ci, m≤Mi, y≤Yi, and k≤Ki, for all i.
If there are multiple solutions, you may output any one of them. (See "What if a test case has multiple correct solutions?" in the Competing section of the FAQ.) This information about multiple solutions will not be explicitly stated in the remainder of the 2022 contest.

## Limits

Time limit: 5 seconds.
Memory limit: 1 GB.

## Test Set 1 (Visible Verdict)

1≤T≤100
0≤Ci≤106, for all i.
0≤Mi≤106, for all i.
0≤Yi≤106, for all i.
0≤Ki≤106, for all i.


## Sample input

3
300000 200000 300000 500000
300000 200000 500000 300000
300000 500000 300000 200000
1000000 1000000 0 0
0 1000000 1000000 1000000
999999 999999 999999 999999
768763 148041 178147 984173
699508 515362 534729 714381
949704 625054 946212 951187

## Sample output

Case #1: 300000 200000 300000 200000
Case #2: IMPOSSIBLE
Case #3: 400001 100002 100003 399994

# d1000000

While the most typical type of dice have 6 sides, each of which shows a different integer 1 through 6, there are many games that use other types. In particular, a dk is a die with k sides, each of which shows a different integer 1 through k. A d6 is a typical die, a d4 has four sides, and a d1000000 has one million sides.

In this problem, we start with a collection of N
dice. The i-th die is a dSi, that is, it has Si sides showing integers 1 through Si. A straight of length ℓ starting at x is the list of integers x,x+1,…,x+(ℓ−1). We want to choose some of the dice (possibly all) and pick one number from each to form a straight. What is the longest straight we can form in this way?

## Input

The first line of the input gives the number of test cases, T.T test cases follow. Each test case is described in two lines. The first line of a test case contains a single integer N, the number of dice in the game. The second line contains N integers S1,S2,…,SN, each representing the number of sides of a different die.

## Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of input dice that can be put in a straight.

## Limits

Memory limit: 1 GB.
1≤T≤100

## Test Set 1 (Visible Verdict)

Time limit: 5 seconds.
1≤N≤10
4≤Si≤20, for all i 

## Test Set 2 (Visible Verdict)

Time limit: 15 seconds.
1≤N≤105
4≤Si≤106, for all i.

## Sample input

4
4
6 10 12 8
6
5 4 5 4 4 4
10
10 10 7 6 7 4 4 5 7 4
1
10

## Sample output

Case #1: 4
Case #2: 5
Case #3: 9
Case #4: 1

