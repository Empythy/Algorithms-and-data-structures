"""#include <bits/stdc++.h>
using namespace std;

int item_number, packge_volumn;
int volume, value, number;

int dp[20010];
int dp_prev[20010];
int monotone_queue[20010];

int main() {
    cin >> item_number >> packge_volumn;
    for (int i = 0; i < item_number; ++i) {
        memcpy(dp_prev, dp, sizeof(dp));
        cin >> volume >> value >> number;
        for (int j = 0; j < volume; ++j) {
            int head = 0, tail = -1;
            for (int k = j; k <= packge_volumn; k += volume) {
                if (head <= tail && (k - monotone_queue[head]) / volume > number)
                    head++;

                if (head <= tail)
                    dp[k] = max(dp[k], dp_prev[monotone_queue[head]] + (k - monotone_queue[head]) / volume * value);

                while (head <= tail && dp_prev[monotone_queue[tail]] - (monotone_queue[tail] - j) / volume * value<= dp_prev[k] - (k - j) / volume * value) {
                    --tail;
                }

                monotone_queue[++tail] = k;
            }
        }
    }
    cout << dp[packge_volumn] << endl;
}"""
dp = [0] * 20010
dp_prev = [0] * 20010
monotone_queue = [0] * 20010

n, m  = map(int, input().split())
for i in range(n):
    dp_prev = dp.copy()
    volume,value, number = map(int, input().split())