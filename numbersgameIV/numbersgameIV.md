 play a number game.

At first,A is (1,0) and B is (0,1)
Let's say that A is (Xa, Ya) and B is (Xb, Yb).
On the each move you can replace either A or B with (Xa + Xb, Ya + Yb).

For the given state (m, n) you are asked to find the minimum number of moves required to reach a state where A + B = (m, n) (i.e.Xa + Xb = m and Ya + Yb = n).

Return the minimum number of moves to get A + B = (m, n) or -1 if it is impossible.

Examples:

NumberGameIV(1,1) = 0
A + B = (1,0) + (0,1) = (1,1)
So the answer is 0.

NumberGameIV(4,7) = 4
You need at least 4 moves to do that.
Move________A________B_______A+B
At_First__(1,0)____(0,1)____(1,1)
Replace_A_(1,1)____(0,1)____(1,2)
Replace_B_(1,1)____(1,2)____(2,3)
Replace_A_(2,3)____(1,2)____(3,5)
Replace_A_(3,5)____(1,2)____(4,7)
So the answer is 4.

NumberGameIV(2,2) = -1
After trying a small number of moves, it is clear that that there is no way to reach the state where A + B = (2,2).
so the answer is -1.

Reference: http://codeforces.com/problemset/problem/585/C

[input] integer m

1 ≤ m < 230.
[input] integer n

1 ≤ n < 230.
[output] integer

The minimum number of moves required to get A + B = (m, n), or -1 if it's impossible.
