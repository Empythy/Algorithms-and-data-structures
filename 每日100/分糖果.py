class Solution:
    def distributeCandies(self, candies, num_people):
        used = (1+num_people)*num_people // 2
        cnt = 0
        while candies // used:
            cnt += 1
            candies = candies - used
            used = used + num_people*num_people
        last = candies
        if cnt > 0:
            arr = [i*cnt + (cnt-1)*cnt // 2 * num_people for i in range(1, num_people+1)]
        else:
            arr = [0] * num_people
        for i in range(num_people):
            if last - ((i+1)+ cnt * num_people) >= 0:
                arr[i] = arr[i] + (i+1) + cnt * num_people
                last = last - ((i + 1) + cnt * num_people)
            else:
                arr[i] = last + arr[i]
                break
        return arr

if __name__ == "__main__":
    s = Solution()
    candies = 80
    num_people = 4
    ret = s.distributeCandies(candies, num_people)
    print(ret)




