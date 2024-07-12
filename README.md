# Watermarking Scripts

## Introduction
These scripts demonstrate how to embed and extract invisible watermarks from images using Python, NumPy, PyWavelets, PIL (Pillow), and scipy.

## Dependencies
Make sure you have Python 3.x installed. Install the required Python packages using pip:

```bash
pip install numpy pywavelets pillow scipy
```

Usage
1. Adding Watermark (add-watermark.py)
This script adds an invisible watermark to an image.

Usage:
```bash
python add-watermark.py
```

2. Extracting Watermark (watermark-extractor.py)
This script extracts the invisible watermark from an image that has been watermarked.

Usage:
```bash
python watermark-extractor.py
```

### Scripts Overview
#### add-watermark.py
Description: Embeds an invisible watermark into an image.
Dependencies: numpy, pywavelets, pillow, scipy
Usage: Ensure imagetest1.jpg and qrcodetest1.png are in the respective folders. Run the script to watermark imagetest1.jpg.

#### watermark-extractor.py
Description: Extracts an invisible watermark from an image.
Dependencies: numpy, pywavelets, pillow, scipy
Usage: Run the script to extract the watermark from ./result/image_with_watermark.jpg and save it as ./result/extracted_watermark.png.
