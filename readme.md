# streamdeck_application
A open-source cross plattform streamdeck software written in python

## Installation
Clone this repository and install the [python-elgato-streamdeck](https://github.com/abcminiuser/python-elgato-streamdeck) libary

### Quick install script for Linux with APT:
```bash
# Install python-elgato-streamdeck libary and it's dependencies
sudo apt install -y libhidapi-libusb0
pip install streamdeck

# Clone the repo
git clone https://github.com/EmnichtdaYT/streamdeck_application && cd streamdeck_application

# Add udev rule to allow all users non-root access to Elgato StreamDeck devices
sudo tee /etc/udev/rules.d/10-streamdeck.rules << EOF
    SUBSYSTEMS=="usb", ATTRS{idVendor}=="0fd9", GROUP="users", TAG+="uaccess"
    EOF

# Reload udev rules to ensure the new permissions take effect
sudo udevadm control --reload-rules

```