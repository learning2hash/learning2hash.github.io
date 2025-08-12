---
layout: publication
title: Learning Instance Representation Banks For Aerial Scene Classification
authors: Jingjun Yi, Beichen Zhou
conference: Arxiv
year: 2022
bibkey: yi2022learning
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.13744'}]
tags: []
short_authors: Jingjun Yi, Beichen Zhou
---
Aerial scenes are more complicated in terms of object distribution and
spatial arrangement than natural scenes due to the bird view, and thus remain
challenging to learn discriminative scene representation. Recent solutions
design \textit\{local semantic descriptors\} so that region of interests (RoIs)
can be properly highlighted. However, each local descriptor has limited
description capability and the overall scene representation remains to be
refined. In this paper, we solve this problem by designing a novel
representation set named \textit\{instance representation bank\} (IRB), which
unifies multiple local descriptors under the multiple instance learning (MIL)
formulation. This unified framework is not trivial as all the local semantic
descriptors can be aligned to the same scene scheme, enhancing the scene
representation capability. Specifically, our IRB learning framework consists of
a backbone, an instance representation bank, a semantic fusion module and a
scene scheme alignment loss function. All the components are organized in an
end-to-end manner. Extensive experiments on three aerial scene benchmarks
demonstrate that our proposed method outperforms the state-of-the-art
approaches by a large margin.