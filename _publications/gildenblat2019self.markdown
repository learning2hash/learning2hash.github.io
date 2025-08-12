---
layout: publication
title: Self-supervised Similarity Learning For Digital Pathology
authors: Jacob Gildenblat, Eldad Klaiman
conference: Arxiv
year: 2019
bibkey: gildenblat2019self
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.08139'}]
tags: ["Self-Supervised"]
short_authors: Jacob Gildenblat, Eldad Klaiman
---
Using features extracted from networks pretrained on ImageNet is a common
practice in applications of deep learning for digital pathology. However it
presents the downside of missing domain specific image information. In digital
pathology, supervised training data is expensive and difficult to collect. We
propose a self-supervised method for feature extraction by similarity learning
on whole slide images (WSI) that is simple to implement and allows creation of
robust and compact image descriptors. We train a siamese network, exploiting
image spatial continuity and assuming spatially adjacent tiles in the image are
more similar to each other than distant tiles. Our network outputs feature
vectors of length 128, which allows dramatically lower memory storage and
faster processing than networks pretrained on ImageNet. We apply the method on
digital pathology WSIs from the Camelyon16 train set and assess and compare our
method by measuring image retrieval of tumor tiles and descriptor pair distance
ratio for distant/near tiles in the Camelyon16 test set. We show that our
method yields better retrieval task results than existing ImageNet based and
generic self-supervised feature extraction methods. To the best of our
knowledge, this is also the first published method for self-supervised learning
tailored for digital pathology.