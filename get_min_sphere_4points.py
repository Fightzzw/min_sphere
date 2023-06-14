import numpy as np



def get_min_sphere_4points(points):
    """
    Get the minimum radius of a circumscribed sphere that encloses all the points
    """
    def minimum_enclosing_sphere_3points(triangle):
        # Compute the circumcenter of the triangle
        a, b, c = triangle
        ab = b - a
        ac = c - a
        ab_cross_ac = np.cross(ab, ac)
        ab_cross_ac_norm_sq = np.dot(ab_cross_ac, ab_cross_ac)
        if ab_cross_ac_norm_sq == 0:
            # Points are colinear, return a point and radius of infinity
            return a, np.inf
        ab_norm_sq = np.dot(ab, ab)
        ac_norm_sq = np.dot(ac, ac)
        circumcenter = a + (np.cross(ab_norm_sq * ac - ac_norm_sq * ab, ab_cross_ac) / (2 * ab_cross_ac_norm_sq))
        # Calculate the radius of the circumcircle
        radius = np.linalg.norm(circumcenter - a)
        # Check if the circumcenter lies inside the triangle
        if np.all(np.logical_and(circumcenter >= a, circumcenter <= c)):
            return circumcenter, radius
        # Otherwise, the minimum enclosing sphere is the circumcircle
        else:
            center = np.mean(triangle, axis=0)
            radius = np.max(np.linalg.norm(triangle - center, axis=1))
            return center, radius
    def _min_sphere(points, center, radius):
        if len(points) == 0 or len(center) == 3:
            if len(center) == 3:
                # c1, c2, c3 = center
                # return np.array([(c1 + c2 + c3) / 3]), 0
                return minimum_enclosing_sphere_3points(center)
            elif len(center) == 2:
                c1, c2 = center
                return (c1 + c2) / 2, np.linalg.norm(c1 - c2) / 2
            elif len(center) == 1:
                return center[0], 0
            else:
                return None, 0
        else:
            p = points[0]
            points = points[1:]
            c, r = _min_sphere(points, center, radius)
            if c is None or np.linalg.norm(p - c) > r:
                center.append(p)
                c, r = _min_sphere(points, center, radius)
                center.pop()
            return c, r

    if len(points) < 4:
        raise ValueError("At least 4 points are required.")
    np.random.shuffle(points)
    center, radius = _min_sphere(points, [], 0)
    print("Center:", center)
    print("Radius:", radius)
    return center, radius


