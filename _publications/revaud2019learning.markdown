---
    layout: publication
    title: "Learning with Average Precision: Training Image Retrieval with a Listwise Loss"
    authors: Revaud Jerome, Almazan Jon, de Rezende Rafael Sampaio, de Souza Cesar Roberto
    conference: Arxiv
    year: 2019
    bibkey: revaud2019learning
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1906.07589"}
   - {name: "Paper", url: "https://europe.naverlabs.com/Deep-Image-Retrieval/"}
    tags: ['Arxiv', 'Image Retrieval']
    ---
    {% raw %}
    Image retrieval can be formulated as a ranking problem where the goal is to order database images by decreasing similarity to the query. Recent deep models for image retrieval have outperformed traditional methods by leveraging ranking-tailored loss functions, but important theoretical and practical problems remain. First, rather than directly optimizing the global ranking, they minimize an upper-bound on the essential loss, which does not necessarily result in an optimal mean average precision (mAP). Second, these methods require significant engineering efforts to work well, e.g. special pre-training and hard-negative mining. In this paper we propose instead to directly optimize the global mAP by leveraging recent advances in listwise loss formulations. Using a histogram binning approximation, the AP can be differentiated and thus employed to end-to-end learning. Compared to existing losses, the proposed method considers thousands of images simultaneously at each iteration and eliminates the need for ad hoc tricks. It also establishes a new state of the art on many standard retrieval benchmarks. Models and evaluation scripts have been made available at https://europe.naverlabs.com/Deep-Image-Retrieval/
    {% endraw %}