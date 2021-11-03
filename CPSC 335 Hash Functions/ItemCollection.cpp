#include <string>
#include <iostream>
#include <fstream>
#include <stdexcept>
#include "ItemCollection.hpp"

using std::string;
using std::ifstream;
using std::cout;
using std::endl;

// function to return the hash value based on the first digit
unsigned int hashfct1(unsigned int barcode) {
    barcode /= 1000000;
    barcode %= 10;
    return barcode;
}

// function to return the hash value based on the second digit
unsigned int hashfct2(unsigned int barcode) {
    barcode /= 100000;
    barcode %= 10;
    return barcode;
}

// function to return the hash value based on the third digit
unsigned int hashfct3(unsigned int barcode) {
    barcode /= 10000;
    barcode %= 10;
    return barcode;
}

// function to return the hash value based on the fourth digit
unsigned int hashfct4(unsigned int barcode) {
    barcode /= 1000;
    barcode %= 10;
    return barcode;
}

// function to return the hash value based on the fifth digit
unsigned int hashfct5(unsigned int barcode) {
    barcode /= 100;
    barcode %= 10;
    return barcode;
}

// function to return the hash value based on the fourth digit
unsigned int hashfct6(unsigned int barcode) {
    barcode /= 10;
    barcode %= 10;
    return barcode;
}

// function to return the hash value based on the fifth digit
unsigned int hashfct7(unsigned int barcode) {
    barcode /= 1;
    barcode %= 10;
    return barcode;
}


// Constructor for struct Item
Item::Item(string itemColor, string itemShape, string itemBrand,
		 unsigned int barcode):itemColor_(itemColor),itemShape_(itemShape), itemBrand_(itemBrand),
				       barcode_(barcode)
{};

// Load information from a text file with the given filename
// THIS FUNCTION IS COMPLETE
void ItemCollection::readTextfile(string filename) {
  ifstream myfile(filename);

  if (myfile.is_open()) {
    cout << "Successfully opened file " << filename << endl;
    string itemColor;
    string itemShape;
    string itemBrand;
    unsigned int barcode;
    while (myfile >> itemColor >> itemShape >> itemBrand >> barcode) {
			if (itemColor.size() > 0)
      	addItem(itemColor, itemShape, itemBrand, barcode);
    }
    myfile.close();
  }
  else
    throw std::invalid_argument("Could not open file " + filename);
}

void ItemCollection::addItem(string itemColor, string itemShape, string itemBrand, unsigned int barcode) {
  // TO BE COMPLETED
  // function that adds the specified pair of glasses to main display (i.e., to all hash tables)

    Item glasses = Item(itemColor, itemShape, itemBrand, barcode);    // create the glasses object.
    
    // Add each object into the hash table as a  <key, item> pair. The hash function will place them in hashfct#(barcode) index.
    hT1.insert(std::make_pair(glasses.barcode_, glasses));
    hT2.insert(std::make_pair(glasses.barcode_, glasses));
    hT3.insert(std::make_pair(glasses.barcode_, glasses));
    hT4.insert(std::make_pair(glasses.barcode_, glasses));
    hT5.insert(std::make_pair(glasses.barcode_, glasses));
    hT6.insert(std::make_pair(glasses.barcode_, glasses));
    hT7.insert(std::make_pair(glasses.barcode_, glasses));
    
}

bool ItemCollection::removeItem(unsigned int barcode) {
  // TO BE COMPLETED
  // function that removes the pair of glasses specified by the barcode from the display
  // if pair is found, then it is removed and the function returns true
  // else returns false

    //uses an iterator to search through each bucket/chain in hash table 1 (if its in 1 its in all of them) and if the glasses are found
    // it erases it from every hash table and returns true. If it does not find the glasses it then returns false.

    for (auto ptr = hT1.begin(hashfct1(barcode)); ptr != hT1.end(hashfct1(barcode)); ptr++ ) {  //ptr points the first pair(key, item) and iterates through the whole bucket untils it hits null (end).
       
        if (ptr->first == barcode) {   // the pair i used to insert was <key, item> where key was the barcode so I just need the first value. ptr->second.barcode would also work.
            hT1.erase(barcode);
            hT2.erase(barcode);
            hT3.erase(barcode);
            hT4.erase(barcode);
            hT5.erase(barcode);
            hT6.erase(barcode);
            hT7.erase(barcode);
            
            //deletion worked out therefore we return true.
            return true;


        }
    }

    return false;
}

//function thats added which is suppose to calculate the difference between the highest and lowest bucket.
unsigned int ItemCollection::calculateBalance(CustomHashTable table){

    unsigned int difference;
    unsigned int low = table.bucket_size(0);  // bucket_size() returns the amount of objects inside a bucket at a given index in the hash table.
    unsigned int high = table.bucket_size(0);

    for (unsigned i = 1; i < 10; i++) {       // we only care about the 0-9 buckets and since index at 0 is covered we iterate from 1 to 9.
        
        if (high < table.bucket_size(i)) {   // checks to see if current bucket size is greater than the current highest size and if it is then we set highest to the current bucket_size
            high = table.bucket_size(i);    
        }

        if (low > table.bucket_size(i)) {    // checks to see if current bucket size is less than the current lowest size and if it is then we set lowest to the current bucket_size
            low = table.bucket_size(i);
        }
    }


    difference = high - low;                 // calculates the difference between high and low bucket size.

    return difference;

}


unsigned int ItemCollection::bestHashing() {
  // TO BE COMPLETED
  // function that decides the best has function, i.e. the ones among
  // fct1-fct7 that creates the most balanced hash table for the current
  // ItemCollection data member allItems


    unsigned int best_table;
    unsigned int best_difference;
    unsigned int current_difference;
    unsigned int balances[8];           //used an array so I don't have to use if statements for each hash table and instead just use a for loop and one if statement 


    // assign the balance of each hash table in the array corresponding to their hash table number.
    balances[1] = calculateBalance(hT1);
    balances[2] = calculateBalance(hT2);
    balances[3] = calculateBalance(hT3);
    balances[4] = calculateBalance(hT4);
    balances[5] = calculateBalance(hT5);
    balances[6] = calculateBalance(hT6);
    balances[7] = calculateBalance(hT7);
    
    //to start up we arbitary set the best to hash table 1. As setting it as a random number can lead to issues.
    best_table = 1;
    best_difference = balances[1];    

    for(int i = 2; i < 8; i++){  // hash table 1 is done so we only iterate through hash tables 2-7.    
        
        current_difference = balances[i];  

        if(current_difference < best_difference){
            best_table = i;
            best_difference = current_difference;
        }
    } 

    return best_table;   // ends by returning the most balanced hash_Table.
}

// ALREADY COMPLETED
size_t ItemCollection::size() {
    if ((hT1.size() != hT2.size()) || (hT1.size() != hT3.size()) || (hT1.size() != hT4.size()) || (hT1.size() != hT5.size())|| (hT1.size() != hT6.size()) || (hT1.size() != hT7.size()))
  	    throw std::length_error("Hash table sizes are not the same");
    
	return hT1.size();
}
