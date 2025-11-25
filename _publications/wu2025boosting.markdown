---
layout: publication
title: Boosting Text-to-chart Retrieval Through Training With Synthesized Semantic
  Insights
authors: Yifan Wu, Lutao Yan, Yizhang Zhu, Yinan Mei, Jiannan Wang, Nan Tang, Yuyu
  Luo
conference: Arxiv
year: 2025
bibkey: wu2025boosting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.10043'}]
tags: ["Datasets", "Evaluation"]
short_authors: Wu et al.
---
Charts are crucial for data analysis and decision-making.Text-to-chart retrieval systems have become increasingly important for Business Intelligence (BI), where users need to find relevant charts that match their analytical needs. These needs can be categorized into precise queries that are well-specified and fuzzy queries that are more exploratory -- both require understanding the semantics and context of the charts. However, existing text-to-chart retrieval solutions often fail to capture the semantic content and contextual information of charts, primarily due to the lack of comprehensive metadata (or semantic insights). To address this limitation, we propose a training data development pipeline that automatically synthesizes hierarchical semantic insights for charts, covering visual patterns (visual-oriented), statistical properties (statistics-oriented), and practical applications (task-oriented), which produces 207,498 semantic insights for 69,166 charts. Based on these, we train a CLIP-based model named ChartFinder to learn better representations of charts for text-to-chart retrieval. Our method leverages rich semantic insights during the training phase to develop a model that understands both visual and semantic aspects of charts.To evaluate text-to-chart retrieval performance, we curate the first benchmark, CRBench, for this task with 21,862 charts and 326 text queries from real-world BI applications, with ground-truth labels verified by the crowd workers.Experiments show that ChartFinder significantly outperforms existing methods in text-to-chart retrieval tasks across various settings. For precise queries, ChartFinder achieves up to 66.9% NDCG@10, which is 11.58% higher than state-of-the-art models. In fuzzy query tasks, our method also demonstrates consistent improvements, with an average increase of 5% across nearly all metrics.