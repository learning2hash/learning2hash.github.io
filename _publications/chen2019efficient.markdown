---
    layout: publication
    title: "Efficient Object Embedding for Spliced Image Retrieval"
    authors: Chen Bor-Chun, Wu Zuxuan, Davis Larry S., Lim Ser-Nam
    conference: Arxiv
    year: 2019
    bibkey: chen2019efficient
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1905.11903"}
    tags: ['Arxiv', 'TIP', 'Image Retrieval']
    ---
    {% raw %}
    Detecting spliced images is one of the emerging challenges in computer vision. Unlike prior methods that focus on detecting low-level artifacts generated during the manipulation process, we use an image retrieval approach to tackle this problem. When given a spliced query image, our goal is to retrieve the original image from a database of authentic images. To achieve this goal, we propose representing an image by its constituent objects based on the intuition that the finest granularity of manipulations is oftentimes at the object-level. We introduce a framework, object embeddings for spliced image retrieval (OE-SIR), that utilizes modern object detectors to localize object regions. Each region is then embedded and collectively used to represent the image. Further, we propose a student-teacher training paradigm for learning discriminative embeddings within object regions to avoid expensive multiple forward passes. Detailed analysis of the efficacy of different feature embedding models is also provided in this study. Extensive experimental results show that the OE-SIR achieves state-of-the-art performance in spliced image retrieval.
    {% endraw %}