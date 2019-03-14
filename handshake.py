#!/usr/bin/env python

import sys
import serial
from dorji import uart_transaction
from dorji import handshake

exit(handshake())
