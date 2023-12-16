# 📞 Calling Yaroslav - L10 C02

Agent 707, we know the gang are attacking soon, so it's time to start bringing them in. This morning our agents picked up one of the gang's henchmen, Yaroslav, because we knew he had the time and date of the attack on his phone. The trouble is, we've looked at his phone and it contains a sophisticated eight-digit PIN locking system. It's based on a math problem, and we want you to crack it.

Here's what we know: when the phone was first started the PIN code code to log in was 4096. Every time we enter the PIN code, the number of times the PIN code has been entered correctly in the past is added to the value of the PIN code, to get the new PIN. We know the system has been used 5520 times before. What will the PIN code be this time?

Tip: Get the right PIN code to get the flag. All we know at the moment is that it's definitely eight digits long.

💡 Hint: The easiest ways to calculate this are to break it down into pieces and write a script to calculate it,
   or use a mathematical equation.

The PIN code was originally 4096. When the code was 4096 the number of times the code was entered in the past was 0. So your solution needs to add the code to the number of times the PIN code was entered, then add 1 to the number of times the code was entered, and repeat that 5521 times to get the correct result.

## Step by Step

- All you need to do to solve this problem is add the initial value of 4096 to the sum of all integers from 1 to 5521 (we know it has been put in correctly 5520 times so this time we need to use 5521)
- To get that sum we can use Gauss summation formula `(n*(n-1))/2`
- The correct pin will be the result of `4096 + (5521*5520)/2`
- Put that into a calculator and you get `15242056`
- Click those numbers on the phone and you will get the flag

`flag: mbljBmpNNXikgBFc6dDU`
