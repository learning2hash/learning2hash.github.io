---
layout: publication
title: 'Fico-itr: Bridging Fine-grained And Coarse-grained Image-text Retrieval For
  Comparative Performance Analysis'
authors: Mikel Williams-Lekuona, Georgina Cosma
conference: Arxiv
year: 2024
bibkey: williamslekuona2024fico
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.20114'}]
tags: [Evaluation, Efficiency, Scalability, Tools & Libraries, Hashing Methods, Text
    Retrieval]
short_authors: Mikel Williams-Lekuona, Georgina Cosma
---
In the field of Image-Text Retrieval (ITR), recent advancements have leveraged large-scale Vision-Language Pretraining (VLP) for Fine-Grained (FG) instance-level retrieval, achieving high accuracy at the cost of increased computational complexity. For Coarse-Grained (CG) category-level retrieval, prominent approaches employ Cross-Modal Hashing (CMH) to prioritise efficiency, albeit at the cost of retrieval performance. Due to differences in methodologies, FG and CG models are rarely compared directly within evaluations in the literature, resulting in a lack of empirical data quantifying the retrieval performance-efficiency tradeoffs between the two. This paper addresses this gap by introducing the \texttt\{FiCo-ITR\} library, which standardises evaluation methodologies for both FG and CG models, facilitating direct comparisons. We conduct empirical evaluations of representative models from both subfields, analysing precision, recall, and computational complexity across varying data scales. Our findings offer new insights into the performance-efficiency trade-offs between recent representative FG and CG models, highlighting their respective strengths and limitations. These findings provide the foundation necessary to make more informed decisions regarding model selection for specific retrieval tasks and highlight avenues for future research into hybrid systems that leverage the strengths of both FG and CG approaches.