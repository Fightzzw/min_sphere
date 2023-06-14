import matplotlib.pyplot as plt
from get_min_sphere_4points import get_min_sphere_4points
from fit_circumscribed_sphere_4points import fit_circumscribed_sphere_4points

if __name__ == '__main__':

    # # Define the four points
    p1 = np.array([0, 0, 0])
    p2 = np.array([0, 4, 0])
    p3 = np.array([4, 0, 0])
    p4 = np.array([1, 2, 0])

    points1 = np.array([p1, p2, p3, p4])

    points1 = np.random.rand(4, 3)
    # show_tetrahedron(points1)
    center0, radius0 = fit_circumscribed_sphere_4points(points1)

    center1, radius1 = get_min_sphere_4points(points1)


    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Plot the points
    ax.scatter(points1[:, 0], points1[:, 1], points1[:, 2], c='b')
    # plot the tetrahedron
    ax.plot(points1[:, 0], points1[:, 1], points1[:, 2], c='b')

    # Plot the sphere1
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    x = center0[0] + radius0 * np.cos(u) * np.sin(v)
    y = center0[1] + radius0 * np.sin(u) * np.sin(v)
    z = center0[2] + radius0 * np.cos(v)
    ax.plot_wireframe(x, y, z, color="g")

    # Plot the sphere2
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    x = center1[0] + radius1 * np.cos(u) * np.sin(v)
    y = center1[1] + radius1 * np.sin(u) * np.sin(v)
    z = center1[2] + radius1 * np.cos(v)
    ax.plot_wireframe(x, y, z, color="y")

    # Set the axes properties
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('equal')
    # Show the plot
    print('Showing the plot...')
    plt.show()
