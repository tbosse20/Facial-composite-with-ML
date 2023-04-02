import random

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

class FacialComposite:
    # canvasSize

    parameters = {
        "head": {
            "shape": [0, 0],
            "width": [500, 800], "height": [500, 800],
            "distance": None, "vertical": None,
            "color": [[0, 0, 0], [255, 255, 255]]
        }, "eye": {
            "shape": [0, 0],
            "width": [100, 200], "height": [100, 200],
            "distance": [0, 2.0], "vertical": [0, 9.0],
            "color": None
        },
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

        vertical, distance = feature["vertical"], feature["distance"]
        distance += int(self.canvas.shape[1] / 2 - width / 2)
        vertical += int(self.canvas.shape[0] / 2 - height / 2)

        self.canvas[
            vertical : vertical + height,
            distance : distance + width
        ] = image

    def ShowFaceImage(self):
        plt.imshow(self.canvas)
        plt.show()

    def __str__(self):
        return str(self.features)


if __name__ == "__main__":
    festures = {
        "head": {"shape": 0, "width": 700, "height": 700, "distance": 0, "vertical": 0},
        "eye": {"shape": 0, "width": 100, "height": 100, "distance": 0, "vertical": 0},
    }

    randomFace = FacialComposite(festures)
    print(randomFace)
    randomFace.ShowFaceImage()