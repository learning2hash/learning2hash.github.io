---
layout: publication
title: 'Microyolo: Towards Single-shot Object Detection On Microcontrollers'
authors: "Mark Deutel, Christopher Mutschler, J\xFCrgen Teich"
conference: Communications in Computer and Information Science
year: 2024
bibkey: deutel2024microyolo
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.15865'}]
tags: ["Efficiency", "Memory Efficiency"]
short_authors: "Mark Deutel, Christopher Mutschler, J\xFCrgen Teich"
---
This work-in-progress paper presents results on the feasibility of
single-shot object detection on microcontrollers using YOLO. Single-shot object
detectors like YOLO are widely used, however due to their complexity mainly on
larger GPU-based platforms. We present microYOLO, which can be used on Cortex-M
based microcontrollers, such as the OpenMV H7 R2, achieving about 3.5 FPS when
classifying 128x128 RGB images while using less than 800 KB Flash and less than
350 KB RAM. Furthermore, we share experimental results for three different
object detection tasks, analyzing the accuracy of microYOLO on them.