def lbstokg(weight):
    return weight*0.45359237

def fttoin(ft,inch):
    return ft*0.3048+inch*0.0254

def bmi(weight,height):
    # Body Mass Index (BMI)
    if height < 1.0 or height > 2.5 \
            or weight < 20.0 or weight > 200.0:
            return None

    return (weight)/(height**2)
#weight=float(input("Enter your weight(kg): "))
#height=float(input("Enter your height(meters): "))
weight=lbstokg(176)
height=fttoin(5,7)
print("Your Body Mass Index(BMI):",bmi(weight,height))
