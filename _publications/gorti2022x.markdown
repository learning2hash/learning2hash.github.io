---
layout: publication
title: 'X-pool: Cross-modal Language-video Attention For Text-video Retrieval'
authors: Satya Krishna Gorti, Noel Vouitsis, Junwei Ma, Keyvan Golestan, Maksims Volkovs,
  Animesh Garg, Guangwei Yu
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: gorti2022x
citations: 170
additional_links: [{name: Code, url: 'https://layer6ai-labs.github.io/xpool/'}, {
    name: Paper, url: 'https://arxiv.org/abs/2203.15086'}]
tags: ["CVPR", "Datasets", "Evaluation", "Multimodal Retrieval", "Video Retrieval"]
short_authors: Gorti et al.
---
In text-video retrieval, the objective is to learn a cross-modal similarity
function between a text and a video that ranks relevant text-video pairs higher
than irrelevant pairs. However, videos inherently express a much wider gamut of
information than texts. Instead, texts often capture sub-regions of entire
videos and are most semantically similar to certain frames within videos.
Therefore, for a given text, a retrieval model should focus on the text's most
semantically similar video sub-regions to make a more relevant comparison. Yet,
most existing works aggregate entire videos without directly considering text.
Common text-agnostic aggregations schemes include mean-pooling or
self-attention over the frames, but these are likely to encode misleading
visual information not described in the given text. To address this, we propose
a cross-modal attention model called X-Pool that reasons between a text and the
frames of a video. Our core mechanism is a scaled dot product attention for a
text to attend to its most semantically similar frames. We then generate an
aggregated video representation conditioned on the text's attention weights
over the frames. We evaluate our method on three benchmark datasets of MSR-VTT,
MSVD and LSMDC, achieving new state-of-the-art results by up to 12% in relative
improvement in Recall@1. Our findings thereby highlight the importance of joint
text-video reasoning to extract important visual cues according to text. Full
code and demo can be found at: https://layer6ai-labs.github.io/xpool/