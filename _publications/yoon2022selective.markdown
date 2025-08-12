---
layout: publication
title: Selective Query-guided Debiasing For Video Corpus Moment Retrieval
authors: Sunjae Yoon, Ji Woo Hong, Eunseop Yoon, Dahyun Kim, Junyeong Kim, Hee Suk
  Yoon, Chang D. Yoo
conference: Lecture Notes in Computer Science
year: 2022
bibkey: yoon2022selective
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.08714'}]
tags: ["Multimodal Retrieval", "Video Retrieval"]
short_authors: Yoon et al.
---
Video moment retrieval (VMR) aims to localize target moments in untrimmed
videos pertinent to a given textual query. Existing retrieval systems tend to
rely on retrieval bias as a shortcut and thus, fail to sufficiently learn
multi-modal interactions between query and video. This retrieval bias stems
from learning frequent co-occurrence patterns between query and moments, which
spuriously correlate objects (e.g., a pencil) referred in the query with
moments (e.g., scene of writing with a pencil) where the objects frequently
appear in the video, such that they converge into biased moment predictions.
Although recent debiasing methods have focused on removing this retrieval bias,
we argue that these biased predictions sometimes should be preserved because
there are many queries where biased predictions are rather helpful. To
conjugate this retrieval bias, we propose a Selective Query-guided Debiasing
network (SQuiDNet), which incorporates the following two main properties: (1)
Biased Moment Retrieval that intentionally uncovers the biased moments inherent
in objects of the query and (2) Selective Query-guided Debiasing that performs
selective debiasing guided by the meaning of the query. Our experimental
results on three moment retrieval benchmarks (i.e., TVR, ActivityNet, DiDeMo)
show the effectiveness of SQuiDNet and qualitative analysis shows improved
interpretability.