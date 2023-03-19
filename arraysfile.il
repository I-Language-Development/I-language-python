


use GarbageCollection; 

import file; //importiere built-in bibliothek
?string[] mydata; //neue variable: array (string oder null)

class Program(){
	int main(){
		bool input_loop = true;
		while (input_loop){
			mydata.append(input("What to append? "));
				if (mydata[-1] == "quit"){
				mydata = mydata[:-1]; // array slicen
			}
		}
		dynamic this_file = file.open();
		for(int i; i<len(mydata);i++;){ //hier bin ich mir noch nicht sicher, ob das eine schöne syntax ist
			this_file.write_string(mydata[i]);
		}
		this_file.close()
		delete this_file; //muss nicht gemacht werden, da GarbageCollection an
		return _PROGRAM_END;
	}
}



