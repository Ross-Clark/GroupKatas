import unittest
from task import read_file, write_ip_to_file, total_status_codes, get_404
class test(unittest.TestCase):

    def test_read(self):
        with open ('server_logs.log', 'rt') as myfile:
            contents = myfile.readlines()
        #getting file reading from function
        another_read = read_file()   
        #assert
        assert(contents == another_read)
    
    def test_write_ip_to_file(self):
        #arrange
        test_list = ['175.39.217.117']
        #act
        write_ip_to_file(test_list)
        with open('ip.log', 'r') as f:
            check_test_list = f.readlines()
        #assert
        print(check_test_list[0])
        #assert('175.39.217.117' == check_test_list)


if __name__ == '__main__':
    unittest.main()
