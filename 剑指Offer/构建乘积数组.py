class Solution:
    def multiply(self, A):
        # write code here

        arr1 = [1]
        """
        A[0]
        A[0] A[1]
        A[0] A[1] A[2]
        """
        n = len(A)
        for i in range(1, n):
            arr1.append(arr1[-1] * A[i])

        arr2 = [1]
        """
        .....
        A[n-3] A[n-2] A[n-1]
        A[n-2] A[n-1]
        A[n-1]
        """
        for i in range(n-1, 0):
            arr2.insert(0, arr2[0] * A[i])
        B = []
        for i in range(n-1):
            B.append(arr1[i] * arr2[i])
        return B

if __name__ == '__main__':
    A = [1,2,3,4,5]
    s = Solution()
    s.multiply(A)
