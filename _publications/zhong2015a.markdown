---
    layout: publication
    title: "A Deep Hashing Learning Network"
    authors: Zhong Guoqiang, Yang Pan, Wang Sijiang, Dong Junyu
    conference: Arxiv
    year: 2015
    bibkey: zhong2015a
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1507.04437"}
    tags: ['Supervised', 'Arxiv', 'Quantisation']
    ---
    {% raw %}
    Hashing-based methods seek compact and efficient binary codes that preserve the neighborhood structure in the original data space. For most existing hashing methods, an image is first encoded as a vector of hand-crafted visual feature, followed by a hash projection and quantization step to get the compact binary vector. Most of the hand-crafted features just encode the low-level information of the input, the feature may not preserve the semantic similarities of images pairs. Meanwhile, the hashing function learning process is independent with the feature representation, so the feature may not be optimal for the hashing projection. In this paper, we propose a supervised hashing method based on a well designed deep convolutional neural network, which tries to learn hashing code and compact representations of data simultaneously. The proposed model learn the binary codes by adding a compact sigmoid layer before the loss layer. Experiments on several image data sets show that the proposed model outperforms other state-of-the-art methods.
    {% endraw %}