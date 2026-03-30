# Test Report: Fixed classifyTriangle() Implementation

## Bugs Fixed

1. **Line 34:** `b <= b` changed to `b <= 0` — original always evaluated True, rejecting all inputs
2. **Line 46:** Triangle inequality used subtraction (`b - c`, `a - c`) instead of addition — changed to `b + c`, `a + c`
3. **Line 50:** Equilateral check `a == b and b == a` was redundant — changed to `a == b and b == c`
4. **Line 52:** Right triangle used `a * 2` (multiply) instead of `a ** 2` (square) — also added all three permutations
5. **Line 54:** Scalene check repeated `a != b` twice — changed second to `a != c`

## Test Results

| Test ID | Input | Expected Result | Actual Result | Pass or Fail |
|---------|-------|----------------|---------------|-------------|
| testRightTriangleA | 3,4,5 | Right | Right | Pass |
| testRightTriangleB | 5,3,4 | Right | Right | Pass |
| testRightTriangleC | 5,12,13 | Right | Right | Pass |
| testEquilateralA | 1,1,1 | Equilateral | Equilateral | Pass |
| testEquilateralB | 10,10,10 | Equilateral | Equilateral | Pass |
| testEquilateralC | 100,100,100 | Equilateral | Equilateral | Pass |
| testIsoscelesA | 2,2,3 | Isoceles | Isoceles | Pass |
| testIsoscelesB | 3,2,2 | Isoceles | Isoceles | Pass |
| testIsoscelesC | 2,3,2 | Isoceles | Isoceles | Pass |
| testScaleneA | 3,4,6 | Scalene | Scalene | Pass |
| testScaleneB | 7,8,9 | Scalene | Scalene | Pass |
| testScaleneC | 10,11,12 | Scalene | Scalene | Pass |
| testNotATriangleA | 1,2,3 | NotATriangle | NotATriangle | Pass |
| testNotATriangleB | 1,1,10 | NotATriangle | NotATriangle | Pass |
| testNotATriangleC | 10,1,1 | NotATriangle | NotATriangle | Pass |
| testInvalidInputNeg | -1,1,1 | InvalidInput | InvalidInput | Pass |
| testInvalidInputZero | 0,1,1 | InvalidInput | InvalidInput | Pass |
| testInvalidInputOver | 201,1,1 | InvalidInput | InvalidInput | Pass |

**Summary:** 18 tests ran. 18 passed, 0 failed. All defects in classifyTriangle() have been fixed.
