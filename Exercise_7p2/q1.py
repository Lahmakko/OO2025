##Example of a simple lambda function:


# Lambda function
sum_lambda = lambda x, y: x + y
##To convert it to a for-loop-based solution:


def sum_for(x, y):
    result = 0
    for num in [x, y]:
        result += num
    return result
##Or a while-loop-based solution:


def sum_while(x, y):
    result = x
    while y:
        result += 1
        y -= 1
    return result