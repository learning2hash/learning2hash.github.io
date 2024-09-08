---
    layout: publication
    title: "NIST: An Image Classification Network to Image Semantic Retrieval"
    authors: Dong Le, Chen Xiuyuan, Mao Mengdie, Zhang Qianni
    conference: Arxiv
    year: 2016
    bibkey: dong2016nist
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1607.00464"}
    tags: ['Image Retrieval', 'Arxiv', 'ICIP']
    ---
    This paper proposes a classification network to image semantic retrieval (NIST) framework to counter the image retrieval challenge. Our approach leverages the successful classification network GoogleNet based on Convolutional Neural Networks to obtain the semantic feature matrix which contains the serial number of classes and corresponding probabilities. Compared with traditional image retrieval using feature matching to compute the similarity between two images, NIST leverages the semantic information to construct semantic feature matrix and uses the semantic distance algorithm to compute the similarity. Besides, the fusion strategy can significantly reduce storage and time consumption due to less classes participating in the last semantic distance computation. Experiments demonstrate that our NIST framework produces state-of-the-art results in retrieval experiments on MIRFLICKR-25K dataset.