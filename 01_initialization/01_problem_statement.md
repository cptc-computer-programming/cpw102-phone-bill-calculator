# Problem Statement

## Phone Data Bill Calculator

A phone customer wants to understand their monthly bill and whether their data use is getting expensive. They know how much data they used and the cost of their base plan, but they need help figuring out what they owe.

Their plan includes 10 GB of data. Usage within that allowance costs only the base plan price. Each GB beyond the allowance adds $2 to the bill. For customers who exceed the allowance, up to 5 extra GB counts as moderate extra usage; more than 5 extra GB counts as high usage.

Create a small Python program that helps this customer. The customer should be able to provide their monthly data usage and base plan cost, then see their total bill and a clear explanation of their usage. Customers within the allowance should know that they stayed within it. Customers who exceeded it should see how far over they went and whether their extra usage was moderate or high.

Choose your own prompts, message wording, variable names, and output layout. Use the planning worksheets to turn this situation into requirements and a design.

## Learning Goals

- Accept multiple user inputs.
- Perform calculations using numeric values.
- Use decision structures to control program flow.
- Apply a nested decision in a meaningful way.
- Write a function that returns a Boolean value and use its result in a decision.

## Example terminal runs

```text
Enter data used (GB): 13
Enter base plan cost: 40
You are 3.0 GB over your limit.
Moderate extra usage.
Your total bill is: $46.00
```

```text
Enter data used (GB): 9
Enter base plan cost: 40
You are within your data limit.
Your total bill is: $40.00
```

## Technical expectations

You must:

- Write your Python program in `03_execution/data_bill.py`. 
- Use a nested `if` to distinguish moderate from high extra usage for customers who exceed the allowance.
- Create and use a function that accepts data usage in GB and returns a Boolean value indicating whether it exceeds the 10 GB allowance. 
- Use that returned value to decide whether the customer is within the allowance or needs overage processing.

## Assumptions

All input data will be numeric. You do not need to handle invalid input.
