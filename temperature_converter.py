# This function takes a temperature
# in Celsius and converts it to
# Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

# This function takes a temperature
# in Fahrenheit and converts it to
# Celsius.
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

print("0C In F: " + str(celsius_to_fahrenheit(0)))
print("100C In F: " + str(celsius_to_fahrenheit(100)))
print("40F In C: " + str(fahrenheit_to_celsius(40)))
print("80F In C: " + str(fahrenheit_to_celsius(80)))
