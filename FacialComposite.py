import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def insertImage(foreground, background, x, y):
    # https://docs.opencv.org/3.4/d0/d86/tutorial_py_image_arithmetics.html
    h, w, channels = foreground.shape
    roi = background[y:y+h, x:x+w]
    foregroundgray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(foregroundgray, 200, 255, cv2.THRESH_BINARY)
    background_bg = cv2.bitwise_and(roi, roi, mask=mask)
    mask_inv = cv2.bitwise_not(mask)
    foreground_fg = cv2.bitwise_and(foreground, foreground, mask=mask_inv)
    dst = cv2.add(background_bg, foreground_fg)
    background[y:y+h, x:x+w] = dst
    return background

class FacialComposite:
    # canvasSize

    parameters = {
        "head": {
            "shape": [0, 1],
            "width": [500, 800], "height": [500, 800],
            "distance": None, "vertical": None,
            "color": [[0, 0, 0], [255, 255, 255]]
        }, "eye": {
            "shape": [0, 2],
            "width": [100, 200], "height": [100, 200],
            "distance": [100, 300], "vertical": [-300, 0],
            "color": None
        }, "mouth": {
            "shape": [0, 1],
            "width": [100, 200], "height": [100, 200],
            "distance": [0, 2.0], "vertical": [0, 300],
            "color": None
        }, "nose": {
            "shape": [0, 1],
            "width": [100, 200], "height": [100, 200],
            "distance": [0, 0], "vertical": [-200, 200],
            "color": None
        }
    }

    def __init__(self, features=None):
        if not features:
            features = self._RandomFeatures()
        else:
            features = self.ValidateFeatures(features)
        self.features = features
        self.DrawFace()
        self.selected = False

    def ValidateFeatures(self, features):
        return features

    # Iterate features
    # Check if value is between parameters
    # Return true

    def _RandomValue(self, feature, attribute):
        para = self.parameters[feature][attribute]
        if not para: return 0
        min, max = para[0], para[1]
        if type(min) == list: return [0, 0, 0]
        value = random.randint(min, max)
        return value

    def _RandomValues(self, feature):
        attributes = dict()
        for attribute in self.parameters[feature]:
            value = self._RandomValue(feature, attribute)
            attributes[attribute] = value
        return attributes

    def _RandomFeatures(self):
        features = dict()
        for feature in self.parameters.keys():
            attributes = self._RandomValues(feature)
            features[feature] = attributes
        return features

    def _LoadFeaturesShapes(self):
        pass

    # Declare shapes dictionary
    # Set path to feature images
    # Iterate each feature
    # Load feature shapes, path
    # Append features shapes to shapes
    # Return shapes

    def FeaturesToDNA(self):
        pass

    # Convert matrix to binary
    # Flatten matrix to DNA
    # Return DNA

    def DNAToFeatures(self):
        pass

    # Convert DNA to decimal
    # Reshape DNA to matrix
    # Return matrix

    def DrawFace(self):
        self.canvas = self.MakeCanvas()

        print(self.features)
        for type, feature in self.features.items():
            self.DrawFeature(type, feature)

    def MakeCanvas(self):
        canvas = np.zeros([800, 800, 3], dtype=np.uint8)
        canvas[:] = 255
        return canvas

        # Instantiate canvas
        # Set canvas size
        # Fill white
        # Return canvas

    def DrawFeature(self, type, feature):
        shape = str(feature["shape"])
        image = cv2.imread("Features/" + type + "/" + shape + ".jpg")

        width, height = feature["width"], feature["height"]
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

        amount = 2 if feature["distance"] > 0 else 1

        for i in range(amount):
            vertical, distance = feature["vertical"], feature["distance"]

            if i == 1:
                image = cv2.flip(image, 1)
                distance *= -1

            distance += int(self.canvas.shape[1] / 2 - width / 2)
            vertical += int(self.canvas.shape[0] / 2 - height / 2)

            self.canvas = insertImage(image, self.canvas, distance, vertical)



    def ShowFaceImage(self):
        plt.imshow(self.canvas)
        plt.axis('off')
        plt.show()

    def __str__(self):
        return str(self.features)


if __name__ == "__main__":

    festures = {
        "head": {"shape": 0, "width": 700, "height": 700, "distance": 0, "vertical": 0},
        "eye": {"shape": 0, "width": 100, "height": 100, "distance": 0, "vertical": 0},
        "mouth": {"shape": 0, "width": 100, "height": 100, "distance": 0, "vertical": 100},
    }

    for i in range(10):
        randomFace = FacialComposite()
        print(randomFace)
        randomFace.ShowFaceImage()