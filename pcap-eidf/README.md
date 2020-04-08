# PCAP - Extract Images and Detect Faces
> Read pcap files and extract all images files and detect does images contains a face

This code in python can read pcap files and extract all images files and detect does images contains a face..

## Requirements

There are some libraries requirements:

os, re, zlib, cv2, scapy

```sh
pip install opencv-python
pip install scapy
```

## Installation

There are no installation.

## Usage example

You need to specify only on argument, example:

```sh
------------------------------------------------
|    PCAP - Extract Images and Detect Faces    |
------------------------------------------------

[!] You need to specify a pcap file!
[-] Usage: # pcap-eidf.py file.pcap
```

The result example:

```sh
------------------------------------------------
|    PCAP - Extract Images and Detect Faces    |
------------------------------------------------

[*] Extracted: 4 images
[*] Detected: 2 faces
```

Two new folders will be created:
```sh
pictures
faces
```

pictures -> All images extracted from the pcap will be saved here.
faces -> All faces detected in images files will be here, if you take a look the images will be contained a draw green around the face detected.

## Development setup

There are no development setup.

## Release History

* 1.0.0
    * The first proper release

## Meta

Rodrigo Ribeiro – [@silvarribeiros](https://twitter.com/silvarribeiros) – silva.rrs@gmail.com

[https://github.com/rodrigorribeiro/](https://github.com/rodrigorribeiro/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
