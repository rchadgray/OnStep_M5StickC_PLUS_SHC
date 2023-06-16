# OnStep_M5StickC_PLUS_SHC
A big thank you to Anat in the OnStep group for posting this first bit of code that connects the M5StickC PLUS to OnStep's WiFi port.
https://onstep.groups.io/g/main/message/52115


This is an OnStep hand controller that uses off the shelf parts.  
https://shop.m5stack.com/collections/m5-controllers/products/m5stickc-plus-esp32-pico-mini-iot-development-kit
https://shop.m5stack.com/collections/m5-sensor/products/m5stickc-mini-joyc-hat-stm32f030

Read this documentation on gettin the VS Code Extension and how to upload the code to the 
https://docs.m5stack.com/en/quick_start/m5stickc_plus/mpy

Update 6-16-23
I got my hardware and found the easiest way to upload this pythong code is not with VS Code, but the UIFlow editor.

Follow these instruction https://docs.m5stack.com/en/quick_start/m5stickc/mpy and when you configure you hardware select "internet" instead of USB.  THis will allow the UIFLow editor to connecto to your hardware over wifi and upload your code.  The UIFlow is easier just becuase it seems to automatically handle the libraries needed for the Joystick.  I am sure VS Code works just fine you just have to figure out Micropython and how to load the joystick libraries.
