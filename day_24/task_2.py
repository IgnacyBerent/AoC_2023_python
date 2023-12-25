import sympy as sp


def main(file: str):
    with open(file, 'r') as f:
        hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in f.readlines()]

    xr, yr, zr, vxr, vyr, vzr = sp.symbols("x, y, z, vx, vy, vz")
    equations = []
    for x, y, z, vx, vy, vz in hailstones:
        equations.append((x - xr) * (vyr - vy) - (y - yr) * (vxr - vx))
        equations.append((x - xr) * (vzr - vz) - (z - zr) * (vxr - vx))

    result = sp.solve(equations, xr, yr, zr, vxr, vyr, vzr)
    result = result[0]
    print(result[0] + result[1] + result[2])


if __name__ == '__main__':
    main('input.txt')
