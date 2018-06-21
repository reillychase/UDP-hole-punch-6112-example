import _winreg
import stun
import requests
import socket
import time
import json

def get_war2_port():
    # Open the key and return the handle object
    hKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\Battle.net\Configuration")
    # Read the value
    try:
      result = _winreg.QueryValueEx(hKey, "Game Data Port")
    # If not found, set to default
    except Exception as e:
      print e
      result = [6112]
    # Return port
    return result[0]

war2_port = get_war2_port()
nat_type, external_ip, external_port = stun.get_ip_info("0.0.0.0", war2_port)
req = requests.get('https://war2.info/nat_stats.php?nat_type=' + str(nat_type))

if nat_type != "Sytmmetric NAT":
  while True:
    time.sleep(10)
    req = requests.get('https://war2.info/player_ips.php')
    json_obj = json.loads(req.content)
    player_ip_list = json_obj["player_ips"]
    print player_ip_list
    for player_ip in player_ip_list:
      try:
        # Target host is IP of player you want to be able to join your game
        target_host = player_ip

        # create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.bind(('0.0.0.0', war2_port))

        # send some data
        client.sendto("For the Alliance", (target_host, war2_port))
        client.shutdown()
        client.close()
        print "Sent data to " + str(player_ip) + " on port " + str(war2_port)
      except Exception as e:
        print e
