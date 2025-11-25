---
layout: publication
title: Unsupervised Dense Retrieval Training With Web Anchors
authors: Yiqing Xie, Xiao Liu, Chenyan Xiong
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: xie2023unsupervised
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Veronicium/AnchorDR'}, {
    name: Paper, url: 'https://arxiv.org/abs/2305.05834'}]
tags: ["SIGIR", "Unsupervised"]
short_authors: Yiqing Xie, Xiao Liu, Chenyan Xiong
---
In this work, we present an unsupervised retrieval method with contrastive
learning on web anchors. The anchor text describes the content that is
referenced from the linked page. This shows similarities to search queries that
aim to retrieve pertinent information from relevant documents. Based on their
commonalities, we train an unsupervised dense retriever, Anchor-DR, with a
contrastive learning task that matches the anchor text and the linked document.
To filter out uninformative anchors (such as ``homepage'' or other functional
anchors), we present a novel filtering technique to only select anchors that
contain similar types of information as search queries. Experiments show that
Anchor-DR outperforms state-of-the-art methods on unsupervised dense retrieval
by a large margin (e.g., by 5.3% NDCG@10 on MSMARCO). The gain of our method is
especially significant for search and question answering tasks. Our analysis
further reveals that the pattern of anchor-document pairs is similar to that of
search query-document pairs. Code available at
https://github.com/Veronicium/AnchorDR.