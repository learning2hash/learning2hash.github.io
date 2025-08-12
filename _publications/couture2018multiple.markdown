---
layout: publication
title: 'Multiple Instance Learning For Heterogeneous Images: Training A CNN For Histopathology'
authors: Heather D. Couture, J. S. Marron, Charles M. Perou, Melissa A. Troester,
  Marc Niethammer
conference: Lecture Notes in Computer Science
year: 2018
bibkey: couture2018multiple
citations: 58
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.05083'}]
tags: []
short_authors: Couture et al.
---
Multiple instance (MI) learning with a convolutional neural network enables
end-to-end training in the presence of weak image-level labels. We propose a
new method for aggregating predictions from smaller regions of the image into
an image-level classification by using the quantile function. The quantile
function provides a more complete description of the heterogeneity within each
image, improving image-level classification. We also adapt image augmentation
to the MI framework by randomly selecting cropped regions on which to apply MI
aggregation during each epoch of training. This provides a mechanism to study
the importance of MI learning. We validate our method on five different
classification tasks for breast tumor histology and provide a visualization
method for interpreting local image classifications that could lead to future
insights into tumor heterogeneity.