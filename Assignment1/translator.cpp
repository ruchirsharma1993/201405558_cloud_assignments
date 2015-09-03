#include<iostream>
#include<fstream>
#include<map>
#include<vector>
using namespace std;
int main()
{
	ifstream in("in_32");
	ofstream out("out_64");
	map<string, string> map_data;
	vector<string> to_repl;

	//Init data
	to_repl.push_back("8");
	map_data["8"] = "16";

	to_repl.push_back("esp");
	map_data["esp"] = "rsp";

	to_repl.push_back("movl");
	map_data["movl"] = "movq";

	to_repl.push_back("pushl");
	map_data["pushl"] = "pushq";
	
	to_repl.push_back("ebp");
	map_data["ebp"] = "rbp";

	 
	string line;
	while(getline(in, line))
	{
		for(int i=0;i<to_repl.size();i++)
		{
			size_t f = line.find(to_repl[i]);
			if (f!=std::string::npos)
				line.replace(f, std::string(to_repl[i]).length(), map_data[to_repl[i]]);
		}
		out<<line;
		out<<endl;	
	}
	in.close();
	out.close();
	return 0;
}

	
