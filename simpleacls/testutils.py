from simpleacls.acls import initialize


class AclTestMixin(object):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        initialize()
