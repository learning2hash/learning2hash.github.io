---
layout: publication
title: Cross-domain Image Matching With Deep Feature Maps
authors: Bailey Kong, James Supancic, Deva Ramanan, Charless C. Fowlkes
conference: Arxiv
year: 2018
citations: 36
bibkey: kong2018cross
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.02367'}]
tags: [Applications, ANN Search, Evaluation Metrics]
---
We investigate the problem of automatically determining what type of shoe
left an impression found at a crime scene. This recognition problem is made
difficult by the variability in types of crime scene evidence (ranging from
traces of dust or oil on hard surfaces to impressions made in soil) and the
lack of comprehensive databases of shoe outsole tread patterns. We find that
mid-level features extracted by pre-trained convolutional neural nets are
surprisingly effective descriptors for this specialized domains. However, the
choice of similarity measure for matching exemplars to a query image is
essential to good performance. For matching multi-channel deep features, we
propose the use of multi-channel normalized cross-correlation and analyze its
effectiveness. Our proposed metric significantly improves performance in
matching crime scene shoeprints to laboratory test impressions. We also show
its effectiveness in other cross-domain image retrieval problems: matching
facade images to segmentation labels and aerial photos to map images. Finally,
we introduce a discriminatively trained variant and fine-tune our system
through our proposed metric, obtaining state-of-the-art performance.