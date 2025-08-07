def convert_temperature(value, unit):
    unit = unit.lower()
    if unit == 'celsius':
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin
    elif unit == 'fahrenheit':
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, kelvin
    elif unit == 'kelvin':
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit
    else:
        return None

temp = float(input("Enter temperature value: "))
unit = input("Enter the unit (Celsius/Fahrenheit/Kelvin): ")

result = convert_temperature(temp, unit)

if result:
    print("Converted values:")
    if unit.lower() == 'celsius':
        print(f"Fahrenheit: {result[0]:.2f}°F\nKelvin: {result[1]:.2f}K")
    elif unit.lower() == 'fahrenheit':
        print(f"Celsius: {result[0]:.2f}°C\nKelvin: {result[1]:.2f}K")
    else:
        print(f"Celsius: {result[0]:.2f}°C\nFahrenheit: {result[1]:.2f}°F")
else:
    print("Invalid unit entered.")