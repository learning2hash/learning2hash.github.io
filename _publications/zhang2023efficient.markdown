---
layout: publication
title: 'Efficient Retrieval Of Images With Irregular Patterns Using Morphological Image Analysis: Applications To Industrial And Healthcare Datasets'
authors: Jiajun Zhang, Georgina Cosma, Sarah Bugby, Jason Watkins
conference: "Arxiv"
year: 2023
citations: 1
bibkey: zhang2023efficient
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2310.06566'}
tags: ['Cross-Modal', 'Deep', 'Independent', 'Retrieval Models', 'Datasets', 'Applications']
---
Image retrieval is the process of searching and retrieving images from a
database based on their visual content and features. Recently, much attention
has been directed towards the retrieval of irregular patterns within industrial
or medical images by extracting features from the images, such as deep
features, colour-based features, shape-based features and local features. This
has applications across a spectrum of industries, including fault inspection,
disease diagnosis, and maintenance prediction. This paper proposes an image
retrieval framework to search for images containing similar irregular patterns
by extracting a set of morphological features (DefChars) from images; the
datasets employed in this paper contain wind turbine blade images with defects,
chest computerised tomography scans with COVID-19 infection, heatsink images
with defects, and lake ice images. The proposed framework was evaluated with
different feature extraction methods (DefChars, resized raw image, local binary
pattern, and scale-invariant feature transforms) and distance metrics to
determine the most efficient parameters in terms of retrieval performance
across datasets. The retrieval results show that the proposed framework using
the DefChars and the Manhattan distance metric achieves a mean average
precision of 80% and a low standard deviation of 0.09 across classes of
irregular patterns, outperforming alternative feature-metric combinations
across all datasets. Furthermore, the low standard deviation between each class
highlights DefChars' capability for a reliable image retrieval task, even in
the presence of class imbalances or small-sized datasets.
