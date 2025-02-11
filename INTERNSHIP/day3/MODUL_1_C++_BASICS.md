C++ for Robotics

# Chapter 1: C++ Basics

## Summary

Estimated time to completion: **5 hours**.

In this unit you are going to learn how to create variables in C++, which types of variables you can create, and how you can operate with those variables. Remember that variables are like storage space for interesting data. We are going to use variables to store sensor data and manipulate it to understand the current situation of the robot. Additionally, you will learn how to add comments to the code.

---

In this course, we want to keep the focus on C++, not on ROS.

However, in order to be able to interact with the simulated robot while hiding all the ROS stuff, we are providing you with a C++ class in charge of managing all the ROS connections under the hood. This class is called RosbotClass. So, during this course, you will be interacting with this C++ class by calling its methods to get data from the robots and send commands to them.

It is very important that you remember that C++ is a compiled language, so every time we make changes to our code we'll need to first compile it and then execute it, in order to see the changes in the simulation.

First, for the purpose of this course we have created helpful programs you'll interact with in the following exercises. To download these exercises into your workspace open a shell and execute the following commands:

```bash
cd ~/catkin_ws/src/
```

```bash
git clone https://bitbucket.org/theconstructcore/cpp_course_repo.git
```

After this you should see the folders `/rosbot_control`, `/c_scripts` and `/utilities` appear in your catkin workspace.

## 1.1 Compile and execute C++ programs

C++ programs can be a little tricky to execute. First of all, for a program written in C++ the name of the file has to be something like name.cpp, where the extension .cpp specifies the programming language we are using.

Second of all, we need a compiler to compile the code (that would be **g++**), and also a name for the compiled code, for example name_compiled, without extension.

Let's see a quick example. Open a shell, go to the utilities folder by typing:

```bash
cd ~/catkin_ws/src/cpp_course_repo/utilities/
```

Then create an empty file that we will call `name.cpp`, by typing:

```bash
touch name.cpp
```

Then open the IDE, is your new file inside the folder /utilities?

Good!

Now paste the following code:

```cpp
#include <iostream>

int main() {
    printf("Hello, ROS developer!   \n");

    return 0;}
```

Once our code is ready we need to first compile it with G++ compiler. Go back to the shell and type:

```bash
g++ -std=c++11 name.cpp -o name_compiled
```

With this command we are telling the compiler g++ to use its version c++11, take the code in name.cpp and compile it in an executable file called name_compiled.

To see the code working we only need to call the executable file by typing:

```bash
./name_compiled
```

Did the message Hello, ROS Developer! appear on the shell?

Awesome!!

Now you know which is the easiest way to have a C++ file executed.

Let's see how can we create code that interacts with a robot, and how can ROS handle this C++ compilation for us.

## 1.2 Compile and execute C++ programs in ROS

Let's begin the unit with a practical exercise. You'll see how a C++ program can be compiled and executed and how it interacts with the ROS robot you see in the simulation.

### - Exercise 1.1 -

The directory **/c_scripts** is a typical ROS package which, for now, you only need to know that is a folder that stores configuration files, links to libraries, and the programs we want to use.

Inside the **src** folder, you will see that there are several empty cpp files, one for each unit.

Open the file `unit1_exercise.cpp` and copy the below code:

```cpp
#include "rosbot_control/rosbot_class.h"
#include <ros/ros.h>

using namespace std;

int main(int argc, char **argv) {
  ros::init(argc, argv, "rosbot_node");

  RosbotClass rosbot;
  rosbot.move();

  float coordinate = rosbot.get_position(1);

  ROS_INFO_STREAM(coordinate);

  return 0;
}
```

This `c_scripts` package already has instructions to compile the program we just edited when compiling the whole workspace. In order to see the changes we'll need to compile the catkin workspace with the following commands:

```bash
cd ~/catkin_ws
```

```bash
catkin_make
```

```bash
source devel/setup.bash
```

If the compiling is succesfull we can run our program by doing:

```bash
rosrun c_scripts unit1_exercise
```

Expected output:

You should see the robot moving, and also sending laser values in the shell.

---

So... what just happened? Let's try to explain it.

### **Code explanation**

**Including libraries**

The first thing we can see in the program is the following line:

