---
    layout: publication
    title: "Understanding and Improving Kernel Local Descriptors"
    authors: Mukundan Arun, Tolias Giorgos, Bursuc Andrei, Jégou Hervé, Chum Ondřej
    conference: Arxiv
    year: 2018
    bibkey: mukundan2018understanding
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1811.11147"}
    tags: ['TIP', 'Arxiv', 'Deep Learning', 'Supervised', 'Unsupervised']
    ---
    We propose a multiple-kernel local-patch descriptor based on efficient match kernels from pixel gradients. It combines two parametrizations of gradient position and direction, each parametrization provides robustness to a different type of patch mis-registration: polar parametrization for noise in the patch dominant orientation detection, Cartesian for imprecise location of the feature point. Combined with whitening of the descriptor space, that is learned with or without supervision, the performance is significantly improved. We analyze the effect of the whitening on patch similarity and demonstrate its semantic meaning. Our unsupervised variant is the best performing descriptor constructed without the need of labeled data. Despite the simplicity of the proposed descriptor, it competes well with deep learning approaches on a number of different tasks.