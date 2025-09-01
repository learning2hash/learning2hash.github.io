---
layout: publication
title: 'Tattoo Image Search At Scale: Joint Detection And Compact Representation Learning'
authors: Hu Han, Jie Li, Anil K. Jain, Shiguang Shan, Xilin Chen
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2019
bibkey: han2018tattoo
citations: 45
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.00218'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Han et al.
---
The explosive growth of digital images in video surveillance and social media
has led to the significant need for efficient search of persons of interest in
law enforcement and forensic applications. Despite tremendous progress in
primary biometric traits (e.g., face and fingerprint) based person
identification, a single biometric trait alone cannot meet the desired
recognition accuracy in forensic scenarios. Tattoos, as one of the important
soft biometric traits, have been found to be valuable for assisting in person
identification. However, tattoo search in a large collection of unconstrained
images remains a difficult problem, and existing tattoo search methods mainly
focus on matching cropped tattoos, which is different from real application
scenarios. To close the gap, we propose an efficient tattoo search approach
that is able to learn tattoo detection and compact representation jointly in a
single convolutional neural network (CNN) via multi-task learning. While the
features in the backbone network are shared by both tattoo detection and
compact representation learning, individual latent layers of each sub-network
optimize the shared features toward the detection and feature learning tasks,
respectively. We resolve the small batch size issue inside the joint tattoo
detection and compact representation learning network via random image stitch
and preceding feature buffering. We evaluate the proposed tattoo search system
using multiple public-domain tattoo benchmarks, and a gallery set with about
300K distracter tattoo images compiled from these datasets and images from the
Internet. In addition, we also introduce a tattoo sketch dataset containing 300
tattoos for sketch-based tattoo search. Experimental results show that the
proposed approach has superior performance in tattoo detection and tattoo
search at scale compared to several state-of-the-art tattoo retrieval
algorithms.