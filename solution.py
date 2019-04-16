#########################
# !!! SOLUTION CODE !!! #
#########################


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
