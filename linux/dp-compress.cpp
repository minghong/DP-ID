#include<bits/stdc++.h>
using namespace std;

const int N = 256*256+1;
int p[N+1];
int length(int i);
void Compress(int n,int p[],int s[],int l[],int b[]);
int TraceBack(int n,int l[],int b[]);  
void Out(int m,int min_len,int l[],int b[]);
void test()
{
	cout << "-----------test----------- " << endl;
	ifstream in("matrix.txt");
	string line;
	while (getline(in, line)){
		stringstream ss(line);
		int x;
		int i=1;
		while (ss >> x){

			p[i++]=int(x);

		}

	}
}

int main()
{

    test();
    int s[N]={0},l[N]={0},b[N]={0};


    Compress(N-1,p,s,l,b);
    int m=TraceBack(N-1,l,b);
    Out(m,s[N-1],l,b);
    return 0;
}

void Compress(int n,int p[],int s[],int l[],int b[])
{
    int Lmax = 256,header = 11;
    s[0] = 0;
    for(int i=1; i<=n; i++)
    {
        b[i] = length(p[i]);
        int bmax = b[i];
        s[i] = s[i-1] + bmax + header;
        l[i] = 1;

        for(int j=2; j<=i && j<=Lmax;j++)  
        {

            if(bmax<length(p[i-j+1]))
            {
                bmax = length(p[i-j+1]);
            }

            if(s[i]>s[i-j]+j*bmax+header)
            {
                s[i] = s[i-j] + j*bmax+header;
                l[i] = j;
                b[i] = bmax; 
            }
        }
    }
}

int length(int i)
{
    int k=1;
    i = i/2;
    while(i>0)
    {
        k++;
        i=i/2;
    }
    return k;

}

int TraceBack(int n,int l[],int b[]) 
{
    stack<int>ss;
    ss.push(l[n]);
    ss.push(b[n]);
    while (n!=0)
    {
        n=n-l[n];
        ss.push(l[n]);  
        ss.push(b[n]);
    }
    int i=0;
    while (!ss.empty())
    {
        b[i]=ss.top();
        ss.pop();
        l[i]=ss.top(); 
        ss.pop();
        i++;
    }
    return i-1;
}

void Out(int m,int min_len,int l[],int b[])
{
    int i=0;
    cout<<"total_length："<<min_len<<endl;
    cout<<"total："<<m<<"segment"<<endl;
    ofstream outfile("signal_pixel.txt");
    for(int j=1; j<=m; j++)
    {
        outfile << l[j] << " "<<b[j]<<endl;
    }

    outfile.close();
}
