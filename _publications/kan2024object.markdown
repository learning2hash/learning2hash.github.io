---
layout: publication
title: Object Retrieval For Visual Question Answering With Outside Knowledge
authors: Shichao Kan, Yuhai Deng, Jiale Fu, Lihui Cen, Zhe Qu, Linna Zhang, Yixiong
  Liang, Yigang Cen
conference: Arxiv
year: 2024
bibkey: kan2024object
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.10798'}]
tags: [Evaluation, Supervised, Image Retrieval, Datasets, Unsupervised]
short_authors: Kan et al.
---
Retrieval-augmented generation (RAG) with large language models (LLMs) plays a crucial role in question answering, as LLMs possess limited knowledge and are not updated with continuously growing information. Most recent work on RAG has focused primarily on text-based or large-image retrieval, which constrains the broader application of RAG models. We recognize that object-level retrieval is essential for addressing questions that extend beyond image content. To tackle this issue, we propose a task of object retrieval for visual question answering with outside knowledge (OR-OK-VQA), aimed to extend image-based content understanding in conjunction with LLMs. A key challenge in this task is retrieving diverse objects-related images that contribute to answering the questions. To enable accurate and robust general object retrieval, it is necessary to learn embeddings for local objects. This paper introduces a novel unsupervised deep feature embedding technique called multi-scale group collaborative embedding learning (MS-GCEL), developed to learn embeddings for long-tailed objects at different scales. Additionally, we establish an OK-VQA evaluation benchmark using images from the BelgaLogos, Visual Genome, and LVIS datasets. Prior to the OK-VQA evaluation, we construct a benchmark of challenges utilizing objects extracted from the COCO 2017 and VOC 2007 datasets to support the training and evaluation of general object retrieval models. Our evaluations on both general object retrieval and OK-VQA demonstrate the effectiveness of the proposed approach. The code and dataset will be publicly released for future research.