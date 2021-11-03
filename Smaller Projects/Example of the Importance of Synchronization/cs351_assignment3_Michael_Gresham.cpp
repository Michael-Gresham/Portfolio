
#include <iostream>
#include <fstream>
#include <thread>
#include <mutex>

using namespace std;

mutex mtx;

void write_numbers(ofstream &myFile) {
	//Entering critical area so use mutex lock
	mtx.lock();
	for (int i = 0; i < 20; i++) {

		for (int j = 1; j < 27; j++) {
			myFile << j << " ";
		}

		myFile << endl;
	}
	mtx.unlock();
	//Exiting critical area so you can release the lock
}

void write_letters(ofstream& myFile) {
	//Entering critical area so use mutex lock
	mtx.lock();
	for (int i = 0; i < 20; i++) {

		for (int j = 97; j < 123; j++) {
			char ascii_char = j;
			myFile << ascii_char << " ";
		}

		myFile << endl;
	}

	mtx.unlock();
	//Exiting critical area so you can release the lock

}

int main() {

	ofstream myFile("Sync.txt");
	thread t1(write_numbers, std::ref(myFile));
	thread t2(write_letters, std::ref(myFile));
	t1.join();
	t2.join();
}