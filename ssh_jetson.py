import argparse
import os

# alias jetssh='python /data/jliu/Tools/ssh_jetson.py --device'

parser = argparse.ArgumentParser(description="ssh corresponding jetson device.")

parser.add_argument('--device', type=str, default='')

args = parser.parse_args()
if 'edge' in args.device:
    os.system('ssh %s@192.168.1.%02d' % (args.device, int(args.device[-2:])+10))
elif 'agx' in args.device:
    os.system('ssh %s@192.168.1.%02d' % (args.device, int(args.device[-2:])+80))
elif 'nx' in args.device:
    os.system('ssh %s@192.168.1.%02d' % (args.device, int(args.device[-2:])+40))
