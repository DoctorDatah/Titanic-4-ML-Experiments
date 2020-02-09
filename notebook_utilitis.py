import os
import matplotlib.pyplot as plt


# # Get 2 levels up in directory structure to root directory of the project
# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) 
# # Also Setting the Root Directory
# os.chdir(os.path.dirname(os.path.dirname(__file__)))
# # Figures images Path
PROJECT_ROOT = os.getcwd()
IMAGES_PATH =  os.path.join('.','figures')

# def set_dir_to_root():
#     """
#     Go 1 level up in directory structure to root directory of the project
#     ---------------------------------------------------------------------
#     """ 
#     os.chdir(os.path.dirname(os.path.dirname(__file__)))

    
def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    """
    Save image to Default Figure path
    Source: Handson ML Book
    """
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)