
// Comment

/*
multiline Comment
*/

use GarbageCollection; //turn on GarbageCollection subroutine

int my_int = 3; //variable definition
dynamic my_dynamic = "Hello World"; //set a dynamic variable to a string



class Program(){ //main Function executed on start
	int main(){ //create a new thread called main, returns int (= Error number or 0=Program end)
		output(my_dynamic); // print "Hello World"
		output(string(my_int + 4)); // print "7"
		return _PROGRAM_END; //_PROGRAM_END is a static built-in constant and equals 0
	}
}







