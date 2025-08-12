---
layout: publication
title: 'A Method For Efficient Heterogeneous Parallel Compilation: A Cryptography
  Case Study'
authors: Zhiyuan Tan, Liutong Han, Mingjie Xing, Yanjun Wu
conference: 2024 IEEE Smart World Congress (SWC)
year: 2024
bibkey: tan2024method
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.09333'}]
tags: ["Efficiency"]
short_authors: Tan et al.
---
In the era of diminishing returns from Moores Law, heterogeneous computing systems have emerged as a vital approach to enhance computational efficiency. This paper introduces a novel MLIR-based dialect, named hyper, designed to optimize data management and parallel computation across diverse hardware architectures. The hyper dialect abstracts the complexities of heterogeneous computing by providing a unified compilation framework that efficiently schedules tasks and manages data communication. To demonstrate its capabilities, we present HETOCompiler, a cryptography-focused compiler prototype that implements multiple hash algorithms and enables their execution on heterogeneous systems. The proposed approach achieves performance improvements over existing programming models for heterogeneous computing (OpenCL), offering an average speedup of 1.93x, 1.18x, and 1.12x for SHA-1, MD5, and SM3 algorithms, respectively. Our findings highlight the potential of the hyper dialect in harnessing the full computational power of heterogeneous devices, advancing the field of compiler design for heterogeneous systems.