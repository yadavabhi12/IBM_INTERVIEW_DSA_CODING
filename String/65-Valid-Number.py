""""
===============================================================================
LeetCode 65 - Valid Number
===============================================================================

PROBLEM
-------
Given a string s, return True if s is a valid number.

Examples of VALID numbers:

"2"
"0089"
"-0.1"
"+3.14"
"4."
"-.9"
"2e10"
"-90E3"
"3e+7"
"+6e-1"
"53.5e93"
"-123.456e789"


Examples of INVALID numbers: 2

"abc"
"1a"
"1e"
"e3"
"99e2.5"
"--6"
"-+3"
"95a54e53"


===============================================================================
WHAT IS A VALID NUMBER?
===============================================================================

A number can have:

    optional sign
          +
          -

    digits

    optional decimal point

    optional exponent


General structure:

        [sign] [number] [exponent]


For example:

        -12.34e+5

        ↓
       sign
        ↓
      12.34
        ↓
       e+5
        ↓
     exponent


===============================================================================
IMPORTANT RULES
===============================================================================

There are 3 main things to understand:

1. Decimal
2. Exponent
3. Sign


===============================================================================
RULE 1 - DIGITS
===============================================================================

At least ONE digit is required.


Valid:

"2"
"123"
"0"


Invalid:

""
"."
"+"


===============================================================================
RULE 2 - DECIMAL POINT
===============================================================================

A decimal point can appear only ONCE.


Valid:

"2.5"
"2."
".5"


Invalid:

"2.5.6"


IMPORTANT:

A decimal point does NOT require digits on both sides.


Therefore:

"4."

is valid.


And:

".9"

is also valid.


But:

"."

is invalid because there is no digit.


===============================================================================
RULE 3 - SIGN
===============================================================================

'+' or '-' can appear:

    at the beginning

OR

    immediately after e/E


Valid:

"+3"
"-3"
"2e+10"
"2e-10"


Invalid:

"1+2"
"2e++3"
"2e--3"


===============================================================================
RULE 4 - EXPONENT
===============================================================================

Exponent can be:

    e
    E


Examples:

"2e10"
"2E10"


After e/E:

    sign is optional

BUT

    at least ONE digit is mandatory.


Valid:

"2e10"
"2e+10"
"2e-10"


Invalid:

"2e"
"2e+"
"2e-"


===============================================================================
VERY IMPORTANT
===============================================================================

Exponent CANNOT contain a decimal.


Valid:

"2.5e10"


Invalid:

"2e2.5"


So:

Base:

    decimal allowed


Exponent:

    decimal NOT allowed


===============================================================================
EXAMPLES
===============================================================================

"2"

VALID


"0089"

VALID


"-0.1"

VALID


"+3.14"

VALID


"4."

VALID


"-.9"

VALID


"2e10"

VALID


"-90E3"

VALID


"3e+7"

VALID


"+6e-1"

VALID


"53.5e93"

VALID


"-123.456e789"

VALID


--------------------------------------------------

"abc"

INVALID


"1a"

INVALID


"1e"

INVALID


"e3"

INVALID


"99e2.5"

INVALID


"--6"

INVALID


"-+3"

INVALID


"95a54e53"

INVALID


===============================================================================
BEST INTUITION
===============================================================================

Think of the string as TWO PARTS:

            BASE
              |
              ↓
       12.34
              |
              e
              |
              ↓
          EXPONENT
             5


Example:

"12.34e-5"


        BASE             EXPONENT

        12.34       e       -5
          ↑                 ↑
      decimal allowed    decimal NOT allowed


Therefore we can parse:

    BEFORE e/E
        ↓
      base

    AFTER e/E
        ↓
      exponent


===============================================================================
APPROACH 1 - ONE PASS STATE TRACKING ⭐⭐⭐
===============================================================================

Maintain:

seen_digit
    ↓
Have we seen a digit?


seen_dot
    ↓
Have we seen '.'?


seen_exp
    ↓
Have we seen e/E?


digit_after_exp
    ↓
If exponent exists, did we see a digit after it?


===============================================================================
ALGORITHM
===============================================================================

For every character:


STEP 1
------

If digit:

    seen_digit = True

If we are after exponent:

    digit_after_exp = True


--------------------------------------------------

STEP 2
------

If '.':

    It is valid only if:

        decimal not seen yet
        AND
        exponent not seen yet


--------------------------------------------------

STEP 3
------

If 'e' or 'E':

    It is valid only if:

        exponent not seen yet
        AND
        digit already exists


Then:

    seen_exp = True
    digit_after_exp = False


--------------------------------------------------

STEP 4
------

If '+' or '-':

    It is valid only:

        at beginning

OR:

        immediately after e/E


--------------------------------------------------

STEP 5
------

Anything else:

    INVALID


--------------------------------------------------

At the end:

Need:

    seen_digit == True

AND

if exponent exists:

    digit_after_exp == True


===============================================================================
CODE
===============================================================================
"""

