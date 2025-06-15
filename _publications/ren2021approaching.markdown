---
layout: publication
title: 'Acnet: Approaching-and-centralizing Network For Zero-shot Sketch-based Image Retrieval'
authors: Hao Ren et al.
conference: "Arxiv"
year: 2021
citations: 13
bibkey: ren2021approaching
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2111.12757'}
tags: ['Tools and Libraries', 'Applications']
---
The huge domain gap between sketches and photos and the highly abstract
sketch representations pose challenges for sketch-based image retrieval
(\underline\{SBIR\}). The zero-shot sketch-based image retrieval
(\underline\{ZS-SBIR\}) is more generic and practical but poses an even greater
challenge because of the additional knowledge gap between the seen and unseen
categories. To simultaneously mitigate both gaps, we propose an
\textbf\{A\}pproaching-and-\textbf\{C\}entralizing \textbf\{Net\}work (termed
"\textbf\{ACNet\}") to jointly optimize sketch-to-photo synthesis and the image
retrieval. The retrieval module guides the synthesis module to generate large
amounts of diverse photo-like images which gradually approach the photo domain,
and thus better serve the retrieval module than ever to learn domain-agnostic
representations and category-agnostic common knowledge for generalizing to
unseen categories. These diverse images generated with retrieval guidance can
effectively alleviate the overfitting problem troubling concrete
category-specific training samples with high gradients. We also discover the
use of proxy-based NormSoftmax loss is effective in the zero-shot setting
because its centralizing effect can stabilize our joint training and promote
the generalization ability to unseen categories. Our approach is simple yet
effective, which achieves state-of-the-art performance on two widely used
ZS-SBIR datasets and surpasses previous methods by a large margin.
