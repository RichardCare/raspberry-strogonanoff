# NAME
Raspberry Strogonanoff

# SYNOPSIS
**strogonanoff_sender.py** [OPTIONS] [on|off]

# DESCRIPTION
A Raspberry Pi Remote Mains Switcher, to switch these

http://www.maplin.co.uk/remote-controlled-mains-sockets-5-pack-348217

with one of these

http://proto-pic.co.uk/434mhz-rf-link-transmitter/

using the documentation of the protocol detailed here

http://elektronikforumet.com/wiki/index.php/RF_Protokoll_-_Nexa/Proove_%28%C3%A4ldre,_ej_sj%C3%A4lvl%C3%A4rande%29

# OPTIONS
    -v, --verbose   enable verbose logging
    -g, --gpio      the GPIO pin of the Raspberry Pi to control (default is 0)
    -c, --channel   'channel' number to send to
                    The 'channel' number sets the 'code' group to send.
                    On the receiving socket device the 'code adjustment dial'
                    is labelled I, II, III & IV, the same as on the remote
                    control's 'code adjustment switch', but this parameter
                    requires 1, 2, 3 or 4 (default is 1).
    -b, --button    'button' number to 'press'
                    The remote control has 8 buttons arranged in 4 rows. This
                    parameter sets the row of buttons being 'pressed'. On the
                    receiving socket device the 'channel adjustment dial'
                    sets which button row corresponds to which receiving
                    socket device, values are 1, 2, 3 or 4 (default is 1)
    [on|off]        whether to send a 'turn on' command or a 'turn off'
                    command (default is on)

# INSTALLATION

Requires WiringPi-Python

    git clone https://github.com/WiringPi/WiringPi-Python.git
    cd WiringPi-Python/
    git submodule update --init
    sudo apt-get install python2.7-dev
    sudo apt-get install python-setuptools
    sudo python setup.py install

# EXAMPLE

Needs to be run as root - 

    sudo python strogonanoff_sender.py --channel 1 --button 3 --gpio 8 on 
    
where the GPIO pin numbers are the big ones on this diagram ![](http://pi4j.com/images/p1header-large.png)


