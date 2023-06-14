import numpy as np

def fit_circumscribed_sphere_4points(array, tol=1e-6):
    # Check if the the points are co-linear
    D12 = array[1] - array[0]
    D12 = D12 / np.linalg.norm(D12)
    D13 = array[2] - array[0]
    D13 = D13 / np.linalg.norm(D13)
    D14 = array[3] - array[0]
    D14 = D14 / np.linalg.norm(D14)

    chk1 = np.clip(np.abs(np.dot(D12, D13)), 0., 1.)  # 如果共线，chk1=1
    chk2 = np.clip(np.abs(np.dot(D12, D14)), 0., 1.)
    # 求的是反余弦值，如果是1，反余弦值为0（弧度），乘以180/pi，就是0（度），说明共线
    if np.arccos(chk1) / np.pi * 180 < tol or np.arccos(chk2) / np.pi * 180 < tol:
        R = np.inf
        C = np.full(3, np.nan)
        return R, C

    # Check if the the points are co-planar
    n1 = np.linalg.norm(np.cross(D12, D13))
    n2 = np.linalg.norm(np.cross(D12, D14))

    chk = np.clip(np.abs(np.dot(n1, n2)), 0., 1.)
    if np.arccos(chk) / np.pi * 180 < tol:
        R = np.inf
        C = np.full(3, np.nan)
        return R, C

    # Centroid of the sphere
    A = 2 * (array[1:] - np.full(len(array) - 1, array[0]))
    b = np.sum((np.square(array[1:]) - np.square(np.full(len(array) - 1, array[0]))), axis=1)
    C = np.transpose(np.linalg.solve(A, b))

    # Radius of the sphere
    R = np.sqrt(np.sum(np.square(array[0] - C), axis=0))
    print("Center:", C)
    print("Radius:", R)

    return C, R


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
