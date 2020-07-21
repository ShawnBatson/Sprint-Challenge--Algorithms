#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) This will be O(n) with a linear runtime. The input is fixed, so no matter what it will cap out at n _ n _ n. There will be one call per input, and the presence of a while loop directly relates to the size/amount of input.

b) O(n^2) The runtime for B is O(n^2) due to the fact that there are two loops. one for loop, and one while loop. The for loop will iterate through each within range, and check to see if the n fits the while stipulation. If it does, then it will go through the while loop. Because there is only information enough to tell that every i in range(n) will trigger the while loop, then worst case scenario is O(n^2) - O(nLogn) - correct answer

c) O(n) Even though it's recursive, it will still be O(n) since it's only performing one action on each input until the base case is reached.

## Exercise II

Egg breaks on floor >= f
egg doesn't break on floor < f

We would use a binary search method.
We start at 0. We go to floor 100 and drop it. if it breaks, we will cut that in half and try floor 50, if it breaks again, we try floor 25, if it breaks again, we halve that again until it does not break. When we find the half-mark where it does not break, then between the previous floor and the floor where it didn't break is the maximum safest floor. We will them repeat the step, breaking it down in halves. We will eventually be between two numbers, and we'll easily be able to single out the highest safest floor, while breaking the fewest possible eggs. This would be O(log(n)) because it is using division to cut out half the amount of possibilites per n value
