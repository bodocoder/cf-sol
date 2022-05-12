#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define f(i,n) for(ll i=0;i<n;i++)
#define rf(i,n) for(ll i=n-1;i>=0;i--)
#define range(i,a,n) for(ll i=a;i<n;i++)
#define vll vector<ll>
const ll mod = 1e9+7;
void dfs(ll x, vll &vis, vector<vll> &g) {
    if(vis[x]) return;
    vis[x] = 1;
    for(ll y: g[x]) dfs(y, vis, g);
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    ll test=1;cin>>test;
    range(tc,1,test+1){
        ll n; cin>>n;
        vll a(n), b(n), c(n);
        vector<vll> g(n+1);
        f(i,n) cin>>a[i];
        f(i, n) cin>>b[i];
        f(i,n) cin>>c[i];
        f(i,n) {
            g[a[i]].push_back(b[i]);
            g[b[i]].push_back(a[i]);
        }
        vll vis(n+1, 0);
        f(i, n) {
            if(c[i] != 0) {
                dfs(c[i], vis, g);
            }
        }
        ll cyc =0;
        f(i, n) {
            if(a[i] == b[i] || vis[a[i]] || vis[b[i]]) continue;
            cyc++;
            dfs(a[i],vis,g);
        }
        ll ans = 1;
        f(i, cyc) {
            ans = (ans * 2) % mod;
        }
        cout<<ans<<"\n";
    }
    return 0;
}