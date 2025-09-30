---
layout: publication
title: 'Learning Local Descriptors By Optimizing The Keypoint-correspondence Criterion:
  Applications To Face Matching, Learning From Unlabeled Videos And 3d-shape Retrieval'
authors: "Nenad Marku\u0161, Igor S. Pand\u017Ei\u0107, J\xF6rgen Ahlberg"
conference: IEEE Transactions on Image Processing
year: 2019
bibkey: "marku\u01612019learning"
citations: 12
additional_links: [{name: Code, url: 'https://github.com/nenadmarkus/wlrn'}, {name: Paper,
    url: 'https://arxiv.org/abs/1603.09095'}]
tags: ["Datasets"]
short_authors: "Nenad Marku\u0161, Igor S. Pand\u017Ei\u0107, J\xF6rgen Ahlberg"
---
Current best local descriptors are learned on a large dataset of matching and
non-matching keypoint pairs. However, data of this kind is not always available
since detailed keypoint correspondences can be hard to establish. On the other
hand, we can often obtain labels for pairs of keypoint bags. For example,
keypoint bags extracted from two images of the same object under different
views form a matching pair, and keypoint bags extracted from images of
different objects form a non-matching pair. On average, matching pairs should
contain more corresponding keypoints than non-matching pairs. We describe an
end-to-end differentiable architecture that enables the learning of local
keypoint descriptors from such weakly-labeled data. Additionally, we discuss
how to improve the method by incorporating the procedure of mining hard
negatives. We also show how can our approach be used to learn convolutional
features from unlabeled video signals and 3D models.
  Our implementation is available at https://github.com/nenadmarkus/wlrn