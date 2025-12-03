---
layout: publication
title: Estimating And Abstracting The 3D Structure Of Bones Using Neural Networks
  On X-ray (2D) Images
authors: "Jana \u010Cavojsk\xE1, Julian Petrasch, Nicolas J. Lehmann, Agn\xE8s Voisard,\
  \ Peter B\xF6ttcher"
conference: Communications biology 2020 3(1) pp.1-13
year: 2020
bibkey: "\u010Davojsk\xE12020estimating"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.11499'}]
tags: ["Distance Metric Learning", "Neural Hashing"]
short_authors: "\u010Cavojsk\xE1 et al."
---
In this paper, we present a deep-learning based method for estimating the 3D
structure of a bone from a pair of 2D X-ray images. Our triplet loss-trained
neural network selects the most closely matching 3D bone shape from a
predefined set of shapes. Our predictions have an average root mean square
(RMS) distance of 1.08 mm between the predicted and true shapes, making it more
accurate than the average error achieved by eight other examined 3D bone
reconstruction approaches. The prediction process that we use is fully
automated and unlike many competing approaches, it does not rely on any
previous knowledge about bone geometry. Additionally, our neural network can
determine the identity of a bone based only on its X-ray image. It computes a
low-dimensional representation ("embedding") of each 2D X-ray image and
henceforth compares different X-ray images based only on their embeddings. An
embedding holds enough information to uniquely identify the bone CT belonging
to the input X-ray image with a 100% accuracy and can therefore serve as a kind
of fingerprint for that bone. Possible applications include faster, image
content-based bone database searches for forensic purposes.