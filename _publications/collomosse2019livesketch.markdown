---
layout: publication
title: 'Livesketch: Query Perturbations For Guided Sketch-based Visual Search'
authors: Collomosse John, Bui Tu, Jin Hailin
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: collomosse2019livesketch
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.06611'}]
tags: ["Efficiency", "CVPR", "Image-Retrieval"]
short_authors: Collomosse John, Bui Tu, Jin Hailin
---
LiveSketch is a novel algorithm for searching large image collections using
hand-sketched queries. LiveSketch tackles the inherent ambiguity of sketch
search by creating visual suggestions that augment the query as it is drawn,
making query specification an iterative rather than one-shot process that helps
disambiguate users' search intent. Our technical contributions are: a triplet
convnet architecture that incorporates an RNN based variational autoencoder to
search for images using vector (stroke-based) queries; real-time clustering to
identify likely search intents (and so, targets within the search embedding);
and the use of backpropagation from those targets to perturb the input stroke
sequence, so suggesting alterations to the query in order to guide the search.
We show improvements in accuracy and time-to-task over contemporary baselines
using a 67M image corpus.