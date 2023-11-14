from importlib import reload
import unittest

from tests.res import test_classes


# pylint: disable=W0104
class Test(unittest.TestCase):
    def setUp(self) -> None:
        reload(test_classes)

    def test_property_is_bound_to_class(self) -> None:
        t: test_classes.TestClass = test_classes.TestClass()

        self.assertEqual(test_classes.TestClass.rw_attr, "change_me")
        self.assertEqual(t.rw_attr, "change_me")

        # change class value
        test_classes.TestClass.rw_attr = "new"
        self.assertEqual(test_classes.TestClass.rw_attr, "new")
        self.assertEqual(t.rw_attr, "new")

        # delete the value
        del test_classes.TestClass.rw_attr
        with self.assertRaises(AttributeError):
            test_classes.TestClass.rw_attr
        with self.assertRaises(AttributeError):
            t.rw_attr

    def test_class_gt_instance(self) -> None:
        t1: test_classes.TestClass = test_classes.TestClass()
        t2: test_classes.TestClass = test_classes.TestClass()

        self.assertEqual(test_classes.TestClass.rw_attr, "change_me")
        self.assertEqual(t1.rw_attr, "change_me")
        self.assertEqual(t2.rw_attr, "change_me")

        # change the instance value
        t1.rw_attr = "new"
        self.assertEqual(test_classes.TestClass.rw_attr, "new")
        self.assertEqual(t1.rw_attr, "new")
        self.assertEqual(t2.rw_attr, "new")

        # change the class value
        test_classes.TestClass.rw_attr = "another_one"
        self.assertEqual(test_classes.TestClass.rw_attr, "another_one")
        self.assertEqual(t1.rw_attr, "another_one")
        self.assertEqual(t2.rw_attr, "another_one")

        # delete the instance value
        del t1.rw_attr
        with self.assertRaises(AttributeError):
            test_classes.TestClass.rw_attr
        with self.assertRaises(AttributeError):
            t1.rw_attr
        with self.assertRaises(AttributeError):
            t2.rw_attr

    def test_read_only_property(self) -> None:
        # basic test
        test_classes.TestClass.rw_attr.strip()
        test_classes.TestClass.rw_attr = "adsf"
        self.assertEqual(test_classes.TestClass.ro_attr, "read-only")

        # try changing or deleting
        with self.assertRaises(AttributeError):
            test_classes.TestClass.ro_attr = "changed"
        with self.assertRaises(AttributeError):
            del test_classes.TestClass.ro_attr

        # do the same with an instance
        t: test_classes.TestClass = test_classes.TestClass()
        with self.assertRaises(AttributeError):
            t.ro_attr = "changed"  # type: ignore
        with self.assertRaises(AttributeError):
            del t.ro_attr  # type: ignore


if __name__ == "__main__":
    unittest.main()
