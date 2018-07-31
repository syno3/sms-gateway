## Welcome to sms-gateway

![sms](https://raw.githubusercontent.com/syno3/sms-gateway/master/Images/sms3.png)<br>
An SMS gateway allows a computer to send or receive Short Message Service (SMS) transmissions to or from a telecommunications network. Most messages are eventually routed into the mobile phone networks. Many SMS gateways support media conversion from email and other formats.This is a great way of bypassing the high text rates charged by the network providers.
### How it works
The Gateway can convert complicated SMS protocols into more common protocols such as HTTP. This means that developers can use web-based applications to develop an independent SMS service.<br>
for more information visit [quora](https://www.quora.com/How-does-SMS-gateways-work)
![sms2](https://qph.ec.quoracdn.net/main-qimg-55497d0e94f38b86ac02e9cf56001fb5)
### Prerequisites
Inorder to run this script on your system you need to have python installed, this can be done the `apt-get install python`command.You will also need to have git installed in your computer use `apt-get install git` to download the package.Lastly am going  to be using asciimatics so you will have to download it through `pip install asciimatics` and you are good to go.
 ### Installing and running the scripts
 ```
apt update
apt upgrade
git clone https://github.com/syno3/sms-gateway
cd sms-gateway
chmod 755 *
python initial.py
