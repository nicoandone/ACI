import cv2
import config


def to_grayscale(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def denoise(image, method, size):
    if method == "median":
        image = cv2.medianBlur(image, size)
    elif method == "gaussian":
        image = cv2.GaussianBlur(image, (size, size), 0)  
    return image


def binarize(image):
    threshold, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    print("threshold: ", threshold)
    return binary


def clean(image, method, size):
    if method == "opening":
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    elif method == "line_opening":
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, 1))
        vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, size))
        horizontal = cv2.morphologyEx(image, cv2.MORPH_OPEN, horizontal_kernel)
        vertical = cv2.morphologyEx(image, cv2.MORPH_OPEN, vertical_kernel)
        image = cv2.bitwise_or(horizontal, vertical)
    return image


def preprocess(image, method, filter_size, morph_method, morph_size):
    grayscale = to_grayscale(image)
    denoised = denoise(grayscale, method, filter_size)
    binary = binarize(denoised)
    cleaned = clean(binary, morph_method, morph_size)
    return cleaned


def main():
    cfg = config.preprocessing
    out = config.root / cfg["output"]
    out.mkdir(parents=True, exist_ok=True)

    for path in sorted((config.root / cfg["input"]).glob("*.png")):
        image = cv2.imread(str(path))
        result = preprocess(image, cfg["filter"], cfg["filter_size"], cfg["morph_cleanup"], cfg["morph_size"])
        cv2.imwrite(str(out / path.name), result)


if __name__ == "__main__":
    main()
