"""This script will create an x509 cert and private key.
Modifed by Travis Beckwith for USD Class 504."""

from OpenSSL import crypto, SSL
import socket
from pprint import pprint
from time import gmtime, mktime
import shutil, os
import random

host_name = socket.gethostname()

if 'private.key' == True:
    os.remove("private.key")
    os.remove("cert.crt")
    os.chdir("app")
    os.remove("private.key")
    os.remove("cert.crt")
    os.chdir("..")
else:
    print("x509 certificate required for deployment!"'\n'"Please perform the following steps.")



    CountryName = input("Enter country name (ex. US): ")
    StateOrProvinceName = input("Enter state or province name: ")
    LocalityName = input("Enter city name: ")
    OrganizationName = input("Enter organization name: ")
    OrganizationUnitName = input("Enter unit name: ")
    CommonName = '{}'.format(host_name)

    def generate_cert(
        cert_file = "cert.crt",
        pk_file = "private.key"):

        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 2048)

        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = CountryName
        cert.get_subject().ST = StateOrProvinceName
        cert.get_subject().L = LocalityName
        cert.get_subject().O = OrganizationName
        cert.get_subject().OU = OrganizationUnitName
        cert.get_subject().CN = CommonName
        cert.set_serial_number(random.randrange(1000))
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(5*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_subject(cert.get_subject())
        cert.set_pubkey(k)
        cert.add_extensions([
            crypto.X509Extension(b'subjectAltName', True,
                ','.join([
                    'DNS:%s' % socket.gethostname(),
                    'DNS:*.%s' % socket.gethostname(),
                    'DNS:{}'.format(host_name),
                    'DNS:*.{}'.format(host_name)]).encode()),
            crypto.X509Extension(b"basicConstraints", False, b"CA:false")])
        cert.sign(k, 'sha256')

        with open(cert_file, "wt") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
        with open(pk_file, "wt") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))

    generate_cert()

    def copy_files():
        files = ["cert.crt", "private.key"]
        for f in files:
            shutil.copy(f, 'app')

        print("Completed!")

    copy_files()
