---
layout: publication
title: Vehicle And License Plate Recognition With Novel Dataset For Toll Collection
authors: Muhammad Usama, Hafeez Anwar, Abbas Anwar, Saeed Anwar
conference: Arxiv
year: 2022
bibkey: usama2022vehicle
citations: 9
additional_links: [{name: Code, url: 'https://github.com/usama-x930/VT-LPR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2202.05631'}]
tags: ["Datasets"]
short_authors: Usama et al.
---
We propose an automatic framework for toll collection, consisting of three
steps: vehicle type recognition, license plate localization, and reading.
However, each of the three steps becomes non-trivial due to image variations
caused by several factors. The traditional vehicle decorations on the front
cause variations among vehicles of the same type. These decorations make
license plate localization and recognition difficult due to severe background
clutter and partial occlusions. Likewise, on most vehicles, specifically
trucks, the position of the license plate is not consistent. Lastly, for
license plate reading, the variations are induced by non-uniform font styles,
sizes, and partially occluded letters and numbers. Our proposed framework takes
advantage of both data availability and performance evaluation of the backbone
deep learning architectures. We gather a novel dataset, *Diverse Vehicle
and License Plates Dataset (DVLPD)*, consisting of 10k images belonging to six
vehicle types. Each image is then manually annotated for vehicle type, license
plate, and its characters and digits. For each of the three tasks, we evaluate
You Only Look Once (YOLO)v2, YOLOv3, YOLOv4, and FasterRCNN. For real-time
implementation on a Raspberry Pi, we evaluate the lighter versions of YOLO
named Tiny YOLOv3 and Tiny YOLOv4. The best Mean Average Precision (mAP@0.5) of
98.8% for vehicle type recognition, 98.5% for license plate detection, and
98.3% for license plate reading is achieved by YOLOv4, while its lighter
version, i.e., Tiny YOLOv4 obtained a mAP of 97.1%, 97.4%, and 93.7% on vehicle
type recognition, license plate detection, and license plate reading,
respectively. The dataset and the training codes are available at
https://github.com/usama-x930/VT-LPR