---
    layout: publication
    title: "One Permutation Hashing for Efficient Search and Learning"
    authors: Li Ping, Owen Art, Zhang Cun-Hui
    conference: Arxiv
    year: 2012
    bibkey: li2012one
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1208.1259"}
    tags: ['Arxiv']
    ---
    {% raw %}
    Recently, the method of b-bit minwise hashing has been applied to large-scale linear learning and sublinear time near-neighbor search. The major drawback of minwise hashing is the expensive preprocessing cost, as the method requires applying (e.g.,) k=200 to 500 permutations on the data. The testing time can also be expensive if a new data point (e.g., a new document or image) has not been processed, which might be a significant issue in user-facing applications. We develop a very simple solution based on one permutation hashing. Conceptually, given a massive binary data matrix, we permute the columns only once and divide the permuted columns evenly into k bins; and we simply store, for each data vector, the smallest nonzero location in each bin. The interesting probability analysis (which is validated by experiments) reveals that our one permutation scheme should perform very similarly to the original (k-permutation) minwise hashing. In fact, the one permutation scheme can be even slightly more accurate, due to the "sample-without-replacement" effect. Our experiments with training linear SVM and logistic regression on the webspam dataset demonstrate that this one permutation hashing scheme can achieve the same (or even slightly better) accuracies compared to the original k-permutation scheme. To test the robustness of our method, we also experiment with the small news20 dataset which is very sparse and has merely on average 500 nonzeros in each data vector. Interestingly, our one permutation scheme noticeably outperforms the k-permutation scheme when k is not too small on the news20 dataset. In summary, our method can achieve at least the same accuracy as the original k-permutation scheme, at merely 1/k of the original preprocessing cost.
    {% endraw %}