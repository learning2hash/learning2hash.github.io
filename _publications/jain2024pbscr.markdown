---
layout: publication
title: 'PBSCR: The Piano Bootleg Score Composer Recognition Dataset'
authors: Arhan Jain, Alec Bunn, Austin Pham, Tj Tsai
conference: Transactions of the International Society for Music Information Retrieval
year: 2024
bibkey: jain2024pbscr
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.16803'}]
tags: ["Datasets"]
short_authors: Jain et al.
---
This article motivates, describes, and presents the PBSCR dataset for
studying composer recognition of classical piano music. Our goal was to design
a dataset that facilitates large-scale research on composer recognition that is
suitable for modern architectures and training practices. To achieve this goal,
we utilize the abundance of sheet music images and rich metadata on IMSLP, use
a previously proposed feature representation called a bootleg score to encode
the location of noteheads relative to staff lines, and present the data in an
extremely simple format (2D binary images) to encourage rapid exploration and
iteration. The dataset itself contains 40,000 62x64 bootleg score images for a
9-class recognition task, 100,000 62x64 bootleg score images for a 100-class
recognition task, and 29,310 unlabeled variable-length bootleg score images for
pretraining. The labeled data is presented in a form that mirrors MNIST images,
in order to make it extremely easy to visualize, manipulate, and train models
in an efficient manner. We include relevant information to connect each bootleg
score image with its underlying raw sheet music image, and we scrape, organize,
and compile metadata from IMSLP on all piano works to facilitate multimodal
research and allow for convenient linking to other datasets. We release
baseline results in a supervised and low-shot setting for future works to
compare against, and we discuss open research questions that the PBSCR data is
especially well suited to facilitate research on.