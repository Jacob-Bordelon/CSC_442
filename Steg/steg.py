import sys
import argparse

    
parser = argparse.ArgumentParser(prog='steg.py',conflict_handler="resolve")
parser.add_argument("-b","--bit", help="Use bit method", action="store_true")
parser.add_argument("-B","--Byte", help="Use byte method", action="store_true")
parser.add_argument("-s","--store", help="Store (and hide) data", action="store_true")
parser.add_argument("-r","--retrieve", help="Retrieve hidden data", action="store_true")
parser.add_argument("-o","--offset",help="Set offset to <val>",type=int)
parser.add_argument("-i","--interval",help=" Set interval to <val>",type=int)
parser.add_argument("-w","--wrapper_file",help="Set wrapper file to <val>")
parser.add_argument("-h","--hidden_file",help="Set hidden file to <val>")


args = parser.parse_args()
print args



