---
layout: publication
title: 'Stochastic Learning Of Multi-instance Dictionary For Earth Mover''s Distance Based Histogram Comparison'
authors: Jihong Fan, Ru-ze Liang
conference: "Arxiv"
year: 2016
citations: 11
bibkey: fan2016stochastic
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1609.00817'}
tags: ['Tools and Libraries', 'Evaluation Metrics', 'Loss Functions', 'Applications']
---
Dictionary plays an important role in multi-instance data representation. It
maps bags of instances to histograms. Earth mover's distance (EMD) is the most
effective histogram distance metric for the application of multi-instance
retrieval. However, up to now, there is no existing multi-instance dictionary
learning methods designed for EMD based histogram comparison. To fill this gap,
we develop the first EMD-optimal dictionary learning method using stochastic
optimization method. In the stochastic learning framework, we have one triplet
of bags, including one basic bag, one positive bag, and one negative bag. These
bags are mapped to histograms using a multi-instance dictionary. We argue that
the EMD between the basic histogram and the positive histogram should be
smaller than that between the basic histogram and the negative histogram. Base
on this condition, we design a hinge loss. By minimizing this hinge loss and
some regularization terms of the dictionary, we update the dictionary
instances. The experiments over multi-instance retrieval applications shows its
effectiveness when compared to other dictionary learning methods over the
problems of medical image retrieval and natural language relation
classification.
