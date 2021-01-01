
#find max

def findMinRec(A, n):
    # if size = 0 means whole array
    # has been traversed
    if (n == 1):
        return A[0]
    return min(A[n - 1], findMinRec(A, n - 1))

if __name__ == '__main__':
    A = [1, 4, 45, 6, -50, 10, 2]
    n = len(A)
    print(findMinRec(A, n))

#find max
    def findMaxRec(A, n):
        if (n == 1):
            return A[0]
        return max(A[n - 1], findMaxRec(A, n - 1))


    if __name__ == "__main__":
        A = [1, 4, 45, 6, -50, 10, 2]
        n = len(A)
        print(findMaxRec(A, n))