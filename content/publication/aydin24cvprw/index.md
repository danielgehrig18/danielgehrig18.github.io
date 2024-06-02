---
title: "A Hybrid ANN-SNN Architecture for Low-Power and Low-Latency Visual Perception"
authors:
- Asude Aydin
- Mathias Gehrig
- Daniel Gehrig
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
date: "2024-06-17T00:00:00Z"
doi: "" 

# Schedule page publish date (NOT publication's date).
publishDate: "2024-06-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)*"
publication_short: ""

abstract: "Spiking Neural Networks (SNNs) are a class of bioinspired neural networks that promise to bring low-power and low-latency inference to edge-devices through the use of asynchronous and sparse processing. However, being temporal models, SNNs depend heavily on expressive states to generate predictions on par with classical artificial neural networks (ANNs). These states converge only after long transient time periods, and quickly decay in the absence of input data, leading to higher latency, power consumption, and lower accuracy. In this work, we address this issue by initializing the state with an auxiliary ANN running at a low rate. The SNN then uses the state to generate predictions with high temporal resolution until the next initialization phase. Our hybrid ANN-SNN model thus combines the best of both worlds. It does not suffer from long state transients and state decay thanks to the ANN, and can generate predictions with high temporal resolution, low latency, and low power thanks to the SNN. We show for the task of eventbased 2D and 3D human pose estimation that our method consumes 88% less power with only a 4% decrease in performance compared to its fully ANN counterparts when run at the same inference rate. Moreover, when compared to SNNs, our method achieves a 74% lower error. This research thus provides a new understanding of how ANNs and SNNs can be used to maximize their respective benefits."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/CVPRW24_Aydin.pdf
url_code: 'https://github.com/uzh-rpg/hybrid_ann_snn'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

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

{{% callout note %}}
The work by Asude Aydin that contributed to the paper "A Hybrid ANN-SNN Architecture for Low-Power and Low-Latency Visual Perception" at a CVPR Workshop 2024 lead to a UZH Master Thesis Award.
{{% /callout %}}
