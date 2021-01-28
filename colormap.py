import matplotlib.pyplot as plt

def graph(H):
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111)
    ax.set_title('color-map')
    plt.imshow(H, cmap = 'jet')
    ax.set_aspect('equal')

    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')
    plt.show()