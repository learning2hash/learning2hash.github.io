---
layout: publication
title: 'Deriving Visual Semantics From Spatial Context: An Adaptation Of LSA And Word2vec
  To Generate Object And Scene Embeddings From Images'
authors: Matthias S. Treder, Juan Mayor-torres, Christoph Teufel
conference: Arxiv
year: 2020
bibkey: treder2020deriving
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.09384'}]
tags: []
short_authors: Matthias S. Treder, Juan Mayor-torres, Christoph Teufel
---
Embeddings are an important tool for the representation of word meaning.
Their effectiveness rests on the distributional hypothesis: words that occur in
the same context carry similar semantic information. Here, we adapt this
approach to index visual semantics in images of scenes. To this end, we
formulate a distributional hypothesis for objects and scenes: Scenes that
contain the same objects (object context) are semantically related. Similarly,
objects that appear in the same spatial context (within a scene or subregions
of a scene) are semantically related. We develop two approaches for learning
object and scene embeddings from annotated images. In the first approach, we
adapt LSA and Word2vec's Skipgram and CBOW models to generate two sets of
embeddings from object co-occurrences in whole images, one for objects and one
for scenes. The representational space spanned by these embeddings suggests
that the distributional hypothesis holds for images. In an initial application
of this approach, we show that our image-based embeddings improve scene
classification models such as ResNet18 and VGG-11 (3.72% improvement on Top5
accuracy, 4.56% improvement on Top1 accuracy). In the second approach, rather
than analyzing whole images of scenes, we focus on co-occurrences of objects
within subregions of an image. We illustrate that this method yields a sensible
hierarchical decomposition of a scene into collections of semantically related
objects. Overall, these results suggest that object and scene embeddings from
object co-occurrences and spatial context yield semantically meaningful
representations as well as computational improvements for downstream
applications such as scene classification.