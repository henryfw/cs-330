import cv2 as cv
import os
import pickle


# save images as an array of tuples: [( [1024,1024], 0|1 ), ... ]
def resizeImagesAsFile(inputFolder, saveFile, width=1024, height=1024):

    data = []

    for label in ["0", "1"]:
        with os.scandir(inputFolder + "/" + label) as entries:
            for entry in entries:
                if entry.name.lower().endswith(".png") or entry.name.lower().endswith(".jpeg"):
                    image = cv.imread(entry.path, cv.IMREAD_GRAYSCALE)

                    image_scaled = cv.resize(image, (width, height), interpolation=cv.INTER_AREA)
                    data.append((image_scaled, int(label)))

    if os.path.exists(saveFile):
        os.remove(saveFile)

    print("saving {} items.".format(len(data)))
    pickle.dump(data, open(saveFile, "wb"))


if __name__ == '__main__':
    #
    # resizeImagesAsFile('C:/Users/uprz2/Downloads/cs330/images/pneumonia/', "C:/Users/uprz2/Downloads/cs330/data/pneumonia-1024", 1024, 1024)
    # resizeImagesAsFile('C:/Users/uprz2/Downloads/cs330/images/tb1/', "C:/Users/uprz2/Downloads/cs330/data/tb1-1024", 1024, 1024)
    #
    # resizeImagesAsFile('C:/Users/uprz2/Downloads/cs330/images/pneumonia/', "C:/Users/uprz2/Downloads/cs330/data/pneumonia-512", 512, 512)
    # resizeImagesAsFile('C:/Users/uprz2/Downloads/cs330/images/tb1/', "C:/Users/uprz2/Downloads/cs330/data/tb1-512", 512, 512)
    #
    resizeImagesAsFile('C:/Users/uprz2/Downloads/cs330/images/pneumonia/', "C:/Users/uprz2/Downloads/cs330/data/pneumonia-256-grayscale", 256, 256)
    resizeImagesAsFile('C:/Users/uprz2/Downloads/cs330/images/tb1/', "C:/Users/uprz2/Downloads/cs330/data/tb1-256-grayscale", 256, 256)