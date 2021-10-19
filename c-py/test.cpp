#include <iostream>

extern "C"{
	int x = 7;
	int y = 5;

	void hello(){
		std::cout << "helloworld from c++" << std::endl;
	}
};