class Solution:

    def isNumber(self, s: str) -> bool:

        seen_digit = False
        seen_dot = False
        seen_exp = False

        digit_after_exp = True

        for i, ch in enumerate(s):

            # ----------------------------------------------------------
            # DIGIT
            # ----------------------------------------------------------

            if ch.isdigit():

                seen_digit = True

                if seen_exp:
                    digit_after_exp = True


            # ----------------------------------------------------------
            # DECIMAL POINT
            # ----------------------------------------------------------

            elif ch == '.':

                # Decimal cannot appear:
                # 1. more than once
                # 2. after exponent

                if seen_dot or seen_exp:
                    return False

                seen_dot = True


            # ----------------------------------------------------------
            # EXPONENT
            # ----------------------------------------------------------

            elif ch == 'e' or ch == 'E':

                # e/E can appear only once
                # and must come after at least one digit

                if seen_exp or not seen_digit:
                    return False

                seen_exp = True

                # Exponent must eventually contain a digit

                digit_after_exp = False


            # ----------------------------------------------------------
            # SIGN
            # ----------------------------------------------------------

            elif ch == '+' or ch == '-':

                # Valid only at beginning
                # OR immediately after e/E

                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False


            # ----------------------------------------------------------
            # UNKNOWN CHARACTER
            # ----------------------------------------------------------

            else:

                return False


        # At least one digit must exist.
        # If exponent exists, it must contain a digit.

        return seen_digit and digit_after_exp


"""
===============================================================================
DRY RUN 1
===============================================================================

s = "2e10"


Initial:

seen_digit = False
seen_dot = False
seen_exp = False
digit_after_exp = True


--------------------------------------------------

ch = '2'


digit


seen_digit = True


--------------------------------------------------

ch = 'e'


valid because:

seen_digit = True
seen_exp = False


seen_exp = True

digit_after_exp = False


--------------------------------------------------

ch = '1'


digit


digit_after_exp = True


--------------------------------------------------

ch = '0'


digit


Final:

seen_digit = True
digit_after_exp = True


return:

True


===============================================================================
DRY RUN 2
===============================================================================

s = "2e"


--------------------------------------------------

'2'

seen_digit = True


--------------------------------------------------

'e'

seen_exp = True

digit_after_exp = False


END


digit_after_exp = False


Therefore:

False


Correct.


===============================================================================
DRY RUN 3
===============================================================================

s = "2e+"


'2'

digit


'e'

exponent starts


'+'


valid because immediately after e


But:

digit_after_exp = False


END


False


Correct.


===============================================================================
DRY RUN 4
===============================================================================

s = ".9"


'.'


Valid because:

no dot before
no exponent


seen_dot = True


'9'


seen_digit = True


END:

seen_digit = True


True


===============================================================================
DRY RUN 5
===============================================================================

s = "."


'.'


Valid temporarily.


But:

seen_digit = False


END:


False


Correct.


===============================================================================
DRY RUN 6
===============================================================================

s = "99e2.5"


99

digits → valid


e

exponent starts


2

digit


'.'

But:

seen_exp = True


Decimal after exponent is NOT allowed.


Therefore:

False


===============================================================================
DRY RUN 7
===============================================================================

s = "-.9"


'-'


i = 0

Valid sign.


'.'


Valid decimal.


'9'


digit found.


Final:

True


===============================================================================
DRY RUN 8
===============================================================================

s = "6e-1"


'6'

digit


'e'

exponent


'-'

immediately after e → valid


'1'

digit after exponent


True


===============================================================================
WHY `digit_after_exp` IS NEEDED
===============================================================================

Consider:

"1e"


At 'e':

We set:

digit_after_exp = False


If no digit comes later:

return False


Consider:

"1e+"


Same.


At '+':

still:

digit_after_exp = False


Therefore:

False


But:

"1e+5"


After 5:

digit_after_exp = True


Therefore:

True


===============================================================================
IMPORTANT EDGE CASES
===============================================================================

CASE 1:

"4."


True


--------------------------------------------------

CASE 2:

".4"


True


--------------------------------------------------

CASE 3:

"."

False


--------------------------------------------------

CASE 4:

"2e0"


True


--------------------------------------------------

CASE 5:

"2e"


False


--------------------------------------------------

CASE 6:

"2e-"


False


--------------------------------------------------

CASE 7:

"2e+3"


True


--------------------------------------------------

CASE 8:

"2e3.5"


False


--------------------------------------------------

CASE 9:

"1.2.3"


False


--------------------------------------------------

CASE 10:

"--1"


False


--------------------------------------------------

CASE 11:

"+-1"


False


--------------------------------------------------

CASE 12:

"e10"


False


===============================================================================
APPROACH 2 - SPLIT AT e/E
===============================================================================

Another way to understand the problem:

Separate:

BASE

and

EXPONENT


Example:

"12.34e-56"


becomes:

base = "12.34"

exponent = "-56"


Then validate both separately.


Rules:

BASE:

    optional sign
    digits
    optional decimal


EXPONENT:

    optional sign
    digits only


This approach can be easier to understand,
but requires careful handling of edge cases.


===============================================================================
APPROACH 2 CODE
===============================================================================
"""

class Solution:

    def isNumber(self, s: str) -> bool:

        # ----------------------------------------------------------
        # Find exponent
        # ----------------------------------------------------------

        e_count = s.count('e') + s.count('E')

        if e_count > 1:
            return False


        if 'e' in s:
            base, exp = s.split('e')
        elif 'E' in s:
            base, exp = s.split('E')
        else:
            base = s
            exp = None


        # ----------------------------------------------------------
        # Validate base
        # ----------------------------------------------------------

        def valid_base(x):

            if not x:
                return False

            if x[0] in '+-':
                x = x[1:]

            if not x:
                return False

            dot_count = x.count('.')

            if dot_count > 1:
                return False

            x = x.replace('.', '')

            return x.isdigit()


        # ----------------------------------------------------------
        # Validate exponent
        # ----------------------------------------------------------

        def valid_exp(x):

            if not x:
                return False

            if x[0] in '+-':
                x = x[1:]

            if not x:
                return False

            return x.isdigit()


        if not valid_base(base):
            return False


        if exp is not None:

            if not valid_exp(exp):
                return False


        return True


"""
===============================================================================
APPROACH COMPARISON
===============================================================================

APPROACH 1:

One-pass state tracking


Advantages:

    O(n)
    O(1) extra space
    Very interview-friendly
    No string splitting required


APPROACH 2:

Split base and exponent


Advantages:

    Easier to understand conceptually
    Separates base/exponent validation


Disadvantages:

    More string operations
    More edge-case handling


For interview:

    APPROACH 1 is preferred.


===============================================================================
COMMON MISTAKES
===============================================================================

❌ Mistake 1:

Accepting:

"2e"


Exponent needs a digit.


--------------------------------------------------

❌ Mistake 2:

Accepting:

"2e2.5"


Exponent cannot contain decimal.


--------------------------------------------------

❌ Mistake 3:

Accepting:

"1.2.3"


Only one decimal is allowed.


--------------------------------------------------

❌ Mistake 4:

Accepting:

"1+2"


Sign is not allowed in the middle.


--------------------------------------------------

❌ Mistake 5:

Rejecting:

"4."


This is actually valid.


--------------------------------------------------

❌ Mistake 6:

Rejecting:

".5"


This is also valid.


--------------------------------------------------

❌ Mistake 7:

Accepting:

"e3"


Exponent requires a number before it.


===============================================================================
COMPLEXITY
===============================================================================

We scan the string once.


Time:

O(n)


Extra Space:

O(1)


===============================================================================
INTERVIEW EXPLANATION
===============================================================================

"I'll scan the string once while maintaining three flags:
whether I've seen a digit, a decimal point, and an exponent.

A decimal point is allowed only before the exponent and only once.
An exponent is allowed only once and only after at least one digit.
A sign is allowed only at the beginning or immediately after e/E.

Finally, I make sure that at least one digit exists and, if an
exponent exists, there is at least one digit after it.

This gives O(n) time and O(1) extra space."


===============================================================================
QUICK REVISION
===============================================================================

VALID:

    [+/-] digits [. digits] [e/E [+/-] digits]

But decimal can also be:

    .5

or:

    5.


Think:

        BASE
         |
    decimal allowed
         |
         e/E
         |
      EXPONENT
         |
    decimal NOT allowed


===============================================================================
MEMORY TRICK
===============================================================================

Remember:

    DIGIT
      ↓
    DOT only once + before E
      ↓
    E only once + needs digit before
      ↓
    SIGN only at start / after E
      ↓
    E needs digit after


===============================================================================
FINAL CODE ⭐
===============================================================================
"""

class Solution:

    def isNumber(self, s: str) -> bool:

        seen_digit = False
        seen_dot = False
        seen_exp = False
        digit_after_exp = True

        for i, ch in enumerate(s):

            if ch.isdigit():

                seen_digit = True

                if seen_exp:
                    digit_after_exp = True

            elif ch == '.':

                if seen_dot or seen_exp:
                    return False

                seen_dot = True

            elif ch in 'eE':

                if seen_exp or not seen_digit:
                    return False

                seen_exp = True
                digit_after_exp = False

            elif ch in '+-':

                if i != 0 and s[i - 1] not in 'eE':
                    return False

            else:

                return False

        return seen_digit and digit_after_exp

"""
===============================================================================
ONE-LINE FORMULA
===============================================================================

        NUMBER

          ↓

    optional sign
          +
    digits / decimal
          +
    optional e/E
          +
    optional sign
          +
    digits


Complexity:

O(n) time
O(1) space

===============================================================================
"""