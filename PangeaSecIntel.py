# PangeaSecIntel Module

def get_domain_reputation(domain_arg, provider_arg):

	# Imports
	import os
	from pangea.config import PangeaConfig
	from pangea.services import DomainIntel

	# check for required API tokens that should be stored in OS env variables.
	# Pangea API tokens and domain path are available in the Pangea Console
	PANGEA_DOMAIN_TOKEN = os.getenv("PANGEA_DOMAIN_TOKEN")
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_DOMAIN_TOKEN == "":
		return "ERROR: OS env variable not set - PANGEA_DOMAIN_TOKEN (in PangeaSecIntel.get_domain_reputation)"
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_INTEL_DOMAIN == "":
		return "ERROR: OS env variable not set - PANGEA_INTEL_DOMAIN (in PangeaSecIntel.get_domain_reputation)"

	# Set up the Pangea objects needed to access the API
	domain_intel_config = PangeaConfig(domain=PANGEA_INTEL_DOMAIN)
	domain_intel = DomainIntel(token=PANGEA_DOMAIN_TOKEN, config=domain_intel_config)

	# Call the Pangea DomainIntel API  endpoint
	results = domain_intel.reputation(domain=domain_arg, provider=provider_arg)

	return results


def get_ip_reputation(ip_arg, provider_arg):

	# Imports
	import os
	from pangea.config import PangeaConfig
	from pangea.services import IpIntel
	
	# check for required API tokens that should be stored in OS env variables.
	# Pangea API tokens and domain path are available in the Pangea Console
	PANGEA_IP_TOKEN = os.getenv("PANGEA_IP_TOKEN")
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_IP_TOKEN == "":
		return "ERROR: OS env variable not set - PANGEA_IP_TOKEN (in PangeaSecIntel.get_ip_reputation)"
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_INTEL_DOMAIN == "":
		return "ERROR: OS env variable not set - PANGEA_INTEL_DOMAIN (in PangeaSecIntel.get_ip_reputation)"

	ip_intel_config = PangeaConfig(domain=PANGEA_INTEL_DOMAIN)
	ip_intel = IpIntel(token=PANGEA_IP_TOKEN, config=ip_intel_config)

	# Call the Pangea IpIntel API endpoint
	results = ip_intel.reputation(ip=ip_arg, provider=provider_arg)
	return results 


def get_url_reputation(url_arg, provider_arg):
	# Imports
	import os
	from pangea.config import PangeaConfig
	from pangea.services import UrlIntel
	
	# check for required API tokens that should be stored in OS env variables.
	# Pangea API tokens and domain path are available in the Pangea Console
	PANGEA_URL_TOKEN = os.getenv("PANGEA_URL_TOKEN")
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_URL_TOKEN == "":
		return "ERROR: OS env variable not set - PANGEA_URL_TOKEN (in PangeaSecIntel.get_url_reputation)"
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_INTEL_DOMAIN == "":
		return "ERROR: OS env variable not set - PANGEA_INTEL_DOMAIN (in PangeaSecIntel.get_url_reputation)"
	
	# Set up the Pangea objects needed to access the API
	url_intel_config = PangeaConfig(domain=PANGEA_INTEL_DOMAIN)
	url_intel = UrlIntel(token=PANGEA_URL_TOKEN, config=url_intel_config)

	# Call the Pangea UrlIntel API endpoint
	results = url_intel.reputation(url=url_arg, provider=provider_arg)

	return results


def get_file_reputation(hash_arg, hash_type_arg, provider_arg):
	# Imports
	import os
	from pangea.config import PangeaConfig
	from pangea.services import FileIntel
	
	# check for required API tokens that should be stored in OS env variables.
	# Pangea API tokens and domain path are available in the Pangea Console
	PANGEA_FILE_TOKEN = os.getenv("PANGEA_FILE_TOKEN")
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_FILE_TOKEN == "":
		return "ERROR: OS env variable not set - PANGEA_FILE_TOKEN (in PangeaSecIntel.get_file_reputation)"
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_INTEL_DOMAIN == "":
		return "ERROR: OS env variable not set - PANGEA_INTEL_DOMAIN (in PangeaSecIntel.get_file_reputation)"
	
	# Set up the Pangea objects needed to access the API
	file_intel_config = PangeaConfig(domain=PANGEA_INTEL_DOMAIN)
	file_intel = FileIntel(token=PANGEA_FILE_TOKEN, config=file_intel_config)

 	# Call the Pangea FileIntel API endpoint
	results = file_intel.hashReputation(hash=hash_arg, hash_type=hash_type_arg, provider=provider_arg)

	return results

def get_username_reputation(username_arg):

	# Imports
	import os
	from pangea.config import PangeaConfig
	from pangea.services import UserIntel
	
	# check for required API tokens that should be stored in OS env variables.
	# Pangea API tokens and domain path are available in the Pangea Console
	PANGEA_USER_TOKEN = os.getenv("PANGEA_USER_TOKEN")
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_USER_TOKEN == "":
		return "ERROR: OS env variable not set - PANGEA_USER_TOKEN (in PangeaSecIntel.get_username_reputation)"
	PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
	if PANGEA_INTEL_DOMAIN == "":
		return "ERROR: OS env variable not set - PANGEA_INTEL_DOMAIN (in PangeaSecIntel.get_username_reputation)"

	# Set up the Pangea objects needed to access the API
	user_intel_config = PangeaConfig(domain=PANGEA_INTEL_DOMAIN)
	user_intel = UserIntel(token=PANGEA_USER_TOKEN, config=user_intel_config)

	results = user_intel.user_breached(username=username_arg)

	return results 



