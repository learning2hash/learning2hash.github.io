---
layout: publication
title: A study on the use of perceptual hashing to detect manipulation of embedded messages in images
authors: Wöhnert Sven-Jannik, Wöhnert Kai Hendrik, Almamedov Eldar, Frank Carsten, Skwarek Volker
conference: "Arxiv"
year: 2023
bibkey: wöhnert2023study
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2303.00092"}
tags: ['ARXIV', 'General']
---
Typically metadata of images are stored in a specific data segment of the image file. However to securely detect changes data can also be embedded within images. This follows the goal to invisibly and robustly embed as much information as possible to ideally even survive compression. This work searches for embedding principles which allow to distinguish between unintended changes by lossy image compression and malicious manipulation of the embedded message based on the change of its perceptual or robust hash. Different embedding and compression algorithms are compared. The study shows that embedding a message via integer wavelet transform and compression with Karhunen-Loeve-transform yields the best results. However it was not possible to distinguish between manipulation and compression in all cases.
