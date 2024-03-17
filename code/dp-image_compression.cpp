// 图像压缩

#include<bits/stdc++.h>

using namespace std;

int const n=256*256;
int p[n+1];
int s[n+1], l[n+1], b[n+1];

int length(int i)  //计算像素点p所需要的存储位数
{
    int k = 1;
    i = i/2;
    while(i>0)
    {
        k++;
        i = i/2;
    }
    return k;
}
void Compress(int n, int p[], int s[], int l[], int b[])  //令s[i]为前i个段最优合并的存储位数
{
    int Lmax = 256, header = 11;
    s[0] = 0;
    for(int i=1; i<=n; i++)  //i表示前几段
    {
        b[i] = length(p[i]); //计算像素点p需要的存储位数
        int bmax = b[i];
        s[i] = s[i-1] + bmax;  //故下面j从2开始
        l[i] = 1;
        for(int j=2; j<=i && j<=Lmax; j++)   //递推关系:s[i]=  min(1<=j<=i)(lsum(i-j+1, i)<=256) {s[i-j]+ lsum(i-j+1,i)*bmax(i-j+1,i) } + 11
        {
            if(bmax < b[i-j+1])
                bmax = b[i-j+1];
            if(s[i] > s[i-j] + j*bmax)   //因为一开始所有序列并没有分段,所以可以看作每一段就是一个数,故lsum(i-j+1, i) = j;
            {
                s[i] = s[i-j] + j*bmax;
                l[i] = j;   //最优断开位置,l[i]表示前i段的最优分段方案中应该是在i-j处断开  比如l[5] = 3,这表示前五段的最优分段应该是(5-3=2)处断开,s[5] = s[2] + 3*bmax
                            //即 12 | 345,以此类推,得到l[n];之后构造最优解时再由l[n]向前回溯
            }
        }
        s[i] += header;
    }
}
void Traceback(int n, int &m, int s[], int l[])
{
    if(n == 0) return;
    Traceback(n-l[n], m, s, l);
    s[m++] = n-l[n];  //重新为s[]数组赋值，用来存储分段位置
}
void Output(int s[], int l[], int b[], int n)
{
    cout<<"The optimal value is "<<s[n]<<endl;
    int m = 0;
    Traceback(n, m, s, l);
    s[m] = n;
    cout<<"Decompose into "<<m<<" segments "<<endl;
    for(int j=1; j<=m; j++)
    {
        l[j] = l[s[j]];
        b[j] = b[s[j]];
    }
    ofstream outfile("D:\\result.txt");
    for(int j=1; j<=m; j++)

        outfile << l[j] << " "<<b[j]<<endl;
    outfile.close();

}


void test()
{
	cout << "-----------test----------- " << endl;
	ifstream in("D:\\1.txt");
	string line;
	while (getline(in, line)){//获取文件的一行字符串到line中
		stringstream ss(line);//初始化 法1
		int x;
		int i=1;
		while (ss >> x){//每一行包含不同个数的数字

			p[i++]=int(x);
		}

	}
}


int main()
{


    test();
    Compress(n, p, s, l, b);
    int m=0;
    Traceback(n, m, s, l);
    Output(s, l, b, n);
    memset(p, sizeof(p), 0);


    return 0;
}

/*6
10 12 15 255 1 2*/

