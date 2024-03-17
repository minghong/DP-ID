// ͼ��ѹ��

#include<bits/stdc++.h>

using namespace std;

int const n=256*256;
int p[n+1];
int s[n+1], l[n+1], b[n+1];

int length(int i)  //�������ص�p����Ҫ�Ĵ洢λ��
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
void Compress(int n, int p[], int s[], int l[], int b[])  //��s[i]Ϊǰi�������źϲ��Ĵ洢λ��
{
    int Lmax = 256, header = 11;
    s[0] = 0;
    for(int i=1; i<=n; i++)  //i��ʾǰ����
    {
        b[i] = length(p[i]); //�������ص�p��Ҫ�Ĵ洢λ��
        int bmax = b[i];
        s[i] = s[i-1] + bmax;  //������j��2��ʼ
        l[i] = 1;
        for(int j=2; j<=i && j<=Lmax; j++)   //���ƹ�ϵ:s[i]=  min(1<=j<=i)(lsum(i-j+1, i)<=256) {s[i-j]+ lsum(i-j+1,i)*bmax(i-j+1,i) } + 11
        {
            if(bmax < b[i-j+1])
                bmax = b[i-j+1];
            if(s[i] > s[i-j] + j*bmax)   //��Ϊһ��ʼ�������в�û�зֶ�,���Կ��Կ���ÿһ�ξ���һ����,��lsum(i-j+1, i) = j;
            {
                s[i] = s[i-j] + j*bmax;
                l[i] = j;   //���ŶϿ�λ��,l[i]��ʾǰi�ε����ŷֶη�����Ӧ������i-j���Ͽ�  ����l[5] = 3,���ʾǰ��ε����ŷֶ�Ӧ����(5-3=2)���Ͽ�,s[5] = s[2] + 3*bmax
                            //�� 12 | 345,�Դ�����,�õ�l[n];֮�������Ž�ʱ����l[n]��ǰ����
            }
        }
        s[i] += header;
    }
}
void Traceback(int n, int &m, int s[], int l[])
{
    if(n == 0) return;
    Traceback(n-l[n], m, s, l);
    s[m++] = n-l[n];  //����Ϊs[]���鸳ֵ�������洢�ֶ�λ��
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
	while (getline(in, line)){//��ȡ�ļ���һ���ַ�����line��
		stringstream ss(line);//��ʼ�� ��1
		int x;
		int i=1;
		while (ss >> x){//ÿһ�а�����ͬ����������

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

