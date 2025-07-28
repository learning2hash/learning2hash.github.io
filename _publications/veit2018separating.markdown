---
layout: publication
title: Separating Self-expression And Visual Content In Hashtag Supervision
authors: Andreas Veit, Maximilian Nickel, Serge Belongie, Laurens van Der Maaten
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: veit2018separating
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.09825'}]
tags: ["CVPR"]
short_authors: Veit et al.
---
The variety, abundance, and structured nature of hashtags make them an
interesting data source for training vision models. For instance, hashtags have
the potential to significantly reduce the problem of manual supervision and
annotation when learning vision models for a large number of concepts. However,
a key challenge when learning from hashtags is that they are inherently
subjective because they are provided by users as a form of self-expression. As
a consequence, hashtags may have synonyms (different hashtags referring to the
same visual content) and may be ambiguous (the same hashtag referring to
different visual content). These challenges limit the effectiveness of
approaches that simply treat hashtags as image-label pairs. This paper presents
an approach that extends upon modeling simple image-label pairs by modeling the
joint distribution of images, hashtags, and users. We demonstrate the efficacy
of such approaches in image tagging and retrieval experiments, and show how the
joint model can be used to perform user-conditional retrieval and tagging.