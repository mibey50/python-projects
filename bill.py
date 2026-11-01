def work_out_bil(previous, current):
    units = current - previous
    if  units <=10:
        water_cost = units * 50
    else:
        water_cost = 10 * 50 +(units-10) * 80
    service = 200
    total =  water_cost + service
    return units,water_cost,service,total

units,water_cost,service,total = work_out_bil(120,135)
print("Units used:", units)
print("Water cost:", water_cost)
print("Service charge:", service)
print("Total bill:", total)
