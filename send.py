#!/usr/bin/env python3

import argparse
import logging

from rpi_rf import RFDevice

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

parser = argparse.ArgumentParser(description='Отправка десятичных кодов через устройство GPIO 433/315 МГц')
parser.add_argument('code', metavar='CODE', type=int,
                    help="Десятичный код для отправки")
parser.add_argument('-g', dest='gpio', type=int, default=21,
                    help="GPIO порт (по умолчанию: 21)")
parser.add_argument('-p', dest='pulselength', type=int, default=None,
                    help="Длина импульса (по умолчанию: 350)")
parser.add_argument('-t', dest='protocol', type=int, default=None,
                    help="Протокол (по умолчанию: 1)")
args = parser.parse_args()

rfdevice = RFDevice(args.gpio)
rfdevice.enable_tx()

if args.protocol:
    protocol = args.protocol
else:
    protocol = "default"
if args.pulselength:
    pulselength = args.pulselength
else:
    pulselength = "default"
logging.info(str(args.code) +
             " [протокол " + str(protocol) +
             ", длина импульса " + str(pulselength) + "]")

rfdevice.tx_code(args.code, args.protocol, args.pulselength)
rfdevice.cleanup()














