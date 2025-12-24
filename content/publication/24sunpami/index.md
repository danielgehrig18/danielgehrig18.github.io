---
title: "A Unified Framework for Event-based Frame Interpolation with Ad-hoc Deblurring in the Wild"
authors:
- Lei Sun
- Daniel Gehrig
- Christos Sakaridis
- Mathias Gehrig
- Jingyun Liang
- Peng Sun
- Zhijie Xu
- Kaiwei Wang
- Luc Van Gool
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-03-20T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Transactions on Pattern Analysis and Machine Intelligence (T-PAMI)*"
publication_short: ""

abstract: "Effective video frame interpolation hinges on the adept handling of motion in the input scene. Prior work acknowledges asynchronous event information for this, but often overlooks whether motion induces blur in the video, limiting its scope to sharp frame interpolation. We instead propose a unified framework for event-based frame interpolation that performs deblurring ad-hoc and thus works both on sharp and blurry input videos. Our model consists in a bidirectional recurrent network that incorporates the temporal dimension of interpolation and fuses information from the input frames and the events adaptively based on their temporal proximity. To enhance the generalization from synthetic data to real event cameras, we integrate self-supervised framework with the proposed model to enhance the generalization on real-world datasets in the wild. At the dataset level, we introduce a novel real-world high-resolution dataset with events and color videos named HighREV, which provides a challenging evaluation setting for the examined task. Extensive experiments show that our network consistently outperforms previous state-of-the-art methods on frame interpolation, single image deblurring, and the joint task of both. Experiments on domain transfer reveal that self-supervised training effectively mitigates the performance degradation observed when transitioning from synthetic data to real-world data. Code and datasets are available at https://github.com/AHupuJR/REFID."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://arxiv.org/abs/2301.05191
url_code: 'https://github.com/AHupuJR/REFID'
url_dataset: 'https://github.com/AHupuJR/REFID'
url_poster: 'https://cvpr2023.thecvf.com/virtual/2023/poster/22871'
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/mzSQR2MEAsU'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
