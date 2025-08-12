---
layout: publication
title: Monocular Camera Based Fruit Counting And Mapping With Semantic Data Association
authors: Xu Liu, Steven W. Chen, Chenhao Liu, Shreyas S. Shivakumar, Jnaneshwar Das,
  Camillo J. Taylor, James Underwood, Vijay Kumar
conference: IEEE Robotics and Automation Letters
year: 2019
bibkey: liu2018monocular
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.01417'}]
tags: ["Datasets", "Evaluation"]
short_authors: Liu et al.
---
We present a cheap, lightweight, and fast fruit counting pipeline that uses a
single monocular camera. Our pipeline that relies only on a monocular camera,
achieves counting performance comparable to state-of-the-art fruit counting
system that utilizes an expensive sensor suite including LiDAR and GPS/INS on a
mango dataset. Our monocular camera pipeline begins with a fruit detection
component that uses a deep neural network. It then uses semantic structure from
motion (SFM) to convert these detections into fruit counts by estimating
landmark locations of the fruit in 3D, and using these landmarks to identify
double counting scenarios. There are many benefits of developing a low cost and
lightweight fruit counting system, including applicability to agriculture in
developing countries, where monetary constraints or unstructured environments
necessitate cheaper hardware solutions.