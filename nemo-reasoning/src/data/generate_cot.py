import json

# ReAct Style CoT
crypto_chat = [
    {"role": "system", "content": f"You are a helpful chatbot that will do its best to answer questions. Be concise!"},
    {"role": "user", "content": f"How do we translate 10 MB into byte?"},
    {"role": "assistant", "content": f"We know that:\n1 MB = 1 MegaByte = 1000000 byte\n So, we can calulcate that 10 MB or 10 MegaBytes as\n10 * 1000000 = 10000000\n<answer>10000000.0</answer>"},
    {"role": "user", "content": "Could you provide the value of 5 cm in inches?"},
    {"role": "assistant", "content": "We know that:\n1 centimeter = 0.3937 inch or 1 cm = 0.3937 in\nSo, we can calulcate that 5 cm to inches or 10 MegaBytes as\n5 * 0.3937 = 2.047 inches\n<answer>2.047</answer>"},
    {"role": "user", "content": "How many hours are in 2 days"},
    {"role": "assistant", "content": "We know that:\n 1 day = 24 hour\n So, we can calulcate that 2 day in hours as\n24 * 2 = 48 hours\n<answer>48.0</answer>"},
    
]
# 196ff375
"""
In Alice's Wonderland, a secret set of transformation rules is applied to equations. Below are a few examples:
[@)$: = )@<
@#\@$ = $^
$<)<[ = )@#
#^\$% = @^%
Now, determine the result for: %^\#@

A secret transformation rule was applied to numbers and operators.  The expressions have the form 2 symbol value operator 2 symbol value. I should try groupping similar operators and counting the number of output digits.

Operator ) is unknown
[@ ) $: = ) @ < 3  digits
$< ) <[ = ) @ # 3  digits

Operator \ is unknown
@# \ @$ = $ ^ 2  digits
#^ \ $% = @ ^ % 3  digits

The ) operator is always increasing to 3 digits, likely means the ) is addition.
The \ operator results in 2 and 3 digit ouputs.  Assuming the \ is subtraction.

Next I need to decode the symbols to numbers between 0-9.  The maximum value of an addition between two digit numbers will always be less than 199.  
Both addition operations result in a carry digit of 1.  This means
"""