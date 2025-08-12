---
layout: publication
title: An Entropy-based Text Watermarking Detection Method
authors: Yijian Lu, Aiwei Liu, Dianzhi Yu, Jingjing Li, Irwin King
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: lu2024entropy
citations: 2
additional_links: [{name: Code, url: 'https://github.com/luyijian3/EWD\'}, {name: Code,
    url: 'https://github.com/THU-BPM/MarkLLM\'}, {name: Paper, url: 'https://arxiv.org/abs/2403.13485'}]
tags: ["Evaluation"]
short_authors: Lu et al.
---
Text watermarking algorithms for large language models (LLMs) can effectively
identify machine-generated texts by embedding and detecting hidden features in
the text. Although the current text watermarking algorithms perform well in
most high-entropy scenarios, its performance in low-entropy scenarios still
needs to be improved. In this work, we opine that the influence of token
entropy should be fully considered in the watermark detection process, \(i.e.\),
the weight of each token during watermark detection should be customized
according to its entropy, rather than setting the weights of all tokens to the
same value as in previous methods. Specifically, we propose
\textbf\{E\}ntropy-based Text \textbf\{W\}atermarking \textbf\{D\}etection
(\textbf\{EWD\}) that gives higher-entropy tokens higher influence weights during
watermark detection, so as to better reflect the degree of watermarking.
Furthermore, the proposed detection process is training-free and fully
automated. From the experiments, we demonstrate that our EWD can achieve better
detection performance in low-entropy scenarios, and our method is also general
and can be applied to texts with different entropy distributions. Our code and
data is available\footnote\{https://github.com/luyijian3/EWD\}.
Additionally, our algorithm could be accessed through MarkLLM
\cite\{pan2024markllm\}\footnote\{https://github.com/THU-BPM/MarkLLM\}.