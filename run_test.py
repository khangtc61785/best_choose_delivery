import solution

locations = solution.get_locations()

# Test cas 1
print("=========Test case 1=========")
order = solution.read_json_file('case_1/order.json')
warehouses = solution.read_json_file('case_1/warehouses.json')
solution.main(order, warehouses)

# Test cas 2
print("=========Test case 2=========")
order = solution.read_json_file('case_2/order.json')
warehouses = solution.read_json_file('case_2/warehouses.json')
solution.main(order, warehouses)

# Test cas 3
print("=========Test case 3=========")
order = solution.read_json_file('case_3/order.json')
warehouses = solution.read_json_file('case_3/warehouses.json')
solution.main(order, warehouses)

# Test cas 4
print("=========Test case 4=========")
order = solution.read_json_file('case_4/order.json')
warehouses = solution.read_json_file('case_4/warehouses.json')
solution.main(order, warehouses)

# Test cas 5
print("=========Test case 5=========")
order = solution.read_json_file('case_5/order.json')
warehouses = solution.read_json_file('case_5/warehouses.json')
solution.main(order, warehouses)

