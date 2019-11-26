#include <iostream>
#include <sstream>

using namespace std;

// CHEEZ-IT GROOVES crispy cracker chips
//string VALID_HASH = "434845455a2d49542047524f4f5645532063726973707920637261636b6572206368697073";
string VALID_HASH = "ffffffbcffffffb7ffffffbaffffffbaffffffa5ffffffd2ffffffb6ffffffabffffffdfffffffb8ffffffadffffffb0ffffffb0ffffffa9ffffffbaffffffacffffffdfffffff9cffffff8dffffff96ffffff8cffffff8fffffff86ffffffdfffffff9cffffff8dffffff9effffff9cffffff94ffffff9affffff8dffffffdfffffff9cffffff97ffffff96ffffff8fffffff8c";

string hexify(unsigned char c)
{
	stringstream ss;

	ss << hex << (int)~c;

	return ss.str();
}

string hash(string password)
{
	string output = "";    

	for (int i=0; i<password.length(); i++)
	{
		output += hexify(password[i]);
	}

	return output;
}

int main()
{
	string password;

	cout << "Password: ";
	getline(cin, password);
//	cout << hash(password) << endl;
//	return 0;

	if (hash(password) == VALID_HASH)
		cout << "SUCCESS!\n";
	else
		cout << "FAILURE.\n";
}
