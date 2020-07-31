import json


def read_json_file(file_path):
    output = None
    with open(file_path) as json_file:
        output = json.load(json_file)
    return output


def get_locations():
    locations = []
    with open('locations.json') as json_file:
        locations = json.load(json_file)
    return locations


def sort_close_customer(order_location, locations):
    """[summary]

    Args:
        order_location ([type]): [description]
        locations ([type]): [description]

    Returns:
        [type]: [description]
    """
    len_locations = len(locations)
    # Fisrt location is order location
    output = [order_location]
    order_location_index = locations.index(order_location)
    before = order_location_index - 1
    after = order_location_index + 1
    while before > -1 or after < len_locations:
        if before > -1:
            output.append(locations[before])
            before -= 1
        if after < len_locations:
            output.append(locations[after])
            after += 1
    return output


def get_best_choice(current, new):
    best = {}
    if len(new) > len(current):
        return new
    for product in new:
        current_detail = current.get(product, "")
        new_detail = new.get(product, "")
        if int(new_detail.split("_")[0]) > int(current_detail.split("_")[0]):
            best.update({product: "{}_{}".format(
                new_detail.split("_")[0], new_detail.split("_")[1])})
        else:
            best.update({product: "{}_{}".format(
                current_detail.split("_")[0], current_detail.split("_")[1])})
    return best


def find_order_wareshouse(order_products, order_close_locations, warehouses):
    expect_all_quantity = sum(quantity for quantity in order_products.values())
    total_all_product = 0
    result = {}
    # Create default result
    for product, quantity in order_products.items():
        result.update({product: {
            "total_quantity": 0,
            "warehouses": []
        }})

    for location in order_close_locations:
        warehouses_at_location = warehouses.get(location, [])
        best_choice_at_location = {}
        # If not any warehouse in this location
        # Don't do anything
        # Find best choice at location
        for warehouse in warehouses_at_location:
            warehouse_name = warehouse.get("name", "NoName")
            warehouse_products = warehouse.get("product", {})
            tmp = {}
            for product, quantity in order_products.items():
                wh_product_quan = warehouse_products.get(product, 0)
                tmp.update({"{}_{}".format(
                    quantity, product): "{}_{}".format(
                        wh_product_quan, warehouse_name)})
            best_choice_at_location = get_best_choice(
                best_choice_at_location, tmp)
        # print(best_choice_at_location)

        for key, value in best_choice_at_location.items():
            total_quantity = result[key.split("_")[1]]["total_quantity"]
            order_quantity = int(key.split("_")[0])
            warehouses_quantity = int(value.split("_")[0])
            if total_quantity == order_quantity:
                continue
            if warehouses_quantity >= order_quantity:
                if total_quantity:
                    quantity_actual = order_quantity - total_quantity
                else:
                    quantity_actual = order_quantity
            else:
                quantity_actual = warehouses_quantity - total_quantity
            if not quantity_actual:
                continue
            result[key.split("_")[1]]["warehouses"].append("{}_{}".format(
                quantity_actual, value.split("_")[1]))
            result[key.split("_")[1]]["total_quantity"] = sum(
                int(item.split("_")[0]) for item in result[key.split("_")[1]]["warehouses"])

        total_all_product = sum(value['total_quantity']
                                for value in result.values())
        # If product that we need enough
        # Don't need to find in another location
        if total_all_product == expect_all_quantity:
            break
    return result


def main(order, warehouses):
    locations = get_locations()
    # Check If not order's location in locations
    # Raise and not do anything
    order_location = order.get("location", None)
    order_product = order.get("product", None)
    if not order_location in locations:
        print("Location \"{}\" is not exist".format(order_location))
    elif not order_product:
        print("Product is not exist")
    else:
        print("Order: {}".format(order))
        order_close_locations = sort_close_customer(order_location, locations)
        print("Order of locations close to customer: {}".format(
            order_close_locations))

        print("Result: {}".format(find_order_wareshouse(order_product,
                                    order_close_locations, warehouses)))


if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser(version="%prog ",
                          usage='%prog ORDER.json WAREHOUSES.json')
    _, args = parser.parse_args()
    order_file = args[0]
    warehouses_file = args[1]
    order = read_json_file(order_file)
    warehouses = read_json_file(warehouses_file)

    main(order, warehouses)
