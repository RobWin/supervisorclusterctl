from supervisorclusterctl import supervisorclusterctl
import unittest

class TestSupervisorclusterctl(unittest.TestCase):
    
    def testWithHelpOption(self):       
        with self.assertRaises(SystemExit) as exception:
            supervisorclusterctl.main(["-h"])            
        self.assertEqual(exception.exception.code, 0)
        
    def testWithoutHostPatternArgument(self):       
        with self.assertRaises(SystemExit) as exception:
            supervisorclusterctl.main([])            
        self.assertEqual(exception.exception.code, 2)
        
    def testStartWithoutProcessName(self):       
        with self.assertRaises(SystemExit) as exception:
            supervisorclusterctl.main(["dev", "start"])            
        self.assertEqual(exception.exception.code, 2)
       
    def testStopWithoutProcessName(self):       
        with self.assertRaises(SystemExit) as exception:
            supervisorclusterctl.main(["dev", "stop"])            
        self.assertEqual(exception.exception.code, 2)

    def testRemoveWithoutProcessName(self):       
        with self.assertRaises(SystemExit) as exception:
            supervisorclusterctl.main(["dev", "remove"])            
        self.assertEqual(exception.exception.code, 2)