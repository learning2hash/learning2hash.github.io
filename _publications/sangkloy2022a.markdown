---
    layout: publication
    title: "A Sketch Is Worth a Thousand Words: Image Retrieval with Text and Sketch"
    authors: Sangkloy Patsorn, Jitkrittum Wittawat, Yang Diyi, Hays James
    conference: Arxiv
    year: 2022
    bibkey: sangkloy2022a
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2208.03354"}
   - {name: "Paper", url: "https://janesjanes.github.io/tsbir/."}
    tags: ['Arxiv', 'Image Retrieval']
    ---
    {% raw %}
    We address the problem of retrieving images with both a sketch and a text query. We present TASK-former (Text And SKetch transformer), an end-to-end trainable model for image retrieval using a text description and a sketch as input. We argue that both input modalities complement each other in a manner that cannot be achieved easily by either one alone. TASK-former follows the late-fusion dual-encoder approach, similar to CLIP, which allows efficient and scalable retrieval since the retrieval set can be indexed independently of the queries. We empirically demonstrate that using an input sketch (even a poorly drawn one) in addition to text considerably increases retrieval recall compared to traditional text-based image retrieval. To evaluate our approach, we collect 5,000 hand-drawn sketches for images in the test set of the COCO dataset. The collected sketches are available a https://janesjanes.github.io/tsbir/.
    {% endraw %}