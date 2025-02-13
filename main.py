from flask import Flask
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/wakepc')
def wakepc():
    mac_address = "00:1A:2B:3C:4D:5E"  # Replace with your PC’s MAC address
    send_magic_packet(mac_address)
    return "PC Wake-on-LAN signal sent!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
