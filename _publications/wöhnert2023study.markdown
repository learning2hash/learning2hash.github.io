---
layout: publication
title: 'A Study On The Use Of Perceptual Hashing To Detect Manipulation Of Embedded Messages In Images'
authors: Sven-jannik Wöhnert, Kai Hendrik Wöhnert, Eldar Almamedov, Carsten Frank, Volker Skwarek
conference: "Arxiv"
year: 2023
citations: 0
bibkey: wöhnert2023study
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2303.00092'}
tags: ['Hashing Fundamentals', 'Quantization and Compression', 'Hashing Methods']
---
Typically, metadata of images are stored in a specific data segment of the
image file. However, to securely detect changes, data can also be embedded
within images. This follows the goal to invisibly and robustly embed as much
information as possible to, ideally, even survive compression.
  This work searches for embedding principles which allow to distinguish
between unintended changes by lossy image compression and malicious
manipulation of the embedded message based on the change of its perceptual or
robust hash. Different embedding and compression algorithms are compared.
  The study shows that embedding a message via integer wavelet transform and
compression with Karhunen-Loeve-transform yields the best results. However, it
was not possible to distinguish between manipulation and compression in all
cases.
