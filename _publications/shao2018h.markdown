---
    layout: publication
    title: "H-CNN: Spatial Hashing Based CNN for 3D Shape Analysis"
    authors: Shao Tianjia, Yang Yin, Weng Yanlin, Hou Qiming, Zhou Kun
    conference: Arxiv
    year: 2018
    bibkey: shao2018h
    additional_links:
       - {name: "DOI", url: "10.1109/TVCG.2018.2887262"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1803.11385"}
    tags: ['CNN', 'Arxiv']
    ---
    We present a novel spatial hashing based data structure to facilitate 3D shape analysis using convolutional neural networks (CNNs). Our method well utilizes the sparse occupancy of 3D shape boundary and builds hierarchical hash tables for an input model under different resolutions. Based on this data structure, we design two efficient GPU algorithms namely hash2col and col2hash so that the CNN operations like convolution and pooling can be efficiently parallelized. The spatial hashing is nearly minimal, and our data structure is almost of the same size as the raw input. Compared with state-of-the-art octree-based methods, our data structure significantly reduces the memory footprint during the CNN training. As the input geometry features are more compactly packed, CNN operations also run faster with our data structure. The experiment shows that, under the same network structure, our method yields comparable or better benchmarks compared to the state-of-the-art while it has only one-third memory consumption. Such superior memory performance allows the CNN to handle high-resolution shape analysis.