from supervisorclusterctl import supervisorclusterctl
import unittest


class TestSupervisorClusterCTL(unittest.TestCase):
    
    def test_supervissorctl_with_host_patterns(self):       
        with self.assertRaises(SystemExit) as exception:
            supervisorclusterctl.main(["spicadev", "-v"])
            
        self.assertEqual(exception.exception.code, 0)
if __name__ == "__main__":
    unittest.main()