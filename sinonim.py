def describe_car(car_name, car_type="быстро"):
    print(car_name + " разгоняется " + car_type)

print(describe_car('volvo'))
print(describe_car(car_name='volvo'))
print(describe_car(car_name='volvo', car_type="быстро"))
print(describe_car(car_type="быстро", car_name='volvo'))

