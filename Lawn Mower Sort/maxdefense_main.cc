
#include <cassert>
#include <sstream>

#include "maxdefense.hh"
#include "timer.hh"
#include <iostream>
#include "rubrictest.hh"

using namespace std;





int main()
{



	ArmorVector trivial_armors;
	trivial_armors.push_back(std::shared_ptr<ArmorItem>(new ArmorItem("test helmet", 100.0, 20.0)));
	trivial_armors.push_back(std::shared_ptr<ArmorItem>(new ArmorItem("test boots", 40.0, 5.0)));

	auto all_armors = load_armor_database("armor.csv");
	//assert(all_armors);



	Timer timer;

		int size = 1000;
		auto filtered_armors1 = filter_armor_vector(*all_armors, 1, 2500, size);
		//cout << "Current Size :  " << size << endl;
		
	
		auto best = dynamic_max_defense(*filtered_armors1, 6000);
	

	double elapsed = timer.elapsed();
	std::cout << "Elapsed time in seconds for Dynamic Algorithm " << elapsed << std::endl;

	return 0;
}