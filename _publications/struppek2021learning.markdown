---
    layout: publication
    title: "Learning to Break Deep Perceptual Hashing: The Use Case NeuralHash"
    authors: Struppek Lukas, Hintersdorf Dominik, Neider Daniel, Kersting Kristian
    conference: Arxiv
    year: 2021
    bibkey: struppek2021learning
    additional_links:
       - {name: "DOI", url: "10.1145/3531146.3533073"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2111.06628"}
    tags: ['Arxiv']
    ---
    {% raw %}
    Apple recently revealed its deep perceptual hashing system NeuralHash to detect child sexual abuse material (CSAM) on user devices before files are uploaded to its iCloud service. Public criticism quickly arose regarding the protection of user privacy and the system's reliability. In this paper, we present the first comprehensive empirical analysis of deep perceptual hashing based on NeuralHash. Specifically, we show that current deep perceptual hashing may not be robust. An adversary can manipulate the hash values by applying slight changes in images, either induced by gradient-based approaches or simply by performing standard image transformations, forcing or preventing hash collisions. Such attacks permit malicious actors easily to exploit the detection system: from hiding abusive material to framing innocent users, everything is possible. Moreover, using the hash values, inferences can still be made about the data stored on user devices. In our view, based on our results, deep perceptual hashing in its current form is generally not ready for robust client-side scanning and should not be used from a privacy perspective.
    {% endraw %}