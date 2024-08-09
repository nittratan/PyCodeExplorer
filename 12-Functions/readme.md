
## What are Functions ?

- A function is a piece of code which performs a specific task.
- It is used to reduce the repetition of the code hence reducing the size of the code, Less chances of making mistakes in the code.
- Functions make the task easy for the programmers as each programmer in a team can be given a specific task( function ) and at the end we can combine these task together to make single application.




###  Why do we need function
*example*

```python
Program without function                    with function
1.---------code-------                    1.--------code-------   
2.---------code-------                    2.--------code-------
3.---------code-------                    3.--------code-------
  statement-1                       
  statement-2                              fun()
  statement-3
7.---------code-------                    7.--------code-------
8.---------code-------                    8.--------code-------
9.---------code-------                    9.--------code-------
  statement-1
  statement-2                              fun()
  statement-3
13.---------code-------                   13.--------code-------
14.---------code-------                   14.--------code-------
15.---------code-------                   15.--------code-------
  statement-1
  statement-2                              fun()
  statement-3
19.---------code-------                   19.--------code-------
20.---------code-------                   20.--------code-------
21.---------code-------                   21.--------code-------
  statement-1
  statement-2                               fun()
  statement-3
25.---------code-------                   25.--------code-------
26.---------code-------                   26.--------code-------
27.---------code-------                   27.--------code-------

```


#### Without Functions
In the version without functions, you have the following repeated code blocks:

*statement-1*\
*statement-2*\
*statement-3*\
\
These blocks are repeated multiple times in different parts of the program. This approach has several drawbacks:


- Code Duplication: The same code is repeated multiple times, leading to unnecessary duplication. This makes the code longer, harder to read, and more prone to errors.
- Maintenance Difficulty: If you need to update statement-1, statement-2, or statement-3, you'll have to find and modify each occurrence manually, which is time-consuming and error-prone.
- Increased Complexity: With more repeated code, the overall complexity of the program increases, making it harder to understand and debug.

#### In the version with functions, the repeated code blocks are encapsulated/wrap-up in a function named fun():

```python
def fun():
    statement-1
    statement-2
    statement-3
```

Now, instead of repeating the code, you simply call the function fun() whenever you need to execute those statements. This approach offers several advantages:

- Code Reusability: By defining the repeated code in a function, you can reuse it multiple times without duplication. This leads to shorter, more concise code.
- Easier Maintenance: If you need to update the logic in statement-1, statement-2, or statement-3, you only have to do it in one place—inside the function. This reduces the risk of errors and makes the program easier to maintain.
- Improved Readability: With functions, the code becomes more organized and easier to understand. Each function can be given a meaningful name that describes its purpose, making the overall program structure clearer.
- Reduced Complexity: By removing code duplication and centralizing the logic in functions, the program becomes less complex and easier to manage.