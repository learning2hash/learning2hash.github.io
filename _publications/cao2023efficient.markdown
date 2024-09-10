---
layout: publication
title: Efficient Image-Text Retrieval via Keyword-Guided Pre-Screening
authors: Cao Min, Bai Yang, Wang Jingyao, Cao Ziqiang, Nie Liqiang, Zhang Min
conference: "Arxiv"
year: 2023
bibkey: cao2023efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2303.07740"}
tags: ['ARXIV', 'Cross Modal', 'Text Retrieval']
---
Under the flourishing development in performance current image-text retrieval methods suffer from N-related time complexity which hinders their application in practice. Targeting at efficiency improvement this paper presents a simple and effective keyword-guided pre-screening framework for the image-text retrieval. Specifically we convert the image and text data into the keywords and perform the keyword matching across modalities to exclude a large number of irrelevant gallery samples prior to the retrieval network. For the keyword prediction we transfer it into a multi-label classification problem and propose a multi-task learning scheme by appending the multi-label classifiers to the image-text retrieval network to achieve a lightweight and high-performance keyword prediction. For the keyword matching we introduce the inverted index in the search engine and create a win-win situation on both time and space complexities for the pre-screening. Extensive experiments on two widely-used datasets i.e. Flickr30K and MS-COCO verify the effectiveness of the proposed framework. The proposed framework equipped with only two embedding layers achieves O(1) querying time complexity while improving the retrieval efficiency and keeping its performance when applied prior to the common image-text retrieval methods. Our code will be released.
