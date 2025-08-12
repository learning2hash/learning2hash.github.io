---
layout: publication
title: An Empirical Analysis Of Visual Features For Multiple Object Tracking In Urban
  Scenes
authors: Mehdi Miah, Justine Pepin, Nicolas Saunier, Guillaume-alexandre Bilodeau
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: miah2020empirical
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.07881'}]
tags: []
short_authors: Miah et al.
---
This paper addresses the problem of selecting appearance features for
multiple object tracking (MOT) in urban scenes. Over the years, a large number
of features has been used for MOT. However, it is not clear whether some of
them are better than others. Commonly used features are color histograms,
histograms of oriented gradients, deep features from convolutional neural
networks and re-identification (ReID) features. In this study, we assess how
good these features are at discriminating objects enclosed by a bounding box in
urban scene tracking scenarios. Several affinity measures, namely the
\\(\mathrm\{L\}_1\\), \\(\mathrm\{L\}_2\\) and the Bhattacharyya distances, Rank-1 counts
and the cosine similarity, are also assessed for their impact on the
discriminative power of the features. Results on several datasets show that
features from ReID networks are the best for discriminating instances from one
another regardless of the quality of the detector. If a ReID model is not
available, color histograms may be selected if the detector has a good recall
and there are few occlusions; otherwise, deep features are more robust to
detectors with lower recall. The project page is
http://www.mehdimiah.com/visual_features.