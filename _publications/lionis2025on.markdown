---
layout: publication
title: On The Reproducibility Of Learned Sparse Retrieval Adaptations For Long Documents
authors: Emmanouil Georgios Lionis, Jia-Huei Ju
conference: Lecture Notes in Computer Science
year: 2025
bibkey: lionis2025on
citations: 0
additional_links: [{name: Code, url: 'https://github.com/lionisakis/Reproducibilitiy-lsr-long'},
  {name: Paper, url: 'https://arxiv.org/abs/2503.23824'}]
tags: ["Evaluation", "SIGIR", "Text Retrieval"]
short_authors: Emmanouil Georgios Lionis, Jia-Huei Ju
---
Document retrieval is one of the most challenging tasks in Information
Retrieval. It requires handling longer contexts, often resulting in higher
query latency and increased computational overhead. Recently, Learned Sparse
Retrieval (LSR) has emerged as a promising approach to address these
challenges. Some have proposed adapting the LSR approach to longer documents by
aggregating segmented document using different post-hoc methods, including
n-grams and proximity scores, adjusting representations, and learning to
ensemble all signals. In this study, we aim to reproduce and examine the
mechanisms of adapting LSR for long documents. Our reproducibility experiments
confirmed the importance of specific segments, with the first segment
consistently dominating document retrieval performance. Furthermore, We
re-evaluate recently proposed methods -- ExactSDM and SoftSDM -- across varying
document lengths, from short (up to 2 segments) to longer (3+ segments). We
also designed multiple analyses to probe the reproduced methods and shed light
on the impact of global information on adapting LSR to longer contexts. The
complete code and implementation for this project is available at:
https://github.com/lionisakis/Reproducibilitiy-lsr-long.