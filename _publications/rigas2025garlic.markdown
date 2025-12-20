---
layout: publication
title: 'GARLIC: Gaussian Representation Learning For Space Partitioning'
authors: Panagiotis Rigas, Panagiotis Drivas, Charalambos Tzamos, Ioannis Chamodrakas,
  George Ioannakis, Leonidas J. Guibas, Ioannis Z. Emiris
conference: Arxiv
year: 2025
bibkey: rigas2025garlic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.24608'}]
tags: ["Evaluation", "Tools & Libraries", "Vector Indexing"]
short_authors: Rigas et al.
---
We introduce GARLIC (GAussian Representation LearnIng for spaCe partitioning), a novel indexing structure based on \(N\)-dimensional Gaussians for efficiently learning high-dimensional vector spaces. Our approach is inspired from Gaussian splatting techniques, typically used in 3D rendering, which we adapt for high-dimensional search and classification. We optimize Gaussian parameters using information-theoretic objectives that balance coverage, assignment confidence, and structural and semantic consistency. A key contribution is to progressively refine the representation through split and clone operations, handling hundreds of dimensions, thus handling varying data densities. GARLIC offers the fast building times of traditional space partitioning methods (e.g., under \(\sim5\) min build time for SIFT1M) while achieving \(\sim50%\) Recall10@10 in low-candidate regimes. Experimental results on standard benchmarks demonstrate our method's consistency in (a) \(k\)-NN retrieval, outperforming methods, such as Faiss-IVF, in fast-recall by using about half their probes for the same Recall10@10 in Fashion-MNIST, and (b) in classification tasks, beating by \(\sim15%\) accuracy other majority voting methods. Further, we show strong generalization capabilities, maintaining high accuracy even with downsampled training data: using just \(1%\) of the training data returns \(\sim 45%\) Recall@1, thus making GARLIC quite powerful for applications requiring both speed and accuracy.