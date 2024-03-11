#!/usr/bin/node

class CustomObject {
  constructor(type, value) {
    this.type = type;
    this.value = value;
  }

  incr() {
    this.value++;
  }
}

const myObject = new CustomObject('object', 12);

console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

