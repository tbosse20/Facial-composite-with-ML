import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class FacialComposite:
    # canvasSize

    parameters = {
        "head": {
            "shape": [0, 0],
            "width": [1.0, 3.0], "height": [1.0, 10.0],
            "vertical": None, "distance": None,
            "color": [[0, 0, 0], [255, 255, 255]]},
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
        pass

    # Iterate features
    # Check if value is between parameters
    # Return true

    def _RandomValue(self, feature, attribute):
        para = self.parameters[feature][attribute]
        if not para: return 0
        min, max = para[0], para[1]
        value = min  # np.random(min, max)
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

    # DrawFeature(feature) for feature in matrix
        self.DrawFeature("head")

    def MakeCanvas(self):
        canvas = np.zeros((10, 10))
        return canvas

        # Instantiate canvas
        # Set canvas size
        # Fill white
        # Return canvas

    def DrawFeature(self, feature):
        # Create path for image, feature.type/.shape
        # Load feature image
        # Resize image, feature.width/.height
        # Mirror image at feature.distance
        # Place image, feature.vertical(/.distance)
        image = mpimg.imread("Features/head/0.jpg")
        self.cavnas = np.add(self.canvas, image)
        print(self.cavnas)

    def ShowFaceImage(self):
        imgplot = plt.imshow(self.canvas)
        plt.show()

    def __str__(self):
        return str(self.features)


if __name__ == "__main__":
    festures = {
        "head": {"width": 1.7, "height": 4.8}
    }

    randomFace = FacialComposite()
    print(randomFace)
    randomFace.ShowFaceImage()