---
layout: publication
title: Scene Text Retrieval Via Joint Text Detection And Similarity Learning
authors: Wang Hao, Bai Xiang, Yang Mingkun, Zhu Shenggao, Wang Jing, Liu Wenyu
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: wang2021scene
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.01552'}]
tags: ["CVPR", "Datasets", "Evaluation", "Text Retrieval"]
short_authors: Wang et al.
---
Scene text retrieval aims to localize and search all text instances from an
image gallery, which are the same or similar to a given query text. Such a task
is usually realized by matching a query text to the recognized words, outputted
by an end-to-end scene text spotter. In this paper, we address this problem by
directly learning a cross-modal similarity between a query text and each text
instance from natural images. Specifically, we establish an end-to-end
trainable network, jointly optimizing the procedures of scene text detection
and cross-modal similarity learning. In this way, scene text retrieval can be
simply performed by ranking the detected text instances with the learned
similarity. Experiments on three benchmark datasets demonstrate our method
consistently outperforms the state-of-the-art scene text spotting/retrieval
approaches. In particular, the proposed framework of joint detection and
similarity learning achieves significantly better performance than separated
methods. Code is available at: https://github.com/lanfeng4659/STR-TDSL.