---
layout: publication
title: 'Uniasm: Binary Code Similarity Detection Without Fine-tuning'
authors: Yeming Gu, Hui Shu, Fei Kang, Fan Hu
conference: Arxiv
year: 2022
bibkey: gu2022uniasm
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.01144'}]
tags: ["Datasets", "Evaluation", "Privacy & Security", "Similarity Search"]
short_authors: Gu et al.
---
Binary code similarity detection (BCSD) is widely used in various binary
analysis tasks such as vulnerability search, malware detection, clone
detection, and patch analysis. Recent studies have shown that the
learning-based binary code embedding models perform better than the traditional
feature-based approaches. However, previous studies have not delved deeply into
the key factors that affect model performance. In this paper, we design
extensive ablation studies to explore these influencing factors. The
experimental results have provided us with many new insights. We have made
innovations in both code representation and model selection: we propose a novel
rich-semantic function representation technique to ensure the model captures
the intricate nuances of binary code, and we introduce the first UniLM-based
binary code embedding model, named UniASM, which includes two newly designed
training tasks to learn representations of binary functions. The experimental
results show that UniASM outperforms the state-of-the-art (SOTA) approaches on
the evaluation datasets. The average scores of Recall@1 on cross-compilers,
cross-optimization-levels, and cross-obfuscations have improved by 12.7%, 8.5%,
and 22.3%, respectively, compared to the best of the baseline methods. Besides,
in the real-world task of known vulnerability search, UniASM outperforms all
the current baselines.