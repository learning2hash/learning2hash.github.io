---
layout: publication
title: Open Set Logo Detection And Retrieval
authors: "Andras T\xFCzk\xF6, Christian Herrmann, Daniel Manger, J\xFCrgen Beyerer"
conference: Proceedings of the 13th International Joint Conference on Computer Vision,
  Imaging and Computer Graphics Theory and Applications
year: 2018
bibkey: "t\xFCzk\xF62017open"
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.10891'}]
tags: []
short_authors: "T\xFCzk\xF6 et al."
---
Current logo retrieval research focuses on closed set scenarios. We argue
that the logo domain is too large for this strategy and requires an open set
approach. To foster research in this direction, a large-scale logo dataset,
called Logos in the Wild, is collected and released to the public. A typical
open set logo retrieval application is, for example, assessing the
effectiveness of advertisement in sports event broadcasts. Given a query sample
in shape of a logo image, the task is to find all further occurrences of this
logo in a set of images or videos. Currently, common logo retrieval approaches
are unsuitable for this task because of their closed world assumption. Thus, an
open set logo retrieval method is proposed in this work which allows searching
for previously unseen logos by a single query sample. A two stage concept with
separate logo detection and comparison is proposed where both modules are based
on task specific CNNs. If trained with the Logos in the Wild data, significant
performance improvements are observed, especially compared with
state-of-the-art closed set approaches.