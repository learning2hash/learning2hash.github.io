---
layout: publication
title: Real-time Embedded Person Detection And Tracking For Shopping Behaviour Analysis
authors: "Robin Schrijvers, Steven Puttemans, Timothy Callemein, Toon Goedem\xE9"
conference: Lecture Notes in Computer Science
year: 2020
bibkey: schrijvers2020real
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.04942'}]
tags: ["Efficiency"]
short_authors: Schrijvers et al.
---
Shopping behaviour analysis through counting and tracking of people in
shop-like environments offers valuable information for store operators and
provides key insights in the stores layout (e.g. frequently visited spots).
Instead of using extra staff for this, automated on-premise solutions are
preferred. These automated systems should be cost-effective, preferably on
lightweight embedded hardware, work in very challenging situations (e.g.
handling occlusions) and preferably work real-time. We solve this challenge by
implementing a real-time TensorRT optimized YOLOv3-based pedestrian detector,
on a Jetson TX2 hardware platform. By combining the detector with a sparse
optical flow tracker we assign a unique ID to each customer and tackle the
problem of loosing partially occluded customers. Our detector-tracker based
solution achieves an average precision of 81.59% at a processing speed of 10
FPS. Besides valuable statistics, heat maps of frequently visited spots are
extracted and used as an overlay on the video stream.