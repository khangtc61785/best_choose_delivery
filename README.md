# best_chosoe_delivery
## Description
Which is the best warehouse to delivery product to customer?
A product is stored at many warehouses. Each warehouse has an address. The quantity of
product of each warehouse is different. An order contains many order line. Each order line
has a product with quantity. An order also has the address information of customer.
When customer places an order, system has to choose a set of warehouse to delivery all
product. The warehouses are chosen by the some conditions that are prioritized by:
* The first: the warehouse has address at the same city with customer.
* The second: the warehouse has all product of order
* The third: the warehouse has the largest quantity of a product. Exp: iPhone is stored in
two warehouses: A, B. There’s 10 iPhone at warehouse A, and 20 at warehouse B. B is the
better.
Figure out the solution to choose the best warehouses to fulfill an order.
Input:
* A set of warehouses, each warehouse has a list of product with quantity.
* An order with the quantity of product in each order line and an address of customer

Example: A customer is at Hanoi place an order that has two line items:
* 2 books
* 3 pens

Case 1: there are four warehouses:
* Warehouse A, at Hanoi: 1 book
* Warehouse B, at Hanoi: 3 books, 3 pens
* Warehouse C, at Hanoi: 10 books, 7 pens
* Warehouse D, at Hochiminh: 30 books, 70 pens

    => Solution: C is the best.

Case 2: there are three warehouses:
* Warehouse A, at Hanoi: 1 book
* Warehouse B, at Hochiminh: 10 books
* Warehouse C, at Hochiminh, 5 pends

    => Solution: A - 1 book, B - 1 book, C - 3 pens

## Locations
Locations file is a place to prioritize locations close to order_location.

Note: order_location must exist inside Locations json file

Example: A customer is at vungtau place
### Input:
```code
    [
        "hochiminh",
        "vungtau",
        "danang",
        "hanoi"
    ]
```

### Output:
```code
    [
        "vungtau",
        "hochiminh",
        "danang",
        "hanoi"
    ]
```


## Requirement

This module requires the following:

* python3.7
* locations.json
* Input: order.json, warehouses.json

## Usage

* To run test case:

```bash
    python solution.py <order.json> <warehouses.json>
```

* To run test case:

```bash
    python run_test.py
```
