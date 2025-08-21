---
layout: publication
title: 'Sketch Less Face Image Retrieval: A New Challenge'
authors: Dawei Dai, Yutang Li, Liang Wang, Shiyu Fu, Shuyin Xia, Guoyin Wang
conference: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2023
bibkey: dai2023sketch
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.05576'}]
tags: ["Datasets", "ICASSP", "Image Retrieval", "Tools & Libraries"]
short_authors: Dai et al.
---
In some specific scenarios, face sketch was used to identify a person.
However, drawing a complete face sketch often needs skills and takes time,
which hinder its widespread applicability in the practice. In this study, we
proposed a new task named sketch less face image retrieval (SLFIR), in which
the retrieval was carried out at each stroke and aim to retrieve the target
face photo using a partial sketch with as few strokes as possible (see Fig.1).
Firstly, we developed a method to generate the data of sketch with drawing
process, and opened such dataset; Secondly, we proposed a two-stage method as
the baseline for SLFIR that (1) A triplet network, was first adopt to learn the
joint embedding space shared between the complete sketch and its target face
photo; (2) Regarding the sketch drawing episode as a sequence, we designed a
LSTM module to optimize the representation of the incomplete face sketch.
Experiments indicate that the new framework can finish the retrieval using a
partial or pool drawing sketch.