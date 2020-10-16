# OpenVPN 

Provides flexible VPN solutions to secure your data communications, whether it's for Internet privacy, remote access for employees, securing IoT, or for networking Cloud data centers.
Our VPN Server software solution can be deployed on-premises using standard servers or virtual appliances, or on the cloud.

# FixOpenVPNFiles
A small Python Script made to add a path of a user/path file as auth-user-path argument in an OpenVPN configuration file.
It also will remove the "comp-lzo" option because this option is deprecated from OpenVPN 2.4.
The script has to be executed in the same directory of the .ovpn files.
Of course, you have to change the userPath to the path of your file containing your VPN's username and password (1 by line, nothing else).
