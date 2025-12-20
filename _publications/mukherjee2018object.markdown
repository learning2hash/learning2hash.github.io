---
layout: publication
title: Object Cosegmentation Using Deep Siamese Network
authors: Prerana Mukherjee, Brejesh Lall, Snehith Lattupally
conference: Arxiv
year: 2018
bibkey: mukherjee2018object
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.02555'}]
tags: ["Evaluation", "Neural Hashing", "Supervised", "Tools & Libraries"]
short_authors: Prerana Mukherjee, Brejesh Lall, Snehith Lattupally
---
Object cosegmentation addresses the problem of discovering similar objects
from multiple images and segmenting them as foreground simultaneously. In this
paper, we propose a novel end-to-end pipeline to segment the similar objects
simultaneously from relevant set of images using supervised learning via
deep-learning framework. We experiment with multiple set of object proposal
generation techniques and perform extensive numerical evaluations by training
the Siamese network with generated object proposals. Similar objects proposals
for the test images are retrieved using the ANNOY (Approximate Nearest
Neighbor) library and deep semantic segmentation is performed on them. Finally,
we form a collage from the segmented similar objects based on the relative
importance of the objects.