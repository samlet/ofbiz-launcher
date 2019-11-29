# procs-ofbiz-ssl-certificate.md
⊕ [Apache OFBiz Technical Production Setup Guide - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/Apache+OFBiz+Technical+Production+Setup+Guide#ApacheOFBizTechnicalProductionSetupGuide-SSLCertificateSetup)

## SSL Certificate Setup
Choose a password to enter later when prompted. This same password will be used for the keystore password and for another question a bit later as the key password for.

1. Run: "keytool -genkey -keyalg RSA -alias ssl -keystore [keystore name]"

Go through and answer the following questions:

Enter keystore password: [password]

What is your first and last name?
[Unknown]: www.mydomain.com (example)

What is the name of your organizational unit?
[Unknown]: Undersun Testing (example)

What is the name of your organization?
[Unknown]: Undersun Testing (example)

What is the name of your City or Locality?
[Unknown]: New York (example)

What is the name of your State or Province?
[Unknown]: New York (example)

What is the two-letter country code for this unit?
[Unknown]: US (example)

Is CN=www.mydomain.com, OU=Undersun Testing, O=Undersun Testing, L=New York, ST=New York, C=US correct?
[no]: yes

Enter key password for
(RETURN if same as keystore password): [password]

2. Run: "keytool -certreq -alias ssl -keyalg RSA -file certreq.csr -keystore [keystore name]"

The following will be prompted/shown:

Enter keystore password: [password]

The CSR will be saved in the current directory: BEGIN NEW CERTIFICATE REQUEST and END NEW CERTIFICATE REQUEST

3. Submit the CSR to a signing authority (Thawte, Verisign, etc)

4. Download your certificate from the signing authority. Please remember to download the Certificate in PKCS#7 format. If you get a certificate in pem format don't convert to PKCS#7/P7B Format but der format

5. Import the Certificate into the keystore by running:

"keytool -import -alias ssl -trustcacerts -file mysignedcert.cer -keystore [keystore name]"

6. Configure the ofbiz-containers.xml file to point to your new keystore and password:

If using Tomcat (Catalina), which is the default, find the "catalina-container" -> "https-connector" -> "keystoreFile" and "keystorePass" properties and set them.
If using Jetty find the "jetty-container" -> "https-listener" -> "keystore" and "password" properties and set them.
For other Servlet containers, see the documentation for that container to find out how to set the HTTPS keystore and password settings.

