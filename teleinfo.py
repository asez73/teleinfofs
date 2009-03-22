#!/usr/bin/env python

import serial

class Teleinfo:

	ser = serial.Serial()
	
	def __init__ (self, port='/dev/ttyS2'):
		self.ser = serial.Serial(port, baudrate=1200, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN)
	
	def checksum (self, etiquette, valeur):
		sum = 32
		for c in etiquette: sum = sum + ord(c)
		for c in valeur: 	sum = sum + ord(c)
		sum = (sum & 63) + 32
		return chr(sum)
		
	def read (self):
		# Attendre le debut du message
		while self.ser.read(1) != chr(2): pass
		
		message = ""
		fin = False
		
		while not fin:
			char = self.ser.read(1)
			if char != chr(2):
				message = message + char
			else:
				fin = True
		
		trames = [
			trame.split(" ")
			for trame in message.strip("\r\n\x03").split("\r\n")
			]
			
		tramesValides = dict([
			[trame[0],trame[1]]
			for trame in trames
			if (len(trame) == 3) and (self.checksum(trame[0],trame[1]) == trame[2])
			])
			
		return tramesValides
