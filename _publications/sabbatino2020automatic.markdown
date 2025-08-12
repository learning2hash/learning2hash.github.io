---
layout: publication
title: Automatic Section Recognition In Obituaries
authors: Valentino Sabbatino, Laura Bostan, Roman Klinger
conference: Arxiv
year: 2020
bibkey: sabbatino2020automatic
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.12699'}]
tags: []
short_authors: Valentino Sabbatino, Laura Bostan, Roman Klinger
---
Obituaries contain information about people's values across times and
cultures, which makes them a useful resource for exploring cultural history.
They are typically structured similarly, with sections corresponding to
Personal Information, Biographical Sketch, Characteristics, Family, Gratitude,
Tribute, Funeral Information and Other aspects of the person. To make this
information available for further studies, we propose a statistical model which
recognizes these sections. To achieve that, we collect a corpus of 20058
English obituaries from TheDaily Item, Remembering.CA and The London Free
Press. The evaluation of our annotation guidelines with three annotators on
1008 obituaries shows a substantial agreement of Fleiss k = 0.87. Formulated as
an automatic segmentation task, a convolutional neural network outperforms
bag-of-words and embedding-based BiLSTMs and BiLSTM-CRFs with a micro F1 =
0.81.