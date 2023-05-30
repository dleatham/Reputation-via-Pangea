
***Repository Name***:
  **Reputation-via-Pangea**

***Summary***:
Simplified access to Pangea’s SecIntel reputation services via python and flask.

***Repository Description***:
Reputation-via-Pangea provides simplified access to pangea.cloud’s reputation intel services. Pangea’s “security platform as a service” (SPaaS) provides professional developers with a wide range of security services, i.e compliance, data protection, SecIntel, etc. 

Pangea’s security intel services (e.g. intelligence-based reputation for domains, URLs, IPs, usernames, files, etc.) are especially interesting to security analysts and SOC teams. Reputation-via-Pangea provides resources to make it easier for these security professionals to incorporate Pangea’s SecIntel resources in their scripts, runbooks, custom tools/resources, etc.

There are three elements to Reputation-via-Pangea:

-   PangeaSecIntel - This python module is designed to simplify access to the Pangea IntelSec reputation services for: domains, URLs, IP addresses, files, and usernames. Python is popular within the InfoSec community and this module will enhance many of their existing Python projects and enable new ones as well.
    
-   PangeaSecIntel-Example-Script - This Python script provides well-documented, easy-to-follow examples of how to leverage the PangeaSecIntel module to perform reputational lookups.
    
-   pangea-flask - This python Flask app is a single-web-page utility designed for security teams to run locally. With it they can perform reputation lookups quickly and efficiently within their web browser.
    
***Getting Started***:

To use Reputation-via-Pangea, you will need to follow these steps:

-   Create a Pangea Account - Go to [https://pangea.cloud](https://pangea.cloud) and sign up for an account. Pangea offers a free account credit that is more than enough for you to begin using Reputation-via-Pangea resources.
    
-   Setup API Tokens - Use the Pangea console to access your Pangea API tokens and store them locally in OS env variables. Reputation-via-Pangea requires that API tokens be stored in specifically-named environment variables. (See below for additional instructions).
    
-   Install the Pangea Python SDK - Go to [https://pangea.cloud/docs/sdk/python/](https://pangea.cloud/docs/sdk/python/) and follow the setup instructions to install the Pangea Python SDK into your local environment.
    
-   Create a Local Clone of Reputation-via-Pangea - Create a local project directory and use git to create a local clone of Reputation-via-Pangea. Detailed instructions for creating a local clone are available here: [https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    
-   Run PangeaSecIntel-Example-Script.py - Use the python3 command to execute this script. This step will allow you to troubleshoot any issues with the API tokens or connectivity issues with the Pangea services.
    
-   Install Flask and run pangea-flask.py - Flask is a lightweight python application framework ([https://pypi.org/project/Flask/](https://pypi.org/project/Flask/)) and is installed locally with the following command:  
    $ pip3 install -U Flask  
    
    Once Flask is installed, you will need to run pangea-flask.py using the following Flask command:  
    $ flask --app pangea-flask.py run  

    Once running, the application is accessible via a web browser at [http://127.0.0.1:5000](http://120.0.0.1:5000)
    

  

***Setting Up Pangea API Token Access***

Inorder to access the Pangea intel reputation APIs with Reputation-via-Pangea you will need to understand how to copy your API access tokens from your Pangea Console and store them in local environmental variables in your terminal/shell. The API tokens you will need for Reputation-via-Pangea are available in the Pangea Console in the following locations:

-   Domain: [https://console.pangea.cloud/service/domain-intel](https://console.pangea.cloud/service/domain-intel)
    
-   URL: [https://console.pangea.cloud/service/url-intel](https://console.pangea.cloud/service/url-intel)
    
-   IP: [https://console.pangea.cloud/service/ip-intel](https://console.pangea.cloud/service/ip-intel)
    
-   File: [https://console.pangea.cloud/service/file-intel](https://console.pangea.cloud/service/file-intel)
    
-   User: [https://console.pangea.cloud/service/user-intel](https://console.pangea.cloud/service/user-intel)
    

  

The API tokens can be copied from these pages and stored into environment variables using the ‘export’ command:

$ export PANGEA_DOMAIN_TOKEN=<your_token_copied_from_pange_console>

It is necessary that the following environment variables be correctly set with the corresponding API token:

-   PANGEA_DOMAIN_TOKEN
    
-   PANGEA_URL_TOKEN
    
-   PANGEA_IP_TOKEN
    
-   PANGEA_FILE_TOKEN
    
-   PANGEA_USER_TOKEN
    

  

Additionally, you will need to set an environment variable called PANGEA_INTEL_DOMAIN with the domain that is provided on any of the console pages listed above. This domain is typically something similar to: aws.us.pangea.cloud
