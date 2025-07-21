---
layout: publication
title: 'Simpledoc: Multi-modal Document Understanding With Dual-cue Page Retrieval
  And Iterative Refinement'
authors: Jain et al.
conference: 2013 12th International Conference on Document Analysis and Recognition
year: 2025
bibkey: jain2025simpledoc
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.14035'}]
---
Document Visual Question Answering (DocVQA) is a practical yet challenging task, which is to ask questions based on documents while referring to multiple pages and different modalities of information, e.g, images and tables. To handle multi-modality, recent methods follow a similar Retrieval Augmented Generation (RAG) pipeline, but utilize Visual Language Models (VLMs) based embedding model to embed and retrieve relevant pages as images, and generate answers with VLMs that can accept an image as input. In this paper, we introduce SimpleDoc, a lightweight yet powerful retrieval - augmented framework for DocVQA. It boosts evidence page gathering by first retrieving candidates through embedding similarity and then filtering and re-ranking these candidates based on page summaries. A single VLM-based reasoner agent repeatedly invokes this dual-cue retriever, iteratively pulling fresh pages into a working memory until the question is confidently answered. SimpleDoc outperforms previous baselines by 3.2% on average on 4 DocVQA datasets with much fewer pages retrieved. Our code is available at https://github.com/ag2ai/SimpleDoc.