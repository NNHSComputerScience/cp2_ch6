# Functions t0 convert between Celsius and Fahrenheit.

# DOCSTRING: A special way to document a function;
#    It must be triple quoted (single or double), and on the first line after the function header. 
#    Can provide useful information when attempting to use the function.

def celsius_to_fahrenheit(celsius):
    """converts a temperature from celsius to fahrenheit"""
    fahr = celsius * 1.8 + 32
    return fahr

# This function takes a temperature
# in Fahrenheit and converts it to
# Celsius.
def fahrenheit_to_celsius(fahrenheit):
    """converts a temperature from fahrenheit to celsius"""
    celc = (fahrenheit - 32) / 1.8
    return celc

print("0C In F: " + str(celsius_to_fahrenheit(0)))
print("100C In F: " + str(celsius_to_fahrenheit(100)))
print("40F In C: " + str(fahrenheit_to_celsius(40)))
print("80F In C: " + str(fahrenheit_to_celsius(80)))
