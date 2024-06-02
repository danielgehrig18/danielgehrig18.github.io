---
title: "Video to Events: Recycling Video Dataset for Event Cameras"
authors:
- Daniel Gehrig*
- Mathias Gehrig
- Javier Hidalgo-Carrio
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-06-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2020-06-16T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*"

publication_short: ""

abstract: "Event cameras are novel sensors that output brightness changes in the form of a stream of asynchronous “events” instead of intensity frames. They offer significant advantages with respect to conventional cameras: high dynamic range (HDR), high temporal resolution, and no motion blur. Recently, novel learning approaches operating on event data have achieved impressive results. Yet, these methods require a large amount of event data for training, which is hardly available due the novelty of event sensors in computer vision research. In this paper, we present a method that addresses these needs by converting any existing video dataset recorded with conventional cameras to synthetic event data. This unlocks the use of a virtually unlimited number of existing video datasets for training networks designed for real event data. We evaluate our method on two relevant vision tasks, i.e., object recognition and semantic segmentation, and show that models trained on synthetic events have several benefits: (i) they generalize well to real event data, even in scenarios where standard-camera images are blurry or overexposed, by inheriting the outstanding properties of event cameras; (ii) they can be used for fine-tuning on real data to improve over state-of-the-art for both classification and semantic segmentation."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/CVPR20_Gehrig.pdf
url_code: 'https://github.com/uzh-rpg/rpg_vid2e'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/uX6XknBGg0w'

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
