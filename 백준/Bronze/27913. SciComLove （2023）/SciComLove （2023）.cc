#include <iostream>
using namespace std;


int main(void)
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int cnt[202020] = { 0 }, N, Q, i, x, ans = 0;
    cin >> N >> Q;
    for (i = 1; i <= N; i++)
    {
        if (i % 10 == 1 || i % 10 == 4 || i % 10 == 7)
        {
            cnt[i] = 1;
            ans++;
        }
    }

    for (i = 0; i < Q; i++)
    {
        cin >> x;
        cnt[x]++;
        if (cnt[x] % 2 == 1) ans++;
        else ans--;

        cout << ans << "\n";
    }

}