from unittest import TestCase
from parameterized import parameterized
from django.test import TestCase as DjangoTestCase
from django.contrib.auth.models import Group, Permission
from simpleacls.acls import BuiltinAclFlag
from simpleacls.acls import C, R, U, D
from simpleacls.acls import create_groups, set_models_acl
from tests.models import Article, Subject


class TestBuiltinFlags(TestCase):
    def test_builtin_flags_build_permission_code_correctly(self):
        test = BuiltinAclFlag("test_%s", "this is a test")
        self.assertEqual(test.get_permission_code("testmodel"), "test_testmodel")

    def test_create(self):
        self.assertEqual(C.get_permission_code("testmodel"), "add_testmodel")

    def test_read(self):
        self.assertEqual(R.get_permission_code("testmodel"), "view_testmodel")

    def test_update(self):
        self.assertEqual(U.get_permission_code("testmodel"), "change_testmodel")

    def test_delete(self):
        self.assertEqual(D.get_permission_code("testmodel"), "delete_testmodel")


class TestCreateGroups(DjangoTestCase):

    def test_it_creates_the_groups_with_names(self):
        self.assertEqual(Group.objects.count(), 0)
        create_groups(["foo", "bar"])
        self.assertEqual(Group.objects.count(), 2)
        Group.objects.get(name="foo")
        Group.objects.get(name="bar")

    def test_it_can_be_run_multiple_times(self):
        create_groups(["foo", "bar"])
        create_groups(["foo", "bar"])
        create_groups(["foo", "bar"])
        self.assertEqual(Group.objects.count(), 2)


class TestCreateAcls(DjangoTestCase):
    def setUp(self):
        super().setUp()
        self.admin = "admin"
        self.reader = "reader"
        self.writer = "writer"
        create_groups([self.admin, self.reader, self.writer])
        self.ACLS = [
            {
                Article: {
                    self.admin: {C, R, U, D},
                    self.reader: {R},
                    self.writer: {C, R, U}
                }
            },
            {
                Subject: {
                    self.admin: {C, R, U, D},
                    self.reader: {R},
                    self.writer: {R}
                }
            },
        ]
        set_models_acl(self.ACLS)

    @parameterized.expand([
        "add_article",
        "view_article",
        "change_article",
        "delete_article",
        "add_subject",
        "view_subject",
        "change_subject",
        "delete_subject",
    ])
    def test_admin_has_all_permissions(self, permission):
        Group.objects.get(name=self.admin).permissions.get(codename=permission)

    @parameterized.expand([
        "add_article",
        "view_article",
        "change_article",
        "view_subject",
    ])
    def test_writer_has_those_permissions(self, permission):
        Group.objects.get(name=self.writer).permissions.get(codename=permission)

    @parameterized.expand([
        "delete_article",
        "add_subject",
        "change_subject",
        "delete_subject",
    ])
    def test_writer_dont_have_those_permissions(self, permission):
        with self.assertRaises(Permission.DoesNotExist):
            Group.objects.get(name=self.writer).permissions.get(codename=permission)

    @parameterized.expand([
        "view_article",
        "view_subject",
    ])
    def test_reader_has_those_permissions(self, permission):
        Group.objects.get(name=self.reader).permissions.get(codename=permission)

    @parameterized.expand([
        "add_article",
        "change_article",
        "delete_article",
        "add_subject",
        "change_subject",
        "delete_subject",
    ])
    def test_reader_dont_have_those_permissions(self, permission):
        with self.assertRaises(Permission.DoesNotExist):
            Group.objects.get(name=self.reader).permissions.get(codename=permission)