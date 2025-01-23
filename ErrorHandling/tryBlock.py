class CustomError(Exception):
    pass


try:
    raise CustomError("This is a custom error")

except ZeroDivisionError as e:
    print('Error:', e)

except ValueError:
    print('Error: Can\'t convert to integer')

except Exception as e:
    print('An error occurred:', e)

else:
    print('Program ran without an error')

finally:
    print('We are done with error handling')