---
    layout: publication
    title: "Hashing with binary autoencoders"
    authors: Carreira-Perpiñán Miguel Á., Raziperchikolaei Ramin
    conference: Arxiv
    year: 2015
    bibkey: carreiraperpiñán2015hashing
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1501.00756"}
    tags: ['Arxiv', 'Image Retrieval']
    ---
    {% raw %}
    An attractive approach for fast search in image databases is binary hashing, where each high-dimensional, real-valued image is mapped onto a low-dimensional, binary vector and the search is done in this binary space. Finding the optimal hash function is difficult because it involves binary constraints, and most approaches approximate the optimization by relaxing the constraints and then binarizing the result. Here, we focus on the binary autoencoder model, which seeks to reconstruct an image from the binary code produced by the hash function. We show that the optimization can be simplified with the method of auxiliary coordinates. This reformulates the optimization as alternating two easier steps: one that learns the encoder and decoder separately, and one that optimizes the code for each image. Image retrieval experiments, using precision/recall and a measure of code utilization, show the resulting hash function outperforms or is competitive with state-of-the-art methods for binary hashing.
    {% endraw %}