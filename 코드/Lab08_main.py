from Lab08 import*
import sys
import heapq

#1
def testDijkstra():
    sssp = SSSP()
    distances = sssp.runDijkstra(graph, 'A')

    print("Distances:")
    for vertex, distance in distances.items():
        print(vertex, distance)


def main():
    testDijkstra()


if __name__ == '__main__':
    main()
