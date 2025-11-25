---
layout: publication
title: Fully-trainable Deep Matching
authors: James Thewlis, Shuai Zheng, Philip H. S. Torr, Andrea Vedaldi
conference: Procedings of the British Machine Vision Conference 2016
year: 2016
bibkey: thewlis2016fully
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.03532'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Thewlis et al.
---
Deep Matching (DM) is a popular high-quality method for quasi-dense image
matching. Despite its name, however, the original DM formulation does not yield
a deep neural network that can be trained end-to-end via backpropagation. In
this paper, we remove this limitation by rewriting the complete DM algorithm as
a convolutional neural network. This results in a novel deep architecture for
image matching that involves a number of new layer types and that, similar to
recent networks for image segmentation, has a U-topology. We demonstrate the
utility of the approach by improving the performance of DM by learning it
end-to-end on an image matching task.