---
layout: publication
title: Person Detection Using An Ultra Low-resolution Thermal Imager On A Low-cost
  MCU
authors: "Maarten Vandersteegen, Wouter Reusen, Kristof van Beeck, Toon Goedem\xE9"
conference: Lecture Notes in Computer Science
year: 2023
bibkey: vandersteegen2022person
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.08415'}]
tags: ["Datasets", "Evaluation"]
short_authors: Vandersteegen et al.
---
Detecting persons in images or video with neural networks is a well-studied
subject in literature. However, such works usually assume the availability of a
camera of decent resolution and a high-performance processor or GPU to run the
detection algorithm, which significantly increases the cost of a complete
detection system. However, many applications require low-cost solutions,
composed of cheap sensors and simple microcontrollers. In this paper, we
demonstrate that even on such hardware we are not condemned to simple classic
image processing techniques. We propose a novel ultra-lightweight CNN-based
person detector that processes thermal video from a low-cost 32x24 pixel static
imager. Trained and compressed on our own recorded dataset, our model achieves
up to 91.62% accuracy (F1-score), has less than 10k parameters, and runs as
fast as 87ms and 46ms on low-cost microcontrollers STM32F407 and STM32F746,
respectively.