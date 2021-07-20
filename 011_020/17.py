# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


numberwords = {"1": "one",
                "2": "two",
                "3": "three",
                "4": "four",
                "5": "five",
                "6": "six",
                "7": "seven",
                "8": "eight",
                "9": "nine",
                "10": "ten",
                "11": "eleven",
                "12": "twelve",
                "13": "thirteen",
                "14": "fourteen",
                "15": "fifteen",
                "16": "sixteen",
                "17": "seventeen",
                "18": "eighteen",
                "19": "nineteen",
                "20": "twenty",
                "30": "thirty",
                "40": "forty",
                "50": "fifty",
                "60": "sixty",
                "70": "seventy",
                "80": "eighty",
                "90": "ninety",
                "100": "hundred"
               }


def two_digit_number(i):
    if i < 21:
        numword = numberwords[str(i)]
    else:
        if i % 10 == 0:# 30, 40, 50, ...
            numword = numberwords[str(i)]
        else:
            numword = numberwords[str(i // 10 * 10)] + "-" + numberwords[str(i % 10)]
    return numword

s = ""

for i in range(1, 1001):
    if i // 100 == 0:# < 100
        numword = two_digit_number(i)
    if i >= 100 and i != 1000:# >= 100
        if i % 100 == 0:# 100, 200, 300, ...
            numword = numberwords[str(i // 100)] + " " + "hundred"
        else:
            numword = numberwords[str(i // 100)] + " " + "hundred" + " and " + two_digit_number(i % 100)
    if i == 1000:
        numword = "one thousand"
    if i == 1:
        s += numword
    else:

        s += ", " + numword

print(s)

s = s.replace(" ", "")
s = s.replace(",", "")
s = s.replace("-", "")

print(s)
print(len(s))