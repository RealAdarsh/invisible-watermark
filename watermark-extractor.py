import numpy as np
import pywt
from PIL import Image
from scipy.fftpack import dct

def load_image(image_path):
    img = Image.open(image_path).convert('L')
    return np.array(img)

def apply_dct(image_array):
    size = image_array.shape[0]
    all_subdct = np.empty((size, size))
    for i in range(0, size, 8):
        for j in range(0, size, 8):
            subpixels = image_array[i:i+8, j:j+8]
            subdct = dct(dct(subpixels.T, norm="ortho").T, norm="ortho")
            all_subdct[i:i+8, j:j+8] = subdct
    return all_subdct

def get_watermark(dct_watermarked_coeff):
    watermark_size = min(dct_watermarked_coeff.shape) // 8
    subwatermarks = []
    for x in range(0, dct_watermarked_coeff.shape[0], 8):
        for y in range(0, dct_watermarked_coeff.shape[1], 8):
            subwatermarks.append(dct_watermarked_coeff[x+5, y+5])
    watermark = np.array(subwatermarks).reshape(watermark_size, watermark_size)
    return watermark.astype(np.uint8)

def extract_watermark(image_path):
    image_array = load_image(image_path)
    dct_array = apply_dct(image_array)
    watermark = get_watermark(dct_array)
    return watermark

def main():
    image_with_watermark_path = './result/image_with_watermark.jpg'
    watermark = extract_watermark(image_with_watermark_path)
    img = Image.fromarray(watermark)
    img.save('./result/extracted_watermark.png')

if __name__ == "__main__":
    main()
