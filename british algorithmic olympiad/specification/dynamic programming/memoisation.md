Notes on memoisation (in dynamic programming) before attempting code on it (and approaching the Fibonnacci Sequence `cses.fi` problem): 

Say there is a searching problem that requires a recursive search of a branch. The example used in the video was of climbing stairs (and brute forcing the number of possibilities of climbing the steps). 

At the top of the staircase of $n$ stairs, the stepcount would be a function of n, $f(n)$.

Now let's assume that one can either go up stairs one at a time, by skipping a stair or by skipping three (an athlete doing strides for example): the possibility of steps to take when at the top and thinking of how many possibilites have lead to that point would be $f(n-1), f(n-2), f(n-4)$
