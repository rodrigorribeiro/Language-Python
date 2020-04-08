#!/usr/bin/env python

__author__ = "Rodrigo Ribeiro"
__version__ = "1.0.0"

import os
import re
import zlib
import cv2
from scapy.all import *

def get_http_headers(http_payload):
	
	try:
	
		# split headers http traffic
		headers_raw = http_payload[:http_payload.index("\r\n\r\n")+2]
		
		# split fields from headers
		headers = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", headers_raw))
	except:
		return None

	return headers

def extract_image(headers, http_payload):

	image = None
	image_type = None
	
	try:
		
		if "image" in headers['Content-Type']:
		
			# get the content image and payload
			image_type = headers['Content-Type'].split("/")[1]
			image = http_payload[http_payload.index("\r\n\r\n")+4:]
			
			# if detect a compressed file, extract image
			try:
				
				if "Content-Encoding" in headers.keys():
					if headers['Content-Encoding'] == "gzip":
						image = zlib.decompress(image, 16+zlib.MAX_WBITS)
					elif headers['Content-Encoding'] == "deflate":
						image = zlib.decompress(image)
			
			except:
				pass
	except:
		return None, None
	
	return image, image_type
	
def face_detect(path,file_name):

	img = cv2.imread(path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
	reacts = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))
	
	if len(reacts) == 0:
		return False
		
	reacts[:, 2:] += reacts[:, :2]
	
	# detect faces from image
	for (x, y, w, h) in reacts:
		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
	cv2.imwrite("%s/%s-%s" % (faces_directory,pcap_file,file_name),img)
	
	return True

def http_assembler(pcap_file):

	carved_images = 0
	faces_detected = 0
	
	a = rdpcap(pcap_file)
	
	sessions = a.sessions()
	
	for session in sessions:
	
		http_payload = ""
		
		for packet in sessions[session]:
		
			try:
				if packet[TCP].dport == 80 or packet[TCP].sport == 80:
					# remount the stream
					http_payload += str(packet[TCP].payload)
			except:
				pass
		
		headers = get_http_headers(http_payload)
		
		if headers is None:
			continue
		
		image, image_type = extract_image(headers,http_payload)
		
		if image is not None and image_type is not None:
		
			# store the image
			file_name = "%s-pic_carver_%d.%s" % (pcap_file, carved_images,image_type)
			
			fd = open("%s/%s" % (pictures_directory,file_name),"wb")
			
			fd.write(image)
			fd.close()
			
			carved_images += 1
			
			# now, try to detect a face
			try:
				result = face_detect("%s/%s" % (pictures_directory,file_name), file_name)
				if result is True:
					faces_detected += 1
			except:
				pass
	return carved_images, faces_detected

banner  = "------------------------------------------------\n"
banner += "|    PCAP - Extract Images and Detect Faces    |\n"
banner += "------------------------------------------------\n"
print banner

if len(sys.argv) > 1:

	pcap_file = sys.argv[1]
	
	pictures_directory = "./pictures"
	faces_directory = "./faces"
	
	if not os.path.exists(pictures_directory):
		os.makedirs(pictures_directory)
	
	if not os.path.exists(faces_directory):
		os.makedirs(faces_directory)
	
	carved_images, faces_detected = http_assembler(pcap_file)

	print "[*] Extracted: %d images" % carved_images
	print "[*] Detected: %d faces" % faces_detected

else:

	print "[!] You need to specify a pcap file!"
	print "[-] Usage: # pcap_eidf.py file.pcap"