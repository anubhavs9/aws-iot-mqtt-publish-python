# aws-iot-mqtt-publish-python
A Simple application to Publish MQTT data to AWS Cloud using AWS IoT Python SDK.
---
Download AWS IoT Python SDK 
  ```
  pip install awsiotsdk
  ```
---

Steps to configure AWS IoT Core and run the application - 
  1. Login to AWS IoT Core Console
  
  2. Create a policy-
      1. Go to Secure
      2. Choose Policies
      3. Create a new policy
      4. Give a name to policy
      5. Under Add statements
          a. For Actions enter iot:*
          b. For Resource ARN, enter *
          c. For Effect, select Allow
      6. Choose Create
      
  3. Create AWS Thing
      1. Go to Manage
      2. Choose Create
      3. Choose register a thing
      4. Select Create a single thing
      5. Give a name to your thing and select Next
      6. Choose Create Certificate
      7. Download the following : Certificate(xxx.pem.crt), Private Key(xxx.private.pem.key)
      8. Download RootCA file and save it as root.pem
      9. Choose Activate
      10. Select Attach a policy and select previously created policy
      11. Choose Register Thing
      
  4. Get Endpoint URL
      1. Select Settings and go to Custom endpoint
      2. Copy the endpoint url ansd save it
      
  5. Copy the downloaded certificate, private key and rootCA files to /certificates directory
  
  6. Open config.json and update the following -
      1. ENDPONT : Add the custom endpoint url here
      2. CLIENTID : Enter the client id. For ex. TestClient1
      3. PATH_TO_CERT : Add path of certificate(certificates/xxx.pem.crt)
      4. PATH_TO_KEY : Add path of private key(certificates/xxx.private.pem.crt)
      5. PATH_TO_ROOT : Add path of certificate(certificates/root.pem)
      6. TOPIC : Add the topic. For ex. test/testing
      
  7. Run the application
      ```
      python3 publish.py
      ```
---      
[anubhavsharma.dev](https://anubhavsharma.dev)
---
      
