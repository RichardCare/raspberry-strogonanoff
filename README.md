Raspberry Strogonanoff
======================

A Raspberry Pi Remote Mains Switcher, to switch these

http://www.maplin.co.uk/remote-controlled-mains-sockets-5-pack-348217

with one of these

http://proto-pic.co.uk/434mhz-rf-link-transmitter/

using the documentation of the protocol detailed here

http://elektronikforumet.com/wiki/index.php/RF_Protokoll_-_Nexa/Proove_%28%C3%A4ldre,_ej_sj%C3%A4lvl%C3%A4rande%29


Installation
------------

Requires WiringPi-Python

    git clone https://github.com/WiringPi/WiringPi-Python.git
    cd WiringPi-Python/
    git submodule update --init
    sudo apt-get install python2.7-dev
    sudo apt-get install python-setuptools
    sudo python setup.py install

Running
-------

Needs to be run as root - 

    sudo python strogonanoff_sender.py --channel 1 --button 3 --gpio 8 on 
    
where the GPIO pin numbers are the big ones on this diagram ![](http://pi4j.com/images/p1header-large.png)


