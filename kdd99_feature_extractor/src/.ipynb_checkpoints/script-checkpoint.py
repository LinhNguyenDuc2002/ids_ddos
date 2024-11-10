import numpy as np
import pickle
import sys

protocol_type = {
    "icmp" : 0,
    "tcp" : 1,
    "udp" : 2,
}

service = {
    "IRC" : 0,
    "X11" : 1,
    "Z39_50" : 2,
    "auth" : 3,
    "bgp" : 4,
    "courier" : 5,
    "csnet_ns" : 6,
    "ctf" : 7,
    "daytime" : 8,
    "discard" : 9,
    "domain" : 10,
    "domain_u" : 11,
    "echo" : 12,
    "eco_i" : 13,
    "ecr_i" : 14,
    "efs" : 15,
    "exec" : 16,
    "finger" : 17,
    "ftp" : 18,
    "ftp_data" : 19,
    "gopher" : 20,
    "hostnames" : 21,
    "http" : 22,
    "http_443" : 23,
    "imap4" : 24,
    "iso_tsap" : 25,
    "klogin" : 26,
    "kshell" : 27,
    "ldap" : 28,
    "link" : 29,
    "login" : 30,
    "mtp" : 31,
    "name" : 32,
    "netbios_dgm" : 33,
    "netbios_ns" : 34,
    "netbios_ssn" : 35,
    "netstat" : 36,
    "nnsp" : 37,
    "nntp" : 38,
    "ntp_u" : 39,
    "other" : 40,
    "pop_2" : 41,
    "pop_3" : 42,
    "printer" : 43,
    "private" : 44,
    "red_i" : 45,
    "remote_job" : 46,
    "rje" : 47,
    "shell" : 48,
    "smtp" : 49,
    "sql_net" : 50,
    "ssh" : 51,
    "sunrpc" : 52,
    "supdup" : 53,
    "systat" : 54,
    "telnet" : 55,
    "tftp_u" : 56,
    "tim_i" : 57,
    "time" : 58,
    "urh_i" : 59,
    "urp_i" : 60,
    "uucp" : 61,
    "uucp_path" : 62,
    "vmnet" : 63,
    "whois" : 64,
}

flag = {
    "OTH" : 0,
    "REJ" : 1,
    "RSTO" : 2,
    "RSTR" : 3,
    "S0" : 4,
    "S1" : 5,
    "S2" : 6,
    "S3" : 7,
    "SF" : 8,
    "SH" : 9,
}

input = sys.argv[1]
data = input.split(',')
input_list = []
for x in range(len(data)):
    if x == 1:
        input_list.append(protocol_type.get(data[x]))
    elif x == 2:
        input_list.append(service.get(data[x]))
    elif x == 3:
        input_list.append(flag.get(data[x]))
    else:
        input_list.append(float(data[x]))

with open('random_forest_model_28.pkl', 'rb') as file:
    model = pickle.load(file)
    result = model.predict(np.array([input_list]))[0]
    if result == 0:
        print(input + " => " + "DDoS attack")
    else: 
        print(input + " => " + "Nornal")
