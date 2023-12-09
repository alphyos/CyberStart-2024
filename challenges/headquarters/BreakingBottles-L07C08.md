# 🍾 Breaking Bottles - L07 C08

Agent 707, we think we now know how the Chiquitoos' plan to distribute the Cola they steal. One of the gang's supposedly legitimate businesses is actually a bottling plant... and one of the things they bottle is Cola. We think they might be planning to re-label the bottles they steal as another brand they already bottle, making a huge mark-up and meaning the stolen Cola will effectively just disappear! Clever.

We think we might have a way in. The bottling plant has a website and there is a form where you can request a price list for their bottling services. We think it might be vulnerable to command injection, and there's a text file we believe you could access with "recipe" in the file name, which actually includes details about their plan. But here's the issue - they've added a filter to the form, which prevents the use of semi-colons. See if you can find a way around it.

**Tip:** Open the file to get the flag.

```
💡 Hint: What other characters can be used instead of semi-colons to perform a command injection? Think about pipes.
   Oh, and we now know the file you need to find is called "cola_recipe.txt".
```

### Step by Step

- Navigate to the most bottom query where it says "Any message"
- Type "``ls`" and press send. Text should pop up with various .txt file names
    - Remember, you are looking for a **cola recipe**
    ![sending message](/assets/breakingbottles1.png)
- Type "``cat cola_recipe.txt`" and press send. The flag should appear

![sending message](/assets/breakingbottles2.png) ![sending message](/assets/breakingbottles3.png)
