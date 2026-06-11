Notes on memoisation (in dynamic programming) before attempting code on it (and approaching the Fibonnacci Sequence `cses.fi` problem): 

Say there is a searching problem that requires a recursive search of a branch. The example used in the video was of climbing stairs (and brute forcing the number of possibilities of climbing the steps). 

At the top of the staircase of $n$ stairs, the stepcount would be a function of n, $f(n)$.

Now let's assume that one can either go up stairs one at a time, by skipping a stair or by skipping three (an athlete doing strides for example): the possibility of steps to take when at the top and thinking of how many possibilites have lead to that point would be:

$$f(n-1), f(n-2), f(n-4)$$

The goal would be to find how many branches end at $f(0)$ but in searching for this there would be many repeated branches. For example, in the first step the third branch is $f(n-4)$ but so to is one of the branches from the initial third row, just two steps after it (assuming -1 then -2). To compute the values for the entire branch following $f(n-4)$ onwards would be pointless since they would always be the same. 

Memoisation - or caching - is where a script is written such that if that instance comes up where a redundant branch has been found later in the code, it will just search for the list of stored list values and output that same output without wasting extra compute. 
