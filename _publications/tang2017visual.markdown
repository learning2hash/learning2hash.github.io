---
layout: publication
title: Visual And Semantic Knowledge Transfer For Large Scale Semi-supervised Object
  Detection
authors: Yuxing Tang, Josiah Wang, Xiaofang Wang, Boyang Gao, Emmanuel Dellandrea,
  Robert Gaizauskas, Liming Chen
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2017
bibkey: tang2017visual
citations: 67
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.03145'}]
tags: ["Scalability"]
short_authors: Tang et al.
---
Deep CNN-based object detection systems have achieved remarkable success on
several large-scale object detection benchmarks. However, training such
detectors requires a large number of labeled bounding boxes, which are more
difficult to obtain than image-level annotations. Previous work addresses this
issue by transforming image-level classifiers into object detectors. This is
done by modeling the differences between the two on categories with both
image-level and bounding box annotations, and transferring this information to
convert classifiers to detectors for categories without bounding box
annotations. We improve this previous work by incorporating knowledge about
object similarities from visual and semantic domains during the transfer
process. The intuition behind our proposed method is that visually and
semantically similar categories should exhibit more common transferable
properties than dissimilar categories, e.g. a better detector would result by
transforming the differences between a dog classifier and a dog detector onto
the cat class, than would by transforming from the violin class. Experimental
results on the challenging ILSVRC2013 detection dataset demonstrate that each
of our proposed object similarity based knowledge transfer methods outperforms
the baseline methods. We found strong evidence that visual similarity and
semantic relatedness are complementary for the task, and when combined notably
improve detection, achieving state-of-the-art detection performance in a
semi-supervised setting.