# dependencies
# flask        (pip3 install flask)
# pangea-sdk   (pip3 install pangea-sdk)
# PangeaSecIntel.py (in same directory)

from flask import Flask, redirect, render_template, request, url_for
from PangeaSecIntel import get_domain_reputation, get_ip_reputation, get_url_reputation, \
                           get_file_reputation, get_username_reputation

app = Flask(__name__)

# pangea environment setup
import os
from pangea.config import PangeaConfig
from pangea.services import DomainIntel
PANGEA_INTEL_DOMAIN = os.getenv("PANGEA_INTEL_DOMAIN")
PANGEA_DOMAIN_TOKEN = os.getenv("PANGEA_DOMAIN_TOKEN")
PANGEA_IP_TOKEN = os.getenv("PANGEA_IP_TOKEN")
PANGEA_FILE_TOKEN = os.getenv("PANGEA_FILE_TOKEN")
PANGEA_URL_TOKEN = os.getenv("PANGEA_URL_TOKEN")

intel_requested = ""


@app.route("/", methods=["GET", "POST"])
def main_menu():
    # Process the GET method to refresh the page to the original state
    if request.method == "GET":
        return render_template("main_page.html", intel_requested = "None requested.")

    # Prosses the POST method possibilities, checking for input from each field on the form,
    # gather the user input, and then call the corresponding reputation function in PangeaSecIntel
    elif request.form['Intel'] == "Domain Reputation":
        intel_requested = domain_rep_info(request.form.get('the_domain'))
    elif request.form['Intel'] == "URL Reputation":
        intel_requested = url_rep_info(request.form.get('the_url'))
    elif request.form['Intel'] == "IP Reputation":
        intel_requested = ip_rep_info(request.form.get('the_ip'))
    elif request.form['Intel'] == "File Reputation":
        intel_requested = file_rep_info(request.form.get('the_file'))
    elif request.form['Intel'] == "Username Reputation":
        intel_requested = username_rep_info(request.form.get('the_username'))
    else:
        intel_requested = "ERROR: Unexpected Reputation request."

    # send the requested reputation information back to be diplayed at the bottom
    return render_template("main_page.html", intel_requested = intel_requested)


def domain_rep_info(domain_arg):
    domain_intel_provider = "crowdstrike"
    temp = get_domain_reputation( domain_arg, domain_intel_provider )
    results = format_pangea_results(domain_arg, temp)
    return results


def url_rep_info(url_arg):
    url_intel_provider = "crowdstrike"
    temp = get_url_reputation( url_arg, url_intel_provider )
    results = format_pangea_results(url_arg, temp)
    return results



def ip_rep_info(ip_arg):
    ip_intel_provider = "crowdstrike"
    temp = get_ip_reputation( ip_arg, ip_intel_provider )
    results = format_pangea_results(ip_arg, temp)
    return results



def file_rep_info(file_arg):
    file_intel_provider = "reversinglabs"
    hash_type="sha256"
    temp = get_file_reputation( file_arg, hash_type, file_intel_provider )
    results = format_pangea_results(file_arg, temp)
    return results



def username_rep_info(username_arg):
    username_intel_provider = "spycloud"
    temp = get_username_reputation( username_arg)
    results = format_pangea_results(username_arg, temp)
    return results




def format_pangea_results(reputation_item, full_results):
    formated_results = \
      " <h3>Pangea Reputation Intel for: " + str(reputation_item) + "</h3>" + \
      " <p>API CALL STATUS:</p><p>" + str(full_results.status) + "</p>" + \
      " <p>REPUTATION SUMMARY:</p><p>" + str(full_results.summary) + "</p>" + \
      " <p>RAW_RESULT:</p><p>" + str(full_results.raw_result) + "</p>"
    return formated_results


