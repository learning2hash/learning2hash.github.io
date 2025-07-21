---
layout: publication
title: 'SEA: Sentence Encoder Assembly For Video Retrieval By Textual Queries'
authors: Li et al.
conference: IEEE Transactions on Multimedia
year: 2020
bibkey: li2020sea
citations: 51
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.12091'}]
tags: ["Video Retrieval"]
---
Retrieving unlabeled videos by textual queries, known as Ad-hoc Video Search
(AVS), is a core theme in multimedia data management and retrieval. The success
of AVS counts on cross-modal representation learning that encodes both query
sentences and videos into common spaces for semantic similarity computation.
Inspired by the initial success of previously few works in combining multiple
sentence encoders, this paper takes a step forward by developing a new and
general method for effectively exploiting diverse sentence encoders. The
novelty of the proposed method, which we term Sentence Encoder Assembly (SEA),
is two-fold. First, different from prior art that use only a single common
space, SEA supports text-video matching in multiple encoder-specific common
spaces. Such a property prevents the matching from being dominated by a
specific encoder that produces an encoding vector much longer than other
encoders. Second, in order to explore complementarities among the individual
common spaces, we propose multi-space multi-loss learning. As extensive
experiments on four benchmarks (MSR-VTT, TRECVID AVS 2016-2019, TGIF and MSVD)
show, SEA surpasses the state-of-the-art. In addition, SEA is extremely ease to
implement. All this makes SEA an appealing solution for AVS and promising for
continuously advancing the task by harvesting new sentence encoders.