#include <iostream>
#include <stdlib.h>
#include <string>
#include <windows.h>
#include <thread>

using namespace std;



void system_call(const char * command) {
	system(command);
	cout << "Thread Finished" << endl;
}


void main() {
	
	cout << "Welcome to myShell" << std::endl;
	

	while (1) {

		cout << "==> ";
		string command;
		
		getline(cin, command);
		string saved_command = command;
		const char* command_ptr2 = &saved_command[0];
		cout << (command_ptr2) << endl;
		char* command_ptr = &command[0];
		char* parsed_token = strtok_s(command_ptr, " ", &command_ptr);
		string token(parsed_token);

		
		if (token == "dir" || token == "help" || token == "vol" || token == "path" || token == "tasklist" || token == "notepad" || token == "echo" || token == "color" || token == "ping") {
			thread t1(system_call, command_ptr2);
			t1.join();
		}

		else if (token == "quit" || token == "exit") {
			
			break;
		}

		else continue;


	
	}

	cout << "Thanks for using myShell!" << endl;




}