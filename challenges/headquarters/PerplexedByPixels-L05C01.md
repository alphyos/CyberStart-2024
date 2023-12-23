# 🎨 Perplexed By Pixels - L05 C01

The Yakoottees love their cars. And so you'd expect that they might send each other car photos, images and even art. But recently we intercepted something strange: a pixel drawing of a car. What's strange about it? One of the gang, Kanako, sent two copies of it to another gang member. After some initial analysis we noticed some slight variations in colour in a selection of pixels.

One of the team has already built a comparison tool but he's just been reassigned to another urgent project. Perhaps you could take a look at what he's built and finish the analysis.

**Tip:** Calculate the differences, convert it with the ASCII table, and that's your flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: It looks like they're using the change in rgb values between the pixels to generate a set of numbers, which they're then converting to text with the help of an ASCII table. Work out the differences, do the conversion and there's your flag.

</details>

<details><summary>

## Step by Step</summary>

- Click the analyze button which will give you the output below when done.

![image of analysis](/assets/perplexedbypixels1.png)

- Adding the first three sets of numbers together and subtracting that from the added total of the second set of numbers gives you the difference.
- The absolute value of this number is what you will type into the column boxes as shown below in the same order of 01, 02, etc from top to bottom.

![image of ascii converter](/assets/perplexedbypixels2.png)

</details>
