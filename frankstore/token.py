# Import our gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
 
# Specify your authentication credentials
username    = "Francis Sakwa"
apikey      = "850b7b75e8f11c38d69446d24945babc26adc71b40fc15f2beb0d0b3f7a0628e"
 
# Specify your Africa's Talking phone number
callFrom    = "+254701112358"
 
# Specify the numbers you want to call
callTo      = "+254710755176,+254717206181"
 
# Create a new instance of our gateway class
gateway     = AfricasTalkingGateway(username, apikey)
 
try:
    # Make the call
    results = gateway.call(callFrom, callTo)
 
    for result in results:
        # Status "Queued" means the call was successfully placed
        print "Status : %s; phoneNumber : %s " % (result['status'], result['phoneNumber'])
 
    # Our API will now contact your callback URL,
    # once the recipient answers the call!
 
except AfricasTalkingGatewayException, e:
    print 'Encountered an error while making the call: %s' % str(e)
                      