---
    layout: publication
    title: "Bilinear Supervised Hashing Based on 2D Image Features"
    authors: Ding Yujuan, Wong Wai Kueng, Lai Zhihui, Zhang Zheng
    conference: Arxiv
    year: 2019
    bibkey: ding2019bilinear
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1901.01474"}
    tags: ['Supervised', 'Arxiv', 'CNN']
    ---
    Hashing has been recognized as an efficient representation learning method to effectively handle big data due to its low computational complexity and memory cost. Most of the existing hashing methods focus on learning the low-dimensional vectorized binary features based on the high-dimensional raw vectorized features. However, studies on how to obtain preferable binary codes from the original 2D image features for retrieval is very limited. This paper proposes a bilinear supervised discrete hashing (BSDH) method based on 2D image features which utilizes bilinear projections to binarize the image matrix features such that the intrinsic characteristics in the 2D image space are preserved in the learned binary codes. Meanwhile, the bilinear projection approximation and vectorization binary codes regression are seamlessly integrated together to formulate the final robust learning framework. Furthermore, a discrete optimization strategy is developed to alternatively update each variable for obtaining the high-quality binary codes. In addition, two 2D image features, traditional SURF-based FVLAD feature and CNN-based AlexConv5 feature are designed for further improving the performance of the proposed BSDH method. Results of extensive experiments conducted on four benchmark datasets show that the proposed BSDH method almost outperforms all competing hashing methods with different input features by different evaluation protocols.