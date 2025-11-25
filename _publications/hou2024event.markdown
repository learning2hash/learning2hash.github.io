---
layout: publication
title: Event-aware Video Corpus Moment Retrieval
authors: Danyang Hou, Liang Pang, Huawei Shen, Xueqi Cheng
conference: Arxiv
year: 2024
bibkey: hou2024event
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.13566'}]
tags: ["Efficiency", "Video Retrieval"]
short_authors: Hou et al.
---
Video Corpus Moment Retrieval (VCMR) is a practical video retrieval task
focused on identifying a specific moment within a vast corpus of untrimmed
videos using the natural language query. Existing methods for VCMR typically
rely on frame-aware video retrieval, calculating similarities between the query
and video frames to rank videos based on maximum frame similarity.However, this
approach overlooks the semantic structure embedded within the information
between frames, namely, the event, a crucial element for human comprehension of
videos. Motivated by this, we propose EventFormer, a model that explicitly
utilizes events within videos as fundamental units for video retrieval. The
model extracts event representations through event reasoning and hierarchical
event encoding. The event reasoning module groups consecutive and visually
similar frame representations into events, while the hierarchical event
encoding encodes information at both the frame and event levels. We also
introduce anchor multi-head self-attenion to encourage Transformer to capture
the relevance of adjacent content in the video. The training of EventFormer is
conducted by two-branch contrastive learning and dual optimization for two
sub-tasks of VCMR. Extensive experiments on TVR, ANetCaps, and DiDeMo
benchmarks show the effectiveness and efficiency of EventFormer in VCMR,
achieving new state-of-the-art results. Additionally, the effectiveness of
EventFormer is also validated on partially relevant video retrieval task.