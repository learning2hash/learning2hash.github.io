---
layout: publication
title: 'Livechess2fen: A Framework For Classifying Chess Pieces Based On Cnns'
authors: "David Mallas\xE9n Quintana, Alberto Antonio del Barrio Garc\xEDa, Manuel\
  \ Prieto Mat\xEDas"
conference: Arxiv
year: 2020
bibkey: quintana2020livechess2fen
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.06858'}]
tags: ["Tools & Libraries"]
short_authors: "David Mallas\xE9n Quintana, Alberto Antonio del Barrio Garc\xEDa,\
  \ Manuel Prieto Mat\xEDas"
---
Automatic digitization of chess games using computer vision is a significant
technological challenge. This problem is of much interest for tournament
organizers and amateur or professional players to broadcast their
over-the-board (OTB) games online or analyze them using chess engines. Previous
work has shown promising results, but the recognition accuracy and the latency
of state-of-the-art techniques still need further enhancements to allow their
practical and affordable deployment. We have investigated how to implement them
on an Nvidia Jetson Nano single-board computer effectively. Our first
contribution has been accelerating the chessboard's detection algorithm.
Subsequently, we have analyzed different Convolutional Neural Networks for
chess piece classification and how to map them efficiently on our embedded
platform. Notably, we have implemented a functional framework that
automatically digitizes a chess position from an image in less than 1 second,
with 92% accuracy when classifying the pieces and 95% when detecting the board.