# IP-Hunter - Cybaze-Project-Work


### Features

IP Hunter is a 360° Scanner that can do multiple operation:

* IP HUNTER & CHECKER:
  Scan for an IP to know if it is an internal or external IP, the class of the IP address and the information about an external IP from ipwhois and AbuseIPDB
* DNS RESOLVER:Resolve an URL or domain name in the IP address(es) that expose that domain
* PRIVATE IP DATABASE: Database of information about an internal IP with whitelist/blacklist discrimination. You must login before the use
* SSL SCANNER: Scan an URL on 443 port to collect information about SSL certificate
* NETWORK PORT SCANNER: Scan a specific internal host to determinate which port are open and verify if the host is working properly
------------



Quick start
-----------

SSLyze can be installed directly via pip:

    $ pip install --upgrade setuptools
    $ pip install --upgrade sslyze
    $ python -m sslyze --regular www.yahoo.com:443 www.google.com "[2607:f8b0:400a:807::2004]:443"

Documentation
-------------

Documentation is [available here][documentation].

