# python3

def parallel_processing(n, m, data):
    
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads =[(0, i) for i in range(n)]

    output = []

    for i in range(m):
        time = data[i]

        min_start_time = float('inf')
        min_thread_index = None
        for start_time, thread_index in threads:
            if start_time < min_start_time:
                min_start_time = start_time
                min_thread_index = thread_index

    output.append((min_thread_index, min_start_time))

    threads[min_thread_index] = (min_start_time + time, min_thread_index)

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int,input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_index, start_time in result:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()