```cpp
#include "rosbot_control/rosbot_class.h"
```

This C++ line includes a header file named rosbot_class.h from the rosbot_control directory.

The #include directive is a preprocessor directive that tells the compiler to include the contents of the specified header file in the source code file.

By including the rosbot_class.h header file, the C++ program can access the classes, functions, and variables defined in that header file. In this case the rosbot_class.h file contains the class definition and implementation for a class called RosbotClass which we will use to make the robot move.

```cpp
#include <ros/ros.h>
```

This line of C++ code includes the ROS (Robot Operating System) header file ros.h from the ros package, we import this library to make use of the classes and functions that ROS provides.

Note that when including header files, we use " " (quotes) or < > (angle bracket) syntax. Using <> tells the preprocessor to search the usual location for system headers in order to find the required header, whereas using "" tells the preprocessor to first search the directory where the current file is located before searching the usual path for system headers.

```cpp
using namespace std;
```

This line means that we can use the code in the std namespace without typing std:: before it. For example, we can write cout instead of std::cout. We will explain it more in detail later in 1.5.3 Namespace.

**Initialize a ROS node**

```cpp
int main(int argc, char **argv) {
```

C++ needs its programs to be initialized with the int main() line. Going into the details of int main(int argc, char \*\*argv) is beyond the scope of this course. For now, it is sufficient to say that this line of code is necessary to create the main function, which is a required function in any C++ program. This line of code also marks the beginning of the c++ program, the lines that are below this line indicate the actions that will be run.

```cpp
  ros::init(argc, argv, "rosbot_node");
```

By calling ros::init(), the C++ program creates a ROS node with the specified name, in this case rosbot_node and establishes a connection with the ROS master node. This line of code is typically included at the beginning of any ROS program.

**Creating an instance of an object**

```cpp
  RosbotClass rosbot;
  rosbot.move();
```

Then, we are going to create an object called rosbot that will have all the properties of the class RosbotClass. Later in this course you will learn some of the methods of this class and what we they can be used for. For instance, you will learn that you can call a method of this class named move() which will allow us to move the robot forward for two seconds.

**Calling a class method**

A method is a function that belongs to a class and is executed or 'called' just like a regular function, except that we must prepend the name of the instance of an object to the method name.

```cpp
  float coordinate = rosbot.get_position(1);
```

Finally, we are calling the get_position() method provided by the RosbotClass class. This method gives us the position of the robot in x, y and z coordinates. In this particular case, passing number 1 to the method means we are asking for the coordinate x, number 2 for coordinate y and number 3 for coordinate z.

Note that we are unable to observe the internal workings of this method. We can only engage with its input, which is the passing parameter, and its output, which is the float result. However, in a different package within the RosbotClass library, this method acquires values from the robot's odometry and transmits them to us.

What are these odometry values, and how can the robot give them to us?

Well, first of all our robot is a model RosBot like the one in this picture:

It can move thanks to its motors attached to each one of its wheels. Our robot is smart, it has an onboard computer that can store information and bring our commands to the motor wheels. Also, the wheels have a measurement system called encoders that store how many times they rotate. With this data the onboard computer is able to estimate the velocity of the robot, and using the measured time, it is also able to estimate the Odometry data.

Odometry are the values of the current position of the robot, which means its coordinates x,y,z in space, also its orientation according to the worlds axis, and its velocity. As it is a wheeled robot, it can move frontwards and backwards, so it has a linear velocity v, and it can turn left or right, so it has an angular velocity w.

ROS makes it easy to obtain this odometry data with a Subscriber, so we can consume it with our programs. In this case, our method get_position() has a list with the coordinates x,y,z and we can choose with the passing parameter which one of them we need.

**Getting the output of a method**

Also, when calling the specified method we are receiving a value that must be stored somewhere. That somewhere is the variable coordinate.

C++ is very demanding, it needs us to specify every type of variable we are using, even before using it. So in this case, in the same line we can initialize the variable coordinate as type float (you'll see later what this type means) and we assign it the value given by the method get_position().

All this programming is much easier when using the IDE, it sets different colors for types of variables, names of variables, classes, etc. We'll see in the next units.

**Print the results**

```cpp
  ROS_INFO_STREAM(coordinate);
```

In this case we use the ROS_INFO_STREAM macro to print a message to the console (and log it using ROS's logging system). This macro is part of the ROS library and it takes one argument, which is the message to be printed/logged. In this case, the coordinate variable is being passed as the message to be printed/logged.

**Return code of the C++ program**

```cpp
  return 0;
```

In a C++ program, return 0; is used to indicate the successful completion of the program.

Remember that the main function of a program is defined as int main(), which means that it is expected to return an integer value. The integer value returned by the main function is called the exit status or return code of the program. return 0; is for success and return 1; or other numbers for failures.

## 1.3 Variables

A variable can be seen as a container that stores some data: it can be a number, text, or more complex data types.

While our program is being executed variables can be accessed or even changed, which means that a new value will be assigned to the variable.

In a C++ language a variable has to be first declared and then assigned with a number, a sentence, a set of numbers, or others.

See an example of declaring some variables:

```cpp
int a;
a = 3;
```

The variable can change its value during the program but not its type. If it was written as an number, it can not be changed into text for example.

```cpp
a = 5;              // allowed
a = 'Hello';        // not allowed
```

### - Exercise 1.2 -

Let's put it in practice!

First, you'll take the same program we are using (unit1_exercise.cpp) and modify it to take these actions:

1. Get the x and y coordinates of the robot by calling twice at the function get_position() and print them together (Hint: remember to give different names to the results of x and y)
2. Make the robot move by calling the function move(), which needs no parameters, and gives no results.
3. Get the new x and y coordinates of the robot.

Remember to compile and execute the file as explained in section 1.2.

### - Solution of Exercise 1.2 -

Please try to do it by yourself unless you get stuck or need some inspiration. You will learn much more if you fight for each exercise.

```cpp
#include "rosbot_control/rosbot_class.h"
#include <ros/ros.h>

using namespace std;

int main(int argc, char **argv) {
  ros::init(argc, argv, "rosbot_node");

  RosbotClass rosbot;
  rosbot.move();

  float x_1 = rosbot.get_position(1);
  float y_1 = rosbot.get_position(2);

  ROS_INFO_STREAM(x_1 << " and " << y_1);

  rosbot.move();

  float x_2 = rosbot.get_position(1);
  float y_2 = rosbot.get_position(2);

  ROS_INFO_STREAM(x_2 << " and " << y_2);

  return 0;
}
```

## 1.4 Data types

As you've seen, you can create and manipulate variables quite easily, but C++ can be very picky to work with if you don't understand which data type should we use in each case!

There are various data types in C++. For this chapter, we are going to introduce just some of the most important ones.

- Booleans
- Numbers: integers, doubles and floats
- Strings
- Lists
- Dictionaries

NOTE:

All the examples we'll see that do not involve ROS commands, can be tested in a .cpp file in the /utilities folder, as explained in section 1.1

**Booleans**

Booleans can be expressed in C++ as bool, and they are a logic data type which can take the values true or false.

We'll see in later units that they are really useful to make conditions and logic statements in our code.

**Numbers: integers, doubles and floats**

Inside the numbers data type, we can divide into different types of numbers. For now, let's just differentiate into integers (int), doubles (double) and floats (float).

The first ones are integer values, for example 3. If we have numbers with decimals we'll use floats or doubles, depending on how many decimals of precision we need, Floats can have up to 7 decimals, and doubles up to 15 decimals of precision.

```cpp
int a = 3;                    // This is an integer

float b = 0.23;               // This is a float

double c = 0.225678391734;    // This is a double
```

**Strings**

Inside the text data type, we can divide into two different types: characters (char) and strings (string). In this language they all need to be represented inside double quotes (" ").

The first ones are sequences of characters that must have a fixed length, for example "hello". In this case we would have to initialize the variable as a character of length 6, one more of the letters it has.

```cpp
char d[6] = "hello";           // This is a collection of chars
```

Strings are also sequences of characters but with no fixed length. We would initialize them without specifying the length. For example:

```cpp
string e = "developer";
```

Strings can be subscripted or indexed. The first character of a string has the index 0. So, for instance, if we had the following code snippet:

```cpp
char d[6] = "hello";

string e = "developer";

cout << d[0] << endl;        // Print function
cout << e[4] << endl;        // Print function
```

The first print function (we'll later see what exactly is a print function) will show us in the shell the character in the position 0 of the variable d: the letter h of hello.

The second print function will show us in the shell the character in the position 4 of the variable e: the letter l of developer.

Finally, we can also concatenate different string to make a sentence for example:

```cpp
string f = ", ";
string g = "!";

cout << d+f+e+g << endl;     // Print function
```

**Lists**

In C++ lists are ordered sequences of variables of the same type. To initialize them we have to specify which type are the variables inside it. For example, for a list of integer values:

```cpp
list<int> numbers_list({1,10,100,1000});
And a list of string values:
```

```cpp
list<string> vocals_list( {"a","e","i","o","u"} );
```

The inconvenience with lists in C++ is that they are not as easy to print as in other languages. In this case we need to loop over all the items in a list to print them one by one. Don't worry, we'll se in later units how to implement a loop.

For now, here's an example of printing a list:

```cpp
for (int val : numbers_list)             // Loop
    cout << val << "  ";                 // Print function


for (string val : vocals_list)           // Loop
    cout << val << "  ";                 // Print function
```

Lists are very useful, as they occupy a memory space that can be modified. They have builtin functions to, for example, add a new item in the beginning of the list, or at the end of it:

```cpp
numbers_list.push_front(0);             //insert in the beginning
numbers_list.push_back(3000);           //insert in the end
The resulting list would be
0
,
1
,
10
,
100
,
1000
,
3000
```

Finally, we can also concatenate a list at the end of another, enlarging the first one and not deleting the second one, with the builtin function insert():

```cpp
list<int> new_list({5,50,500});

numbers_list.insert(numbers_list.end(),new_list.begin(),new_list.end());
Then the numbers_list will be modified as
0
,
1
,
10
,
100
,
1000
,
3000
,
5
,
50
,
500
```

**Dictionaries**

A dictionary in C++ is called a map, and it is a container of values that are indexed by a key. This means that it stores two kinds of information: keys and values.

For example, if we want to store the names of a TV series characters and also in how many episodes they appear, we don't need a list with the names and a list with the number of episodes, we just need a dictionary where the keys are the names and the values are the number of episodes:
{ "Dolores": 30, "Maeve": 27, "Theresa":6, "Clementine":11 }

To initialize it we need to call map, and specify the data types of the keys and values:

```cpp
map<string,int> girls_dictionary;
```

Here we are creating a dictionary called girls_dictionary, where the keys are strings and the values are integers.

To insert data into this dictionary we can call each key and assign it a value, one by one:

```cpp
girls_dictionary["Dolores"] = 30;
girls_dictionary["Maeve"] = 27;
girls_dictionary["Theresa"] = 6;
girls_dictionary["Clementine"] = 11;

for (auto item : girls_dictionary)
    cout << item.first << " appears in " << item.second << " episodes\n";
```

Finally, we can print the items in the dictionary with a loop that will give:
Clementine appears in 11 episodes

Dolores appears in 30 episodes

Maeve appears in 27 episodes

Theresa appears in 6 episodes

As you can see when we print it this is not a list, the dictionary itself organizes the keys alphabetically.

- Exercise 1.3 -
  Let's put in practice all these data types we just learned!

In this exercise we are going to create a dictionary that will store the x position of the robot over time, and print it in the shell.

First, modify the program unit1_exercise.cpp of the previous exercise to get the x coordinate of the robot by calling the get_position() method, and also get the time of simulation by calling the get_time() method. Note that get_position() and get_time() are methods of the RosbotClass and you need to type rosbot.get_time() instead of just get_time() which is what you would write to call a regular function. (Hint: the timestamp will have a data type of double).

Then, make the robot move by calling the method move() which also belongs to the RosbotClass class.

Repeat step 1: take the x position and the timestamp.

Instead of printing them in the shell, you will initialize a dictionary and store the time obtained as a key, and the x position as a value. Do it for all the values you obtained of x, 1 time, 2 times, .. , as many as you want.

Print the dictionary with the code provided in the Dictionaries section.

Remember to compile and execute the file as explained in section 1.2.

NOTE:

You'll need to include some libraries at the top of your program, to make the map and print work properly. Paste this code on the top of your program unit1_exercise.cpp:

#include <string>
#include <list>
#include <iostream>
#include <map>

using namespace std;

- End of Exercise 1.3 -
- Solution of Exercise 1.3 -
  Please try to do it by yourself unless you get stuck or need some inspiration. You will learn much more if you fight for each exercise.

  unit1_exercise.cpp

#include "rosbot_control/rosbot_class.h"
#include <iostream>
#include <list>
#include <map>
#include <ros/ros.h>
#include <string>

using namespace std;

int main(int argc, char \*\*argv) {
ros::init(argc, argv, "rosbot_node");

RosbotClass rosbot;
rosbot.move();

float x_0 = rosbot.get_position(1);
double t_0 = rosbot.get_time();

ROS_INFO_STREAM(x_0 << " and " << t_0);
rosbot.move();

float x_1 = rosbot.get_position(1);
double t_1 = rosbot.get_time();
ROS_INFO_STREAM(x_1 << " and " << t_1);

map<double, float> x_t_dictionary;
x_t_dictionary[t_0] = x_0;
x_t_dictionary[t_1] = x_1;

for (auto item : x_t_dictionary) {
ROS_INFO_STREAM("Time " << item.first << ", position " << item.second
<< " \n");
}

return 0;
}

- End of Solution of Exercise 1.3 -
  1.5 I/O functions
  1.5.1 Print
  In this chapter, we have already mentioned the function print. Basically, this function is used to write into the standard output of the program. This is especially useful for communicating with the user that is interacting with the program, to let him know what's going on, but it's also very useful when we want to debug our own programs.

In C++ there are multiple ways to implement a print, but in this chapter we have seen two of them:

printf
cout
The first one is a function that needs the type of the variable to be printed. For example, if we want to print an integer, we specify it with the symbol %i, if it's a float with %f, and if it's a string with %s. In the particular case of printing a string, it needs to be converted to a character by the function c_str().

Finally, it also needs to be accompanied by the include of the class iostream.

#include <iostream>
using namespace std;

int main(){

    int a = 42;
    printf("Value a is %i \n",a);            // Print an integer
    float b = 3.1415;
    printf("Value a is %f \n",b);            // Print a float
    string word = "Hey you!";
    printf("- %s \n",word.c_str());           // Print a string

    return 0;}

The second one is an object that refers to Character OUTput (COUT), which needs to be accompanied by the include of the class iostream, the importing of namespace std (we'll see what this means later), and the symbol <<.

For example:

#include <iostream>
using namespace std;

int main(){

    cout << "Are you enjoying this course? \n";     // Print a sentence
    string answer = "Of course!";
    cout << "Answer is " << answer;                  // Print a variable

    return 0;}

It can also be accompanied by the command endl to jump a line at that point:

#include <iostream>
using namespace std;

int main(){

    cout << "Nice!" << endl;
    cout << "Let's get back to work then" << endl;

    return 0;}

It is important to know also, that ROS has its own builtin functions to print data in the shell. In later examples you'll see the use of the functions ROS_INFO and ROS_INFO_STREAM, which essentially have the same purpose as cout, but they also give information about the time of the events it is printing.

1.5.2 Input
In the same way that you may want to write messages to the user who is executing your program, you might also want to ask this user to provide some data to your program. In fact, all programs need to communicate with the environment or "outside world" (usually a user). In programming, this is usually known as I/O (input/output) functionalities.

As we've already seen, the output in this case would be the cout function, which is the recommended one to use, while the input would be performed by the cin function. This cin function reads data from the keyboard. Check out the following example:

```cpp
#include <iostream>
using namespace std;

int main(){

    int x;
    cout << "How old are you? ";
    cin >> x;
    cout << "You are " << x << " years old";

    return 0;}
```

First, we need to initialize the variable where we'll store the data inserted by the user from the keyboard, then ask a question with cout, and finally get the user input from the keyboard.

From this point, this input can be used in our program as the variable x.

It is important to see that the cin function stops the program until the user has typed in the keyboard and pressed enter or a space key is inserted. Let's see an example with a string:

```cpp
#include <iostream>
using namespace std;

int main(){

    string name;
    cout << "What's your name? ";
    cin >> name;
    cout << "Nice to meet you " << name << "!";

    return 0;}
```

Remember to practise with this commands in a cpp file. Use the explanation of the section 1.1 to create a cpp file in the folder /utilities and compile and execute it.

You will see that the code above works as long as you introduce only 1 word (ie. the 1st name). If you try to introduce another word (ie. your 2nd name), this code won't work.

In case you want to capture more than a single word, you can use the following code instead:

getline(cin, name);
1.5.3 Namespace
C++ has a particular feature called namespaces. They allow us to group named entities into a single scope. That way, they will only have a meaning inside that namespace. Also, we can repeat names of variables, but always inside different namespaces.

In practice, we are not going to develop one of them here. We're just going to explain the one we've been using in this chapter: std

using namespace std;
This line allows us to use all the names inside the namespace std, which so far have been:

string
cout
cin
endl
From now on, if we need to use these, we'll add the line of using namespace std.

1.6 Operators
In C++, operators are used to perform operations on variables and values. We can divide the operators into the following basic groups:

Arithmetic Operators
Assignment Operators
Comparison Operators
Logical Operators
Arithmetic Operators

For example:

int a = 4;
int b = 3;

cout << a+b << endl;
cout << a-b << endl;
cout << a\*b << endl;
cout << a/b << endl;
cout << a%b << endl;
Assignment Operators

For example:

int x = 5;

cout << (x += 2) << endl;
cout << (x -= 2) << endl;
cout << (x \*= 2) << endl;
cout << (x /= 2) << endl;
cout << (x %= 2) << endl;
Comparison Operators

For example:

int y = 9;
int z = 8;

cout << (y==z) << endl;
cout << (y>z) << endl;
cout << (y<z) << endl;
cout << (y>=z) << endl;
cout << (y<=z) << endl;
This operator will return a true or false depending of the conditions.

- Exercise 1.4 -
  You are almost done with this chapter!

Let's try a final exercise to put in practice the operators in C++. In this exercise you are going to reuse the code from the previous one, so open the IDE, go to the folder /catkin_ws/src/cpp_course_repo/c_scripts/src and edit your previous unit1_exercise.cpp.

This program now has to perform three actions:

First obtain the measure of time and position x with the functions get_time() and get_position(), and store them in variables. Then make the robot move, and obtain again the time and position x storing them in different variables.

Second, calculate the mean speed of the robot in that period, by applying the formula
v
(
m
/
s
)
=
x
1
−
x
0
t
1
−
t
0

Third, print (using ROS_INFO_STREAM) a true value if the mean speed is lower than 1 m/s

Note!

Remember that in order to use all these functions, you first need to create the object rosbot by doing:

> RosbotClass rosbot;
> and make it move:

> rosbot.move();

- End of Exercise 1.4 -
- Solution of Exercise 1.4 -
  Please try to do it by yourself unless you get stuck or need some inspiration. You will learn much more if you fight for each exercise.

  unit1_exercise.cpp

#include "rosbot_control/rosbot_class.h"
#include <iostream>
#include <ros/ros.h>

using namespace std;

int main(int argc, char \*\*argv) {
ros::init(argc, argv, "rosbot_node");

RosbotClass rosbot;
rosbot.move();

float x_0 = rosbot.get_position(1);
double t_0 = rosbot.get_time();

rosbot.move();

float x_1 = rosbot.get_position(1);
double t_1 = rosbot.get_time();

float speed = (x_1 - x_0)/(t_1 - t_0);
ROS_INFO_STREAM("Speed is lower than 1 m/s? " << (speed<=1.0) << "\n");

return 0;
}

- End of Solution of Exercise 1.4 -
  1.7 Comments
  In programming, it is very common to add comments to your code. Comments are, basically, the parts of the code that are never going to be executed. They are very helpful for making your code much more readable and understandable to third party users.

In C++, line comments are added using the // symbol, and block comments are added using /∗ to open and ∗/ to close:

// This is a comment

printf("This is a demo to show how to use comments in C++");

/_
This is also a comment,
in a block.
_/
1.8 Summary
In this chapter, we've reviewed a basic guide on how to get started in C++, the most important concepts of variables, builtin functions and comments. More important, we've explained how can you compile a C++ code and execute, inside and outside of ROS, so you'll be able to experiment on your own with this information.

Now, with all these concepts you are ready to start creating more complex C++ programs. So... what are you waiting for?
