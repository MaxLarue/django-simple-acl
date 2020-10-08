from testautoload.models import Order, Product, Invoice, InvoiceProposition
from testautoload.groups import DRIVER, SHOP_EMPLOYEE, SALESMAN, ACCOUNTANT, MANAGER
from simpleacls.acls import C, R, U, D


ACLS = {
    Order: {
        DRIVER: {R},
        SHOP_EMPLOYEE: {R},
        SALESMAN: set(),
        ACCOUNTANT: {R},
        MANAGER: {C, R, U, D},
    },
    Product: {
        DRIVER: {R},
        SHOP_EMPLOYEE: {R},
        SALESMAN: {R},
        ACCOUNTANT: {R},
        MANAGER: {C, R, U, D},
    },
    Invoice: {
        DRIVER: set(),
        SHOP_EMPLOYEE: set(),
        SALESMAN: set(),
        ACCOUNTANT: {C, R, U, D},
        MANAGER: {C, R, U, D},
    },
    InvoiceProposition: {
        DRIVER: set(),
        SHOP_EMPLOYEE: set(),
        SALESMAN: {C, R, U, D},
        ACCOUNTANT: {R},
        MANAGER: {C, R, U, D},
    },
}
