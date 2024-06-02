---
title: "Low Latency Automotive Vision with Event Cameras"
authors:
- Daniel Gehrig
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-05-29T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Nature"
publication_short: ""

abstract: "The computer vision algorithms used currently in advanced driver assistance systems rely on image-based RGB cameras, leading to a critical bandwidth–latency trade-off for delivering safe driving experiences. To address this, event cameras have emerged as alternative vision sensors. Event cameras measure the changes in intensity asynchronously, offering high temporal resolution and sparsity, markedly reducing bandwidth and latency requirements. Despite these advantages, event-camera-based algorithms are either highly efficient but lag behind image-based ones in terms of accuracy or sacrifice the sparsity and efficiency of events to achieve comparable results. To overcome this, here we propose a hybrid event- and frame-based object detector that preserves the advantages of each modality and thus does not suffer from this trade-off. Our method exploits the high temporal resolution and sparsity of events and the rich but low temporal resolution information in standard images to generate efficient, high-rate object detections, reducing perceptual and computational latency. We show that the use of a 20 frames per second (fps) RGB camera plus an event camera can achieve the same latency as a 5,000-fps camera with the bandwidth of a 45-fps camera without compromising accuracy. Our approach paves the way for efficient and robust perception in edge-case scenarios by uncovering the potential of event cameras."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: https://www.nature.com/articles/s41586-024-07409-w
url_code: 'https://github.com/uzh-rpg/dagr'
url_dataset: 'https://dsec.ifi.uzh.ch/dsec-detection/'
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/dwzGhMQCc4Y'

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
This work lead to me winning the UZH Annual Award, which is awarded to the best Ph.D. in the department of Informatics!
{{% /callout %}}

