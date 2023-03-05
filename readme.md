# \[WIP\] streamdeck_application
A open-source cross plattform streamdeck software written in python
<br>
<br>
<br>

## Brainstorming / ideas / concepts
Configs for streamdecks will be stored in seperate folders for every deck, identified by their serial number.
This my first concept for the config.json for a streamdeck:
```json
{
  "displayName": "zoe-streamdeck-mini",
  "group": "devicegrp_default",
  "menus": [
    {
      "name": "menu_1",
      "buttons": [
        {},
        {},
        {},
        {
          "name": "btn_standby",
          "onRelease": [
            {
              "action_module": "device",
              "action": "standby"
            }
          ],
          "defaultBackgroundImage": "img_bg_power"
        },
        "btn_menu_1",
        "btn_menu_2"
      ]
    },
    {
      "name": "menu_2",
      "buttons": [
        {},
        {},
        {},
        {
          "name": "btn_standby",
          "onRelease": [
            {
              "action_module": "device",
              "action": "standby"
            }
          ],
          "defaultBackgroundImage": "img_bg_power"
        },
        "btn_menu_1",
        "btn_menu_2"
      ]
    }
  ],
  "buttons": [
    {
      "name": "btn_menu_1",
      "group": "btngrp_menu",
      "onRelease": [
        {
          "action_module": "device",
          "action": "openMenu",
          "action_parameter": ["menu1"]
        },
        "func_btngrp_menu_removeOverlay_img_overlay_selected",
        "func_self_addOverlay_img_overlay_selected"
      ],
      "defaultBackgroundImage": "img_bg_folder"
    },
    {
      "name": "btn_menu_2",
      "group": "btngrp_menu",
      "onRelease": [
        {
          "action_module": "device",
          "action": "openMenu",
          "action_parameter": ["menu2"]
        },
        "func_btngrp_menu_removeOverlay_img_overlay_selected",
        "func_self_addOverlay_img_overlay_selected"
      ],
      "defaultBackgroundImage": "img_bg_folder"
    }
  ],
  "functions": [
    {
      "name": "func_btngrp_menu_removeOverlay_img_overlay_selected",
      "onCall": {
        "action_module": "button",
        "action_target": "btngrp_menu",
        "action": "removeOverlay",
        "action_parameter": ["img_overlay_selected"]
      }
    },
    {
      "name": "func_self_addOverlay_img_overlay_selected",
      "onCall": {
        "action_module": "button",
        "action": "addOverlay",
        "action_parameter": ["img_overlay_selected"]
      }
    }
  ],
  "backgroundImages": [
    {
      "name": "img_bg_folder",
      "imgPath": "./folder.png"
    },
    {
      "name": "img_bg_power",
      "imgPath": "./power.png"
    }
  ],
  "overlayImages": [
    {
      "name": "img_overlay_selected",
      "imgPath": "./selected.png"
    }
  ]
}

```
<br>
<br>
<br>

## Installation
Install python3, clone this repository and install the [python-elgato-streamdeck](https://github.com/abcminiuser/python-elgato-streamdeck) libary

### Quick install script for Linux with APT:
```bash
# Install dependencies
sudo apt update
sudo apt install -y libudev-dev libusb-1.0-0-dev libhidapi-libusb0 python3-pip python3-setuptools
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
To run the application, run `python3 main.py`