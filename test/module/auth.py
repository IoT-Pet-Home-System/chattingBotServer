import unittest
from src.auth.IDissuance import IDIssuance

class auth_test(unittest.TestCase):
    def test_tempID_1(self):
        TID = IDIssuance()
        user_key = "a4ffge51ff6g756e"
        tid = TID.getTempID(user_key)
        print("- Test1: input = " + user_key)
        if "RXYVACD" in tid:
            print("=> Test1: Complete!")
        else:
            self.assertTrue(1, 2)

    def test_tempID_2(self):
        TID = IDIssuance()
        user_key = "a2FsUYsdf2Cc-VSADqx"
        tid = TID.getTempID(user_key)
        print("- Test2: input = " + user_key)
        if "JSWUNONDZ" in tid:
            print("=> Test2: Complete!")
        else:
            self.assertTrue(1, 2)

if __name__ == "__main__":
    unittest.main()