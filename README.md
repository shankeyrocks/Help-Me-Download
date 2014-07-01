Help-Me-Download
================

A downloader that efficiently divides a download amongst systems connected to different networks and later joins to files on the main system. This apparently increased the speed of download.




"Server.py" has to be run on the main system which wants others to help him in downloading any data.
When this is ran, a port is opened to which all the available clients can connect by running client.py on their system.
Right now the the ip address is 'localhost' for testing purposes but it can be changed to the system ip address on the shared network(already tested and it works :) )
Similarly in client.py the ip address can be changed to system ip address on the shared network.
I will update the code soon so that it automatically grabs the system ip address.
Also i will add GUI to both. Right now only server has GUI. client is console based.

Any number of clients can be added and the data download size will be divided amongst them equally right now but i am updating code to divide size as per download speed of every connected system.

Tell me if you find any bugs. I will try to make it more efficient :)
