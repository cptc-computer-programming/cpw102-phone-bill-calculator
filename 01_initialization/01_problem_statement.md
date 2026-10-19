# Problem Statement

## Assignment 4: Phone Data Bill Calculator

Build a Python program that calculates a monthly phone bill based on data usage and displays the total cost along with usage messages.

## Required behavior

Ask for monthly data usage in GB (`data_used`) and base plan cost (`base_cost`). The data limit is 10 GB and the overage rate is $2 per GB.

- If `data_used <= 10`, display a message that the user is within the limit and display the total bill (the base plan cost).
- If `data_used > 10`, display how many GB over the limit the user is. Use a nested `if`: if the overage is greater than 5 GB, display a high usage message; otherwise, display a moderate usage message. Display the total bill.

For usage above the limit, use these formulas:

```text
overage_gb = data_used - 10
overage_cost = overage_gb * 2
total = base_cost + overage_cost
```

## Learning Goals

- Accept multiple user inputs.
- Perform calculations using numeric values.
- Use decision structures to control program flow.
- Apply a nested decision in a meaningful way.

## Example terminal runs

```text
Enter data used (GB): 13
Enter base plan cost: 40
You are 3.0 GB over your limit.
Moderate extra usage.
Your total bill is: $46.0
```

```text
Enter data used (GB): 9
Enter base plan cost: 40
You are within your data limit.
Your total bill is: $40.0
```

Your prompts and layout may differ.

## Technical expectations

Write your Python program in `03_execution/data_bill.py`.

## Assumptions and limits

All input data will be numeric. You do not need to handle invalid input.
