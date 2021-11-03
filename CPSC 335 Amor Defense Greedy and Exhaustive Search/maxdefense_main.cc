
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
	
	



	for (int i = 1; i < 64; i++) {
		
		
		int size = i;
		auto filtered_armors1 = filter_armor_vector(*all_armors, 1, 2500, size);
		cout << "Current Size :  " << size << endl;
		Timer timer;
		//uto best = exhaustive_max_defense(*filtered_armors1, 6000);
		double elapsed;
		//std::cout << "Elapsed time in seconds for Exaushtive: " << elapsed << std::endl;

		//timer.reset();
		auto best = greedy_max_defense(*filtered_armors1, 6000);
		elapsed = timer.elapsed();
		std::cout << "Elapsed time in seconds for Greedy " << elapsed << std::endl;




	}
	
	return 0;
}


