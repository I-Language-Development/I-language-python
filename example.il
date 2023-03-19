/*
* EXAMPLE SYNTAX
*
* NOTE:
* This version is a in-development version and may be changed in the future
*/

// Comment

/*
multiline Comment
*/

// Imports:
// import MODULE
// or with custom names
// import MODULE as NAME
// or jsut importing some things
// import THING from MODULE [as NAME]

// Variables:
// var NAME = EXPRESSION // dynamic tying, also works as type "dynamic"
// or with types assigned at start
// TYPE NAME = EXPRESSION

// Constants:
// const [TYPE] NAME = EXPRESSION

// Classes:
// class NAME([SUBCLASS]) {
// CODE
// }


// Functions:
// [private] RETURN_TYPE NAME(ARGUMENT_TYPE ARGUMENT_NAME /* has to be consistent*/[= DEFAULT_VALUE]) {
// CODE
// }

// Calls to functions from a class:
// CLASS_NAME.NAME()

// Calls to functions:
// NAME(ARGUMENT)

// Print to stdout
// output(VALUE) // Value can be anything, it's representation will be used

// Use garbage collection // I had this as USE because its a subroutine manipulating the parser and not an Object
// import GarbageCollection
// use GarbageCollection // This is very likely to change in the future

//How about the multithreading?
// We could make the 'program' class only needed for that // Good idea, I'll add this soon
