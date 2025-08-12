---
layout: publication
title: Improving Visual Relationship Detection Using Semantic Modeling Of Scene Descriptions
authors: Stephan Baier, Yunpu Ma, Volker Tresp
conference: Lecture Notes in Computer Science
year: 2017
bibkey: baier2017improving
citations: 54
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.00204'}]
tags: ["Datasets", "Evaluation"]
short_authors: Stephan Baier, Yunpu Ma, Volker Tresp
---
Structured scene descriptions of images are useful for the automatic
processing and querying of large image databases. We show how the combination
of a semantic and a visual statistical model can improve on the task of mapping
images to their associated scene description. In this paper we consider scene
descriptions which are represented as a set of triples (subject, predicate,
object), where each triple consists of a pair of visual objects, which appear
in the image, and the relationship between them (e.g. man-riding-elephant,
man-wearing-hat). We combine a standard visual model for object detection,
based on convolutional neural networks, with a latent variable model for link
prediction. We apply multiple state-of-the-art link prediction methods and
compare their capability for visual relationship detection. One of the main
advantages of link prediction methods is that they can also generalize to
triples, which have never been observed in the training data. Our experimental
results on the recently published Stanford Visual Relationship dataset, a
challenging real world dataset, show that the integration of a semantic model
using link prediction methods can significantly improve the results for visual
relationship detection. Our combined approach achieves superior performance
compared to the state-of-the-art method from the Stanford computer vision
group.