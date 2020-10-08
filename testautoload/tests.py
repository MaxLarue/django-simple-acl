from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from parameterized import parameterized
from simpleacls.testutils import AclTestMixin
from testautoload.models import Order, Product, Invoice, InvoiceProposition
from testautoload.groups import DRIVER, SHOP_EMPLOYEE, SALESMAN, ACCOUNTANT, MANAGER


class TestAutoImportHasSetPermissions(AclTestMixin, TestCase):

    @parameterized.expand([
        ("add_order", False),
        ("change_order", False),
        ("delete_order", False),
        ("view_order", True),
        ("add_product", False),
        ("change_product", False),
        ("delete_product", False),
        ("view_product", True),
        ("add_invoice", False),
        ("change_invoice", False),
        ("delete_invoice", False),
        ("view_invoice", False),
        ("add_invoiceproposition", False),
        ("change_invoiceproposition", False),
        ("delete_invoiceproposition", False),
        ("view_invoiceproposition", False),
    ])
    def test_driver_permissions(self, permission_name, should_have_permission):
        self.assert_permission(DRIVER, permission_name, should_have_permission)

    @parameterized.expand([
        ("add_order", False),
        ("change_order", False),
        ("delete_order", False),
        ("view_order", True),
        ("add_product", False),
        ("change_product", False),
        ("delete_product", False),
        ("view_product", True),
        ("add_invoice", False),
        ("change_invoice", False),
        ("delete_invoice", False),
        ("view_invoice", False),
        ("add_invoiceproposition", False),
        ("change_invoiceproposition", False),
        ("delete_invoiceproposition", False),
        ("view_invoiceproposition", False),
    ])
    def test_shop_employee_permissions(self, permission_name, should_have_permission):
        self.assert_permission(SHOP_EMPLOYEE, permission_name, should_have_permission)

    @parameterized.expand([
        ("add_order", False),
        ("change_order", False),
        ("delete_order", False),
        ("view_order", False),
        ("add_product", False),
        ("change_product", False),
        ("delete_product", False),
        ("view_product", True),
        ("add_invoice", False),
        ("change_invoice", False),
        ("delete_invoice", False),
        ("view_invoice", False),
        ("add_invoiceproposition", True),
        ("change_invoiceproposition", True),
        ("delete_invoiceproposition", True),
        ("view_invoiceproposition", True),
    ])
    def test_salesman_permissions(self, permission_name, should_have_permission):
        self.assert_permission(SALESMAN, permission_name, should_have_permission)

    @parameterized.expand([
        ("add_order", False),
        ("change_order", False),
        ("delete_order", False),
        ("view_order", True),
        ("add_product", False),
        ("change_product", False),
        ("delete_product", False),
        ("view_product", True),
        ("add_invoice", True),
        ("change_invoice", True),
        ("delete_invoice", True),
        ("view_invoice", True),
        ("add_invoiceproposition", False),
        ("change_invoiceproposition", False),
        ("delete_invoiceproposition", False),
        ("view_invoiceproposition", True),
    ])
    def test_accountant_permissions(self, permission_name, should_have_permission):
        self.assert_permission(ACCOUNTANT, permission_name, should_have_permission)

    @parameterized.expand([
        ("add_order", True),
        ("change_order", True),
        ("delete_order", True),
        ("view_order", True),
        ("add_product", True),
        ("change_product", True),
        ("delete_product", True),
        ("view_product", True),
        ("add_invoice", True),
        ("change_invoice", True),
        ("delete_invoice", True),
        ("view_invoice", True),
        ("add_invoiceproposition", True),
        ("change_invoiceproposition", True),
        ("delete_invoiceproposition", True),
        ("view_invoiceproposition", True),
    ])
    def test_manager_permissions(self, permission_name, should_have_permission):
        self.assert_permission(MANAGER, permission_name, should_have_permission)

    def assert_permission(self, group_name, permission_name, should_have_permission):
        if should_have_permission:
            self.assert_group_has_permission(group_name, permission_name)
        else:
            self.assert_group_has_not_permission(group_name, permission_name)

    def assert_group_has_permission(self, group_name, permission_name):
        try:
            group = Group.objects.get(name=group_name)
            group.permissions.get(codename=permission_name)
        except Permission.DoesNotExist:
            self.fail("group %s does not have permission %s" % (
                group_name,
                permission_name,
            ))

    def assert_group_has_not_permission(self, group_name, permission_name):
        try:
            group = Group.objects.get(name=group_name)
            group.permissions.get(codename=permission_name)
            self.fail("group %s does have permission %s" % (
                group_name,
                permission_name,
            ))
        except Permission.DoesNotExist:
            pass