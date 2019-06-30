cppCode= """
#include<iostream>
using namespace std;
int main(){
           cout<<'Hello";
           return 0 ;
}

"""

print(cppCode)
print(type(cppCode))

file  = open("/This PC/Downloads/Asdf", "r")

file.write(cppCode)


file.close()
print(">> CPP Code Written")
