# Summary Results Matrix

## 1. Assignment Description

In this assignment, we were given a buggy implementation of a triangle classification program and tasked with writing a comprehensive set of test cases to uncover its defects. After documenting the test results, we then fixed the bugs in the original code, without rewriting it from scratch and then verified that all tests passed.

## 2. Author

- Name: Hamel Desai

## 3. Honor Pledge

## 4.Summary

The initial implementation of `classifyTriangle()` contained 5 defects. In Test Run 1, only 3 out of 18 tests passed, all of which were InvalidInput cases that happened to be caught by earlier validation checks before reaching the logic. Every test for valid triangle classification (Right, Equilateral, Isosceles, Scalene) and NotATriangle failed because a typo on line 34 (`b <= b` instead of `b <= 0`) caused nearly all inputs to be rejected as `InvalidInput` before any triangle logic could execute.

After identifying and fixing all 5 bugs through code inspection and test-driven debugging, Test Run 2 achieved 18 out of 18 tests passing.

|                | Test Run 1 (Buggy) | Test Run 2 (Fixed) |
|----------------|---------------------|---------------------|
| Tests Planned  | 18                  | 18                  |
| Tests Executed | 18                  | 18                  |
| Tests Passed   | 3                   | 18                  |
| Defects Found  | 5                   | 0                   |
| Defects Fixed  | 0                   | 5                   |

### Test Strategy

The strategy for determining test coverage was based on three principles:

1. Category coverage: Every possible return value of `classifyTriangle()` — Right, Equilateral, Isosceles, Scalene, NotATriangle, and InvalidInput has 3 dedicated test cases. This ensures every branch in the classification logic is fully tested.

2. Permutation coverage: For categories where side order matters (Right, Isosceles, and NotATriangle), the 3 test cases rotate which position (a, b, or c) holds the key value. For example, right triangles are tested as `(3,4,5)`, `(5,3,4)`, and `(5,12,13)` to verify the Pythagorean check works regardless of which side is the hypotenuse. Similarly, Isosceles tests place the equal pair in each position: `(2,2,3)`, `(3,2,2)`, `(2,3,2)`.

3. InvalidInput boundary types: Rather than testing one type of bad input 3 times, each test targets a different validation rule: negative values (`-1,1,1`), zero values (`(0,1,1)`), and values exceeding 200 (`201,1,1`), to confirm all three input guards work independently.

## 5. Reflection

The biggest takeaway from this assignment was how a single small bug can mask every other defect in a program. The `b <= b` typo on line 34 caused 15 out of 18 tests to fail with the same `InvalidInput` result, making it impossible to evaluate the rest of the logic until that one fix was in place.

What worked: Writing tests before fixing any bugs was valuable (it kind of reminded of test driven development). Having a full test suite in place before touching `Triangle.py` meant that each fix could be validated immediately and I could confirm that fixing one bug didn't break something else. The permutation-based test design also paid off because it caught the right triangle bug where only one ordering of `a² + b² = c²` was checked.

What didn't work (at first): Reading the buggy code in isolation, some defects were subtle: `a * 2` vs `a ** 2` and `b == a` vs `b == c` are easy to miss on visual inspection alone. The test results made these bugs obvious in a way that code review alone might not have. This reinforced that testing and code inspection are complementary, not interchangeable.
