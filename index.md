# Python More Exceptions

### [HackerRank](www.hackerank.com)

> Write a Calculator class with a single method: int power(int,int).
> The power method takes two integers, n and p, as parameters and returns the integer result of n^p.
> If either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.

## Code

#### Create Calculator class with a single method: int power(n, p)

```python
class Calculator:

  def power(self, n, p):
    pass
```

#### If either n or p is < 0 then raise exception with message

```python
...
if n < 0 or p < 0:
  raise Exception("n and p should be non-negative")
```

#### Else return n^p

```python
...
return n**p
```

#### Final Code with documentation

```python
#Write your code here


class Calculator:
  """This is a class for a single mathematical method, n to the power of p"""

  def power(self, n, p):
    """Calculates the power.

    Parameters
    ----------
      n : int, float : Must be non-negative.
      p : int, float : Must be non-negative.

    Returns
    -------
      n**p : int, float

    Notes
    ----
      * Throws an exception if a non-negative number is given.
    """

    if n < 0 or p < 0:
      raise Exception("n and p should be non-negative")
    return n**p


myCalculator=Calculator()
```

## Conclusion

Another fun warm up.
