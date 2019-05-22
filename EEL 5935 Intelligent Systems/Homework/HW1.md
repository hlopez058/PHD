# Intelligent Systems : Homework 1


## 1. Considering the sigmoid function

```
1/(1 + e^(-a x))
```

### (a) What are the upper and lower limit of the function for constant 'a', and the value of f(x) at x=0 ?

If alpha is constant then the sigmoid function is only constrained as it reaches -/+ infinity . By looking at the limit of x as it reaches negative infinity we see the value of the function go to 0.
```
lim_(x->-∞) 1/(1 + e^(-ax)) = 0
```
As x goes to positive infinity the value of the sigmoid function becomes 1.
```
lim_(x->∞) 1/(1 + e^(-ax)) = 1
```
As we inspect the when the value of x=0 the exponential product becomes 0 and forces e^0 , which is equal to 1. the denominator becomes 2 and eventually collapses the sigmoid function to equal exactly 0.5 when x=0.

### (b) Can you show that df/dx is given by the following ?
```
df/dx = a * f(x)[1-f(x)]
```

To prove the statement we start by taking the derivative of the sigmoid function.
```
d/(dx)(1/(1 + e^(-a x)))
```
We can rewrite the sigmoid function by using the chain rule. The chain rule can help by first assigning a variable 'u', to the denominator.
```
u = (1 + e^(-a x))
```
After we have defined 'u' we can state that with the chain rule the following would be true :
```
d/(dx)[1/(1 + e^(-a x))]= d/(du)[1/u] * du/dx  
```
So lets determine the derivative of (1/u) with respect to u and utilize it to substitute the right hand side of the equation above.
```
d/(du)[1/u] = -1/u^2
```
The substituted representation of the sigmoid function becomes :
```
d/(dx)[1 + e^(-ax)] / [1 + e^(-2ax)]
```
We can now find the derivative of the numerator with respect to x.
```
d/(dx)[1 + e^(-ax)] = -a*e^(-ax)
```
Equivellantly we can determine hte derivative of the denominator :
```
d/(dx)[1 + e^(-2ax)] = -2a*e^(-2ax)
```
And finally we can put it all together and get the following representation for the derivative of the sigmoid function :
```
-a*e^(-ax)/(-2a*e^(-ax)) = (a/2) * [(e^(-ax))/(e^(-2ax))]
```
```
(a/2) * [(e^(-ax))/(e^(-2ax))] ==> (a/2) * [(e^(-ax)) * (e^(-2ax))^-1]

```
....

## (c) How would you modify f(x) such that its value at x=0 is equal  (i) 0.15; (ii)0.8

We can rewrite the sigmoid function with a term 'b' that modifies the denominator to adjust its y value at x=0

```
y = 1/(1 + e^(-a * x +  a * b))
```

To attain the values in consideration we can solve for 'b' by plugging in the value for 'y'

```

```


