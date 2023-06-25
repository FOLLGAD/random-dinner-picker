I understand that you want to create a program that takes the names of your friends and the cost of their dinner as input, and then randomly selects a person to pay for the dinner, with the probability of being selected weighted by the cost of their dinner. I will create a Python program for this purpose.

Here's the plan for the architecture:

1. Create a `Person` class to store the name and cost of dinner for each person.
2. Create a `Dinner` class to store a list of `Person` objects and handle the random selection of a person to pay for the dinner.
3. Create a main function to handle user input and display the result.

Now, let's create the necessary files and implement the code.

person.py
