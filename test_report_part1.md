# Test Report: Initial classifyTriangle() Implementation

| Test ID | Input | Expected Result | Actual Result | Pass or Fail |
|---------|-------|----------------|---------------|-------------|
| testRightTriangleA | 3,4,5 | Right | InvalidInput | Fail |
| testRightTriangleB | 5,3,4 | Right | InvalidInput | Fail |
| testRightTriangleC | 5,12,13 | Right | InvalidInput | Fail |
| testEquilateralA | 1,1,1 | Equilateral | InvalidInput | Fail |
| testEquilateralB | 10,10,10 | Equilateral | InvalidInput | Fail |
| testEquilateralC | 100,100,100 | Equilateral | InvalidInput | Fail |
| testIsoscelesA | 2,2,3 | Isoceles | InvalidInput | Fail |
| testIsoscelesB | 3,2,2 | Isoceles | InvalidInput | Fail |
| testIsoscelesC | 2,3,2 | Isoceles | InvalidInput | Fail |
| testScaleneA | 3,4,6 | Scalene | InvalidInput | Fail |
| testScaleneB | 7,8,9 | Scalene | InvalidInput | Fail |
| testScaleneC | 10,11,12 | Scalene | InvalidInput | Fail |
| testNotATriangleA | 1,2,3 | NotATriangle | InvalidInput | Fail |
| testNotATriangleB | 1,1,10 | NotATriangle | InvalidInput | Fail |
| testNotATriangleC | 10,1,1 | NotATriangle | InvalidInput | Fail |
| testInvalidInputNeg | -1,1,1 | InvalidInput | InvalidInput | Pass |
| testInvalidInputZero | 0,1,1 | InvalidInput | InvalidInput | Pass |
| testInvalidInputOver | 201,1,1 | InvalidInput | InvalidInput | Pass |

**Summary:** 18 tests ran. 3 passed, 15 failed. The `b <= b` bug on line 34 of Triangle.py causes nearly all valid inputs to be incorrectly rejected as `InvalidInput`.
