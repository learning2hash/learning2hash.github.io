---
    layout: publication
    title: "PinView: Implicit Feedback in Content-Based Image Retrieval"
    authors: Hussain Zakria, Klami Arto, Kujala Jussi, Leung Alex P., Pasupa Kitsuchart, Auer Peter, Kaski Samuel, Laaksonen Jorma, Shawe-Taylor John
    conference: Arxiv
    year: 2014
    bibkey: hussain2014pinview
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1410.0471"}
    tags: ['Arxiv', 'Image Retrieval']
    ---
    {% raw %}
    This paper describes PinView, a content-based image retrieval system that exploits implicit relevance feedback collected during a search session. PinView contains several novel methods to infer the intent of the user. From relevance feedback, such as eye movements or pointer clicks, and visual features of images, PinView learns a similarity metric between images which depends on the current interests of the user. It then retrieves images with a specialized online learning algorithm that balances the tradeoff between exploring new images and exploiting the already inferred interests of the user. We have integrated PinView to the content-based image retrieval system PicSOM, which enables applying PinView to real-world image databases. With the new algorithms PinView outperforms the original PicSOM, and in online experiments with real users the combination of implicit and explicit feedback gives the best results.
    {% endraw %}