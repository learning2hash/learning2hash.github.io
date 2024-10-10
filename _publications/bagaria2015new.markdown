---
layout: publication
title: New Hashing Algorithm For Use In TCP Reassembly Module Of IPS
authors: Bagaria Sankalp
conference: "Arxiv"
year: 2015
bibkey: bagaria2015new
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1501.02062"}
tags: ['ARXIV', 'Graph']
---
Since last decade IDS/ IPS has gained popularity in protecting large networks. They can employ signature based techniques and/or flow-based techniques to prevent intrusion from outside/ inside the network they are trying to protect. Signature based IDS/ IPS can be stateless or stateful. Stateful IDS can store the state of the protocol and use it for better detection of malware. In the case of TCP/IP networks an attacker can also launch an attack such that the malicious code is distributed over many packets. These packets pass through the traditional IDS/ IPS and reassemble inside the network. Once re-assembled inside the network by the TCP/IP layer the malicious code launches an attack. The TCP state and a copy of last few packets for each active connection has to be maintained in IDS/IPS. In TCP re-assembly packets are re-assembled at IDS/IPS and searched for signature matches. A connection table has to be maintained for active connections and their list of last few (atmost 11) packets that have already arrived. We need data structures for searching the connection that the latest incoming packet belongs to. Popular hashing algorithms like CRC XOR summing tuple taking modulus are inefficient as hash keys are not evenly distributed in hash-key space. Thus we show how an algorithm based on cryptography concepts can be used for efficient hashing in network connection management. We also show how to use full four tuple for calculating hash key instead of simply summing the tuple and taking the modulus of the sum.
