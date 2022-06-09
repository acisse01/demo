#    Copyright 2016 SAS Project Authors. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
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
    print ""
    print ""
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "----- HELP :"
    print "----- python test_RED.py <Type of test> <number of test>"
    print "       or"
    print "----- python test_RED.py <Type of test>"
    print ""
    print "----- Example: python test_RED.py REG 000 / python test_RED.py REG "
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print ""


  else :    
    if (len(sys.argv) == 2):
      filename = 'RED_FT_S_' + sys.argv[1] + '_*' + '.py'
    else:
      filename = 'RED_FT_S_' + sys.argv[1] + '_' + str(sys.argv[2]) + '.py'
    #end_if
      
    print filename

    tests = unittest.TestLoader().discover('testcases', filename)
    unittest.TextTestRunner(verbosity=0).run(tests)

  #end_if
  
