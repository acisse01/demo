# registration

from datetime import datetime
import json
import os
#import sas
#import sas_testcase
#from util import winnforum_testcase, generateCpiRsaKeys, \
#     convertRequestToRequestWithCpiSignature, makePpaAndPalRecordsConsistent


class RegistrationTestcase(sas_testcase.SasTestCase):

  def setUp(self):
    self._sas, self._sas_admin = sas.GetTestingSas()
    self._sas_admin.Reset()

  def tearDown(self):
    pass




  def test_RED_FT_S_REG_001(self):
    """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Array Single-Step registration for CBSDs :
       - Cat A (height < 6 m,
       - Cat A Indoor (height > 6 m),
       - Cat A Outdoor (height > 6 m),
       - Cat B
    The response should be SUCCESS.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    print(" ")
    print("---- BEGIN RED_FT_S_REG_001 ----")

    # Load Devices
    cbsd_A_All = json.load(
        open(os.path.join('testcases', 'testdata', 'cbsd_A_All.json')))
    cbsd_AI_more_6m_All = json.load(
        open(os.path.join('testcases', 'testdata', 'cbsd_AI_more_6m_All.json')))
    cbsd_AO_more_6m_All = json.load(
        open(os.path.join('testcases', 'testdata', 'cbsd_AO_more_6m_All.json')))
    cbsd_B_All = json.load(
        open(os.path.join('testcases', 'testdata', 'cbsd_B_All.json')))

    # Inject FCC ID and User ID
    for device in [cbsd_A_All, cbsd_AI_more_6m_All, cbsd_AO_more_6m_All, cbsd_B_All]:
      self._sas_admin.InjectFccId({'fccId': device['fccId']})
      self._sas_admin.InjectUserId({'userId': device['userId']})


    # (Generate CPI RSA keys for Cat A Outdoor (height > 6 m))
    cpi_id = 'cpi_id_AO'
    cpi_name = 'cpi_name_AO'
    cpi_private_key, cpi_public_key = generateCpiRsaKeys()

    #Inject CPI Data to simulate CPI Database
    self._sas_admin.InjectCpiUser({
        'cpiId': cpi_id,
        'cpiName': cpi_name,
        'cpiPublicKey': cpi_public_key
    })
    
    # Convert cbsd_AO_more_6m_All's registration request to embed cpiSignatureData
    convertRequestToRequestWithCpiSignature(cpi_private_key, cpi_id,
                                            cpi_name, cbsd_AO_more_6m_All)
    # (Generate CPI RSA keys for Cat B)
    cpi_id = 'cpi_id_B'
    cpi_name = 'cpi_name_B'
    cpi_private_key, cpi_public_key = generateCpiRsaKeys()

    #Inject CPI Data to simulate CPI Database
    self._sas_admin.InjectCpiUser({
        'cpiId': cpi_id,
        'cpiName': cpi_name,
        'cpiPublicKey': cpi_public_key
    })
    # Convert cbsd_B_All's registration request to embed cpiSignatureData
    convertRequestToRequestWithCpiSignature(cpi_private_key, cpi_id,
                                            cpi_name, cbsd_B_All)

    print(" ")
    print(">>>>>> Registration Cat A (height < 6 m), Cat A Indoor (height > 6 m),  Cat A Outdoor (height > 6 m), Cat B --> Waiting for SUCCESS")

    # Register the devices
    devices = [cbsd_A_All, cbsd_AI_more_6m_All, cbsd_AO_more_6m_All, cbsd_B_All]
    request = {'registrationRequest': devices}
    print devices
            
    response = self._sas.Registration(request)['registrationResponse']
    print(response)
    
    # Check registration response
    for x in range(0, 3):
      self.assertEqual(response[x]['response']['responseCode'], 0)
      self.assertTrue('cbsdId' in response[x])

    print("---- END RED_FT_S_REG_001 SUCCESSFULL ----")
##
##







	
