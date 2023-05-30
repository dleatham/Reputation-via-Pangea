# PangeaSecIntel Example Script




###################  CHECK DOMAIN PATH AND TOKENS ##############

# Check to see if Pangea API domain path and API tokens are set
# For more information see the READ_ME file for PangeaSecIntel
import os
import sys 
PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
PANGEA_DOMAIN_TOKEN = os.getenv("PANGEA_DOMAIN_TOKEN")
PANGEA_IP_TOKEN = os.getenv("PANGEA_IP_TOKEN")
PANGEA_FILE_TOKEN = os.getenv("PANGEA_FILE_TOKEN")
PANGEA_USER_TOKEN = os.getenv("PANGEA_USER_TOKEN")
PANGEA_URL_TOKEN = os.getenv("PANGEA_URL_TOKEN")

if PANGEA_INTEL_DOMAIN == "" \
    or PANGEA_DOMAIN_TOKEN == "" \
    or PANGEA_IP_TOKEN == "" \
    or PANGEA_URL_TOKEN == "" \
    or PANGEA_FILE_TOKEN == "" \
    or PANGEA_USER_TOKEN == "" \
    or PANGEA_URL_TOKEN == "":
	print("ERROR: One or more Pangea API tokens or the domain path not set as OS env variable(s).  See READ_ME for details.")
	sys.exit()

print("\n\nStarting PangeaSecIntel Example Script:\n")


###################  DOMAIN REPUTATION EXAMPLE - Crowdstrike ##############

from PangeaSecIntel import get_domain_reputation

# set the domain to be checked and the reputation data provider
unknown_domain = "737updatesboeing.com"
domain_intel_provider = "crowdstrike"

# call the Pangea DomainIntel API to get Crowdstrike intel data
print("===============================================================================")
print("Calling Pangea DomainIntel for the reputation of the domain '737updatesboeing.com' using Crowdstrike as the intel provider.")
results = get_domain_reputation( unknown_domain, domain_intel_provider )

if "ERROR" in results:
	print(results)
else:
	print("  STATUS:\n    ", results.status, "\n", \
      " SUMMARY:\n    ", results.summary, "\n", \
      " RAW_RESULT:\n    ", results.raw_result, "\n" \
      )


###################  DOMAIN REPUTATION EXAMPLE - DomainTools ##############

# set the domain to be checked and the reputation data provider
unknown_domain = "737updatesboeing.com"
domain_intel_provider = "domaintools"

# call the Pangea DomainIntel API to get Crowdstrike intel data
print("\n===============================================================================")
print("Calling Pangea DomainIntel for the reputation of the domain '737updatesboeing.com' using DomainTools as the intel provider.")
results = get_domain_reputation( unknown_domain, domain_intel_provider )

if "ERROR" in results:
	print(results)
else:
	print("  STATUS:\n    ", results.status, "\n", \
      " SUMMARY:\n    ", results.summary, "\n", \
      " RAW_RESULT:\n    ", results.raw_result, "\n" \
      )


###################  IP REPUTATION EXAMPLE - Crowdstrike ##############

from PangeaSecIntel import get_ip_reputation

# set the domain to be checked and the reputation data provider
unknown_ip = "113.235.101.11"
ip_intel_provider = "crowdstrike"

# call the Pangea IPIntel API to get Crowdstrike intel data
print("\n===============================================================================")
print("Calling Pangea IpIntel for the reputation of the IP address '113.235.101.11' using Crowdstrike as the intel provider.")
results = get_ip_reputation( unknown_ip, ip_intel_provider)

if "ERROR" in results:
	print(results)
else:
	print("  STATUS:\n    ", results.status, "\n", \
      " SUMMARY:\n    ", results.summary, "\n", \
      " RAW_RESULT:\n    ", results.raw_result, "\n" \
      )


###################  URL REPUTATION EXAMPLE - Crowdstrike ##############

from PangeaSecIntel import get_url_reputation

# set the URL to be checked and the reputation data provider

unknown_url = "http://113.235.101.11:54384"
url_intel_provider = "crowdstrike"

# call the Pangea UrlIntel API to get Crowdstrike intel data
print("\n===============================================================================")
print("Calling Pangea UrlIntel for the reputation of the URL 'http://113.235.101.11:54384' using Crowdstrike as the intel provider.")
results = get_url_reputation( unknown_url, url_intel_provider)

if "ERROR" in results:
	print(results)
else:
	print("  STATUS:\n    ", results.status, "\n", \
      " SUMMARY:\n    ", results.summary, "\n", \
      " RAW_RESULT:\n    ", results.raw_result, "\n" \
      )

###################  FILE REPUTATION EXAMPLE - ReversingLabs ##############

from PangeaSecIntel import get_file_reputation

# set the URL to be checked and the reputation data provider

unknown_file = "142b638c6a60b60c7f9928da4fb85a5a8e1422a9ffdc9ee49e17e56ccca9cf6e"
hash_type="sha256"
file_intel_provider = "reversinglabs"

# call the Pangea FileIntel API to get ReversingLabs intel data
print("\n===============================================================================")
print("Calling Pangea FileIntel for the reputation of the file with the SHA256 hash \
        '142b638c6a60b60c7f9928da4fb85a5a8e1422a9ffdc9ee49e17e56ccca9cf6e' using ReversingLabs as the intel provider.")
results = get_file_reputation( unknown_file, hash_type, file_intel_provider)

if "ERROR" in results:
	print(results)
else:
	print("  STATUS:\n    ", results.status, "\n", \
      " SUMMARY:\n    ", results.summary, "\n", \
      " RAW_RESULT:\n    ", results.raw_result, "\n" \
      )


###################  FILE REPUTATION EXAMPLE - Crowdstrike ##############

from PangeaSecIntel import get_file_reputation

# set the URL to be checked and the reputation data provider

unknown_file = "142b638c6a60b60c7f9928da4fb85a5a8e1422a9ffdc9ee49e17e56ccca9cf6e"
hash_type="sha256"
file_intel_provider = "crowdstrike"

# call the Pangea FileIntel API to get Crowdstrike intel data
print("\n===============================================================================")
print("Calling Pangea FileIntel for the reputation of the file with the SHA256 hash \
        '142b638c6a60b60c7f9928da4fb85a5a8e1422a9ffdc9ee49e17e56ccca9cf6e' using Crowdstrike as the intel provider.")
results = get_file_reputation( unknown_file, hash_type, file_intel_provider)

if "ERROR" in results:
	print(results)
else:
	print("  STATUS:\n    ", results.status, "\n", \
      " SUMMARY:\n    ", results.summary, "\n", \
      " RAW_RESULT:\n    ", results.raw_result, "\n" \
      )


###################  USERNAME REPUTATION EXAMPLE - SpyCloud ##############

from PangeaSecIntel import get_username_reputation

# set the URL to be checked and the reputation data provider

unknown_username = "myusername"
username_intel_provider = "spycloud"

# call the Pangea UserIntel API to get SpyCloud intel data
print("\n===============================================================================")
print("Calling Pangea UserIntel for the reputation of the username 'myusername' using SpyCloud as the intel provider.")
results = get_username_reputation( unknown_username)

if "ERROR" in results:
	print(results)
else:
	print("  STATUS:\n    ", results.status, "\n", \
      " SUMMARY:\n    ", results.summary, "\n", \
      " RAW_RESULT:\n    ", results.raw_result, "\n" \
      )


