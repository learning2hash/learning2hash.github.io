---
    layout: publication
    title: "Group Invariant Deep Representations for Image Instance Retrieval"
    authors: Morère Olivier, Veillard Antoine, Lin Jie, Petta Julie, Chandrasekhar Vijay, Poggio Tomaso
    conference: Arxiv
    year: 2016
    bibkey: morère2016group
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1601.02093"}
    tags: ['Arxiv', 'Quantisation', 'TIP', 'CNN']
    ---
    {% raw %}
    Most image instance retrieval pipelines are based on comparison of vectors known as global image descriptors between a query image and the database images. Due to their success in large scale image classification, representations extracted from Convolutional Neural Networks (CNN) are quickly gaining ground on Fisher Vectors (FVs) as state-of-the-art global descriptors for image instance retrieval. While CNN-based descriptors are generally remarked for good retrieval performance at lower bitrates, they nevertheless present a number of drawbacks including the lack of robustness to common object transformations such as rotations compared with their interest point based FV counterparts. In this paper, we propose a method for computing invariant global descriptors from CNNs. Our method implements a recently proposed mathematical theory for invariance in a sensory cortex modeled as a feedforward neural network. The resulting global descriptors can be made invariant to multiple arbitrary transformation groups while retaining good discriminativeness. Based on a thorough empirical evaluation using several publicly available datasets, we show that our method is able to significantly and consistently improve retrieval results every time a new type of invariance is incorporated. We also show that our method which has few parameters is not prone to overfitting: improvements generalize well across datasets with different properties with regard to invariances. Finally, we show that our descriptors are able to compare favourably to other state-of-the-art compact descriptors in similar bitranges, exceeding the highest retrieval results reported in the literature on some datasets. A dedicated dimensionality reduction step --quantization or hashing-- may be able to further improve the competitiveness of the descriptors.
    {% endraw %}