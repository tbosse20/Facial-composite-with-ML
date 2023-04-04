import GUI
import Genetic
import FacialComposite
import matplotlib.pyplot as plt

genetic = Genetic.Genetic(
    selection=Genetic.Selection.Tournement,
    unitType=FacialComposite.FacialComposite,
    populationSize=4,
)

#while True:

# https://stackoverflow.com/questions/41793931/plotting-images-side-by-side-using-matplotlib
# https://stackoverflow.com/questions/42867400/python-show-image-upon-hovering-over-a-point
# https://towardsdatascience.com/tooltips-with-pythons-matplotlib-dcd8db758846

# Create the figure and subplots

fig, axes = plt.subplots(2, 2)

# Display the images in the subplots
for i, ax in enumerate(axes.flat):
    ax.imshow(genetic.population[i].canvas, cmap='gray')
    plt.tick_params(top=False, bottom=False, left=False, right=False,
                labelleft=False, labelbottom=False)
def hover(event):
    # if the mouse is over the scatter points
    pass


fig.canvas.mpl_connect('motion_notify_event', hover)


def onclick(event):
    for i, ax in enumerate(axes.flat):
        if ax.contains(event)[0]:
            print(f'You clicked on image {i}')
            genetic.population[i].fitness = 1
            GUI.HighlightSpines(ax)
            fig.canvas.draw_idle()


cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

#genetic.evolve(1)

# Genetic.py
# def evolve(n=1):
# self.selection
