import converter
from util import findMax
import ECom.shipping

ECom.shipping.cal_shipping()
x=converter.lbs_to_kg(int(input('What is your weight: ')))
print(f'your weight in kg is: {x}')

number=[1,51,22,66,20]
max=findMax(number)
print(f'Highest No of list is: {max}')