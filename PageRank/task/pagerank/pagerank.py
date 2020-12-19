import numpy as np
import numpy.linalg as la
from io import StringIO


def pagerank(link_matrix, d) -> np.ndarray:
    n = link_matrix.shape[0]
    r = 100 * np.ones(n) / n
    J = np.ones((n, n))
    M = (d * link_matrix) + (((1 - d) / n) * J)
    r_prev = r
    r_next = M @ r
    while la.norm(r_prev - r_next) > 0.01:
        r_prev = r_next
        r_next = M @ r_next
    return r_next


if __name__ == '__main__':
    first = 5
    d_in = 0.5
    n_in = int(input())
    cites_in = input().split()
    cites = {cites_in[key]: key for key in range(n_in)}
    l_in = []
    for i in range(n_in):
        l_in.append(list(map(float, input().split())))
    l_in_np = np.array(l_in)
    query = input()
    s = StringIO()
    pr = pagerank(l_in_np, d_in)
    np.savetxt(s, pr, fmt="%.3f")
    for _ in cites.keys():
        cites[_] = pr[int(cites[_])]
    cites_sorted = dict(sorted(cites.items(), key=lambda x: (x[1], x[0]), reverse=True))
    if query in cites_sorted.keys():
        print(query)
        del cites_sorted[query]
        first -= 1
    first_5 = {k: cites_sorted[k] for k in list(cites_sorted)[:first]}
    for _ in first_5:
        print(_)


"""
    previous stages
    
    r = 100 * np.ones(7) / 7
    # r = L2 @ r

    s = StringIO()
    np.savetxt(s, L2, fmt="%.3f")
    print(s.getvalue())
    #s2 = StringIO()
    # for i in range(10):
    #    r = L2 @ r
    # np.savetxt(s2, r, fmt="%.3f")
    # print(s2.getvalue())
    r_prev = r
    r_next = L2 @ r
    while la.norm(r_prev - r_next) > 0.01:
        r_prev = r_next
        r_next = L2 @ r_next
    s3 = StringIO()
    np.savetxt(s3, r_next, fmt="%.3f")
    print(s3.getvalue())
    J = np.ones((7, 7))
    d = 0.5
    M = (d * L2) + (((1 - d) / 7) * J)
    r_prev = r
    r_next = M @ r
    while la.norm(r_prev - r_next) > 0.01:
        r_prev = r_next
        r_next = M @ r_next
    s4 = StringIO()
    np.savetxt(s4, r_next, fmt="%.3f")
    print(s4.getvalue())
    #e_values, e_vectors = la.eig(L)
    #vectors1 = np.transpose(e_vectors)[0]
    #vectors_norm = vectors1 * 100 / sum(vectors1)
    #np.savetxt(s, vectors_norm.real, fmt="%.3f")"
"""
