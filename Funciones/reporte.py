def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

generate_report(80, 70, 75)

print(generate_report)

'''Fuel Report:
    Main tank: 80
    External tank: 70
    Hydrogen tank: 75 '''
