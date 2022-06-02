
import logging
import sys
import unittest

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter(
        '[%(levelname)s] %(asctime)s %(filename)s:%(lineno)d %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

if __name__ == '__main__':


  # Run the tests
  if ((len(sys.argv) < 2) or (sys.argv[1] == '?') or (sys.argv[1] == 'help')):


    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print ("----- HELP :")
    print ("----- python test_RED.py <Type of test> <number of test>")
    print ("       or")
    print ("----- python test_RED.py <Type of test>")
    print ("")
    print ("----- Example: python test_RED.py REG 000 / python test_RED.py REG ")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")


  else :    
    if (len(sys.argv) == 2):
      filename = 'RED_FT_S_' + sys.argv[1] + '_*' + '.py'
    else:
      filename = 'RED_FT_S_' + sys.argv[1] + '_' + str(sys.argv[2]) + '.py'
    #end_if
      
    print (filename)
    print (filename)
    tests = unittest.TestLoader().discover('testcases', filename)
    unittest.TextTestRunner(verbosity=0).run(tests)

  #end_if
  
