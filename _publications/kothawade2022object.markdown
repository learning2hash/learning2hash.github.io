---
layout: publication
title: Object-level Targeted Selection Via Deep Template Matching
authors: Suraj Kothawade, Donna Roy, Michele Fenzi, Elmar Haussmann, Jose M. Alvarez,
  Christoph Angerer
conference: 2022 IEEE Intelligent Vehicles Symposium (IV)
year: 2022
bibkey: kothawade2022object
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.01778'}]
tags: [Scalability, Image Retrieval, Evaluation, Datasets]
short_authors: Kothawade et al.
---
Retrieving images with objects that are semantically similar to objects of
interest (OOI) in a query image has many practical use cases. A few examples
include fixing failures like false negatives/positives of a learned model or
mitigating class imbalance in a dataset. The targeted selection task requires
finding the relevant data from a large-scale pool of unlabeled data. Manual
mining at this scale is infeasible. Further, the OOI are often small and occupy
less than 1% of image area, are occluded, and co-exist with many semantically
different objects in cluttered scenes. Existing semantic image retrieval
methods often focus on mining for larger sized geographical landmarks, and/or
require extra labeled data, such as images/image-pairs with similar objects,
for mining images with generic objects. We propose a fast and robust template
matching algorithm in the DNN feature space, that retrieves semantically
similar images at the object-level from a large unlabeled pool of data. We
project the region(s) around the OOI in the query image to the DNN feature
space for use as the template. This enables our method to focus on the
semantics of the OOI without requiring extra labeled data. In the context of
autonomous driving, we evaluate our system for targeted selection by using
failure cases of object detectors as OOI. We demonstrate its efficacy on a
large unlabeled dataset with 2.2M images and show high recall in mining for
images with small-sized OOI. We compare our method against a well-known
semantic image retrieval method, which also does not require extra labeled
data. Lastly, we show that our method is flexible and retrieves images with one
or more semantically different co-occurring OOI seamlessly.