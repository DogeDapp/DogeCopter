import unittest
import Logger as Logger

class Test_LoggerTests(unittest.TestCase):

    def test_Logger_can_write_string_to_file(self):
       log = Logger.Logger("testfile.txt")
       log.appendStringToLogBuffer("sdfbadhsf")
       log.writeLogToFile()       

       f = open("testfile.txt", "r")
       content = f.readline()

       self.assertEquals(log.getTimestamp() + "sdfbadhsf", content)


    def test_Logger_can_write_line_to_file(self):
       log = Logger.Logger("testfile.txt")
       log.appendLineToLog("sdfbadhsf")     

       f = open("testfile.txt", "r")
       content = f.readline()

       self.assertEqual(log.getTimestamp() + "sdfbadhsf\n", content)

    def test_Logger_can_write_non_string_value_to_file_without_blowing_up(self):

       log = Logger.Logger("testfile.txt")
       log.appendStringToLogBuffer(10)
       log.writeLogToFile()       

       f = open("testfile.txt", "r")
       content = f.readline()

       self.assertEquals(log.getTimestamp() + "10", content)


if __name__ == '__main__':
    unittest.main()
