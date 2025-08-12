---
layout: publication
title: 'Keenhash: Hashing Programs Into Function-aware Embeddings For Large-scale
  Binary Code Similarity Analysis'
authors: Zhijie Liu, Qiyi Tang, Sen Nie, Shi Wu, Liang Feng Zhang, Yutian Tang
conference: Proceedings of the ACM on Software Engineering
year: 2025
bibkey: liu2025keenhash
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.11612'}]
tags: ["Hashing Methods", "Scalability"]
short_authors: Liu et al.
---
Binary code similarity analysis (BCSA) is a crucial research area in many fields such as cybersecurity. Specifically, function-level diffing tools are the most widely used in BCSA: they perform function matching one by one for evaluating the similarity between binary programs. However, such methods need a high time complexity, making them unscalable in large-scale scenarios (e.g., 1/n-to-n search). Towards effective and efficient program-level BCSA, we propose KEENHash, a novel hashing approach that hashes binaries into program-level representations through large language model (LLM)-generated function embeddings. KEENHash condenses a binary into one compact and fixed-length program embedding using K-Means and Feature Hashing, allowing us to do effective and efficient large-scale program-level BCSA, surpassing the previous state-of-the-art methods. The experimental results show that KEENHash is at least 215 times faster than the state-of-the-art function matching tools while maintaining effectiveness. Furthermore, in a large-scale scenario with 5.3 billion similarity evaluations, KEENHash takes only 395.83 seconds while these tools will cost at least 56 days. We also evaluate KEENHash on the program clone search of large-scale BCSA across extensive datasets in 202,305 binaries. Compared with 4 state-of-the-art methods, KEENHash outperforms all of them by at least 23.16%, and displays remarkable superiority over them in the large-scale BCSA security scenario of malware detection.