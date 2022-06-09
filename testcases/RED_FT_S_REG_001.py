# registration

from datetime import datetime
import json
import os
import unittest
#from typing_extensions import Self
#from typing_extensions import Self
#import sas
#import sas_testcase
#from util import winnforum_testcase, generateCpiRsaKeys, \
#     convertRequestToRequestWithCpiSignature, makePpaAndPalRecordsConsistent


class RegistrationTestcase(unittest.TestCase):
  def test_RED_FT_S_REG_001(self):

    print(" ")
    print("---- BEGIN RED_FT_S_REG_001 ----")
    # Load Devices
    cbsd_a = json.load(
        open(os.path.join('testcases', 'testdata', 'device_a.json')))
    cbsd_b = json.load(
        open(os.path.join('testcases', 'testdata', 'device_b.json')))
    cbsd_c = json.load(
        open(os.path.join('testcases', 'testdata', 'device_c.json')))
    cbsd_d = json.load(
        open(os.path.join('testcases', 'testdata', 'device_d.json')))
    cbsd_list = [cbsd_a,cbsd_b,cbsd_c,cbsd_d]
    # Inject FCC ID and User ID
    for cbsd in cbsd_list:
      print (cbsd)
      self.assertTrue('cbsdSerialNumber' in cbsd)
      self.assertTrue('longitude' in cbsd['installationParam'])
      self.assertTrue('latitude' in cbsd['installationParam'])
      self.assertEqual(cbsd['airInterface']['radioTechnology'], 'E_UTRA')
    print("---- END RED_FT_S_REG_001 SUCCESSFULL ----")
##
##







	
