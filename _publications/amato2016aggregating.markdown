---
    layout: publication
    title: "Aggregating Binary Local Descriptors for Image Retrieval"
    authors: Amato Giuseppe, Falchi Fabrizio, Vadicamo Lucia
    conference: Arxiv
    year: 2016
    bibkey: amato2016aggregating
    additional_links:
       - {name: "DOI", url: "10.1007/s11042-017-4450-2"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1608.00813"}
    tags: ['Arxiv', 'Image Retrieval', 'CNN']
    ---
    Content-Based Image Retrieval based on local features is computationally expensive because of the complexity of both extraction and matching of local feature. On one hand, the cost for extracting, representing, and comparing local visual descriptors has been dramatically reduced by recently proposed binary local features. On the other hand, aggregation techniques provide a meaningful summarization of all the extracted feature of an image into a single descriptor, allowing us to speed up and scale up the image search. Only a few works have recently mixed together these two research directions, defining aggregation methods for binary local features, in order to leverage on the advantage of both approaches. In this paper, we report an extensive comparison among state-of-the-art aggregation methods applied to binary features. Then, we mathematically formalize the application of Fisher Kernels to Bernoulli Mixture Models. Finally, we investigate the combination of the aggregated binary features with the emerging Convolutional Neural Network (CNN) features. Our results show that aggregation methods on binary features are effective and represent a worthwhile alternative to the direct matching. Moreover, the combination of the CNN with the Fisher Vector (FV) built upon binary features allowed us to obtain a relative improvement over the CNN results that is in line with that recently obtained using the combination of the CNN with the FV built upon SIFTs. The advantage of using the FV built upon binary features is that the extraction process of binary features is about two order of magnitude faster than SIFTs.