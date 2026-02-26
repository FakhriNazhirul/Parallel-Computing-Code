from multiprocessing import Process, Queue

def multiply_row(row, B, q, pid):
    result_row = []
    for col in zip(*B):
        result_row.append(sum(x*y for x, y in zip(row, col)))
    print(f"Proses {pid}: {result_row}")
    q.put(result_row)

if __name__ == "__main__":
    q = Queue()

    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    processes = []

    for i, row in enumerate(A):
        p = Process(target=multiply_row, args=(row, B, q, i+1))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    result = [q.get() for _ in A]

    print("Hasil Perkalian Matriks:")
    for r in result:
        print(r)