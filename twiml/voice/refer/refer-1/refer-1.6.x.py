from twilio.twiml.voice_response import Refer, VoiceResponse, Sip

response = VoiceResponse()
refer = Refer()
refer.sip('sip:alice@example.com')
response.append(refer)

print(response)
