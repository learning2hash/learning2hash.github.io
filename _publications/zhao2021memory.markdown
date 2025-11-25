---
layout: publication
title: Memory Enhanced Embedding Learning For Cross-modal Video-text Retrieval
authors: Rui Zhao, Kecheng Zheng, Zheng-Jun Zha, Hongtao Xie, Jiebo Luo
conference: Arxiv
year: 2021
bibkey: zhao2021memory
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.15686'}]
tags: ["Evaluation", "Multimodal Retrieval", "Text Retrieval", "Video Retrieval"]
short_authors: Zhao et al.
---
Cross-modal video-text retrieval, a challenging task in the field of vision
and language, aims at retrieving corresponding instance giving sample from
either modality. Existing approaches for this task all focus on how to design
encoding model through a hard negative ranking loss, leaving two key problems
unaddressed during this procedure. First, in the training stage, only a
mini-batch of instance pairs is available in each iteration. Therefore, this
kind of hard negatives is locally mined inside a mini-batch while ignoring the
global negative samples among the dataset. Second, there are many text
descriptions for one video and each text only describes certain local features
of a video. Previous works for this task did not consider to fuse the multiply
texts corresponding to a video during the training. In this paper, to solve the
above two problems, we propose a novel memory enhanced embedding learning
(MEEL) method for videotext retrieval. To be specific, we construct two kinds
of memory banks respectively: cross-modal memory module and text center memory
module. The cross-modal memory module is employed to record the instance
embeddings of all the datasets for global negative mining. To avoid the fast
evolving of the embedding in the memory bank during training, we utilize a
momentum encoder to update the features by a moving-averaging strategy. The
text center memory module is designed to record the center information of the
multiple textual instances corresponding to a video, and aims at bridging these
textual instances together. Extensive experimental results on two challenging
benchmarks, i.e., MSR-VTT and VATEX, demonstrate the effectiveness of the
proposed method.