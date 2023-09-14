// 2-hbtn_course.js
export default class HolbertonCourse {
  constructor(name, length, students) {
    // Verify the types of attributes during object creation
    if (typeof name === 'string') {
      // Store attributes in underscore attribute versions
      this._name = name;
    } else {
      throw TypeError('Name must be a string');
    }

    if (typeof length === 'number') {
      // Store attributes in underscore attribute versions
      this._length = length;
    } else {
      throw TypeError('Length must be a number');
    }

    if (Array.isArray(students) && students.every((student) => typeof student === 'string')) {
      // Store attributes in underscore attribute versions
      this._students = students;
    } else {
      throw TypeError('Students must be an array of strings');
    }
  }

  // Getter and setter for the 'name' attribute
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  // Getter and setter for the 'length' attribute
  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    } else {
      throw TypeError('Length must be a number');
    }
  }

  // Getter and setter for the 'students' attribute
  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (Array.isArray(newStudents) && newStudents.every((student) => typeof student === 'string')) {
      this._students = newStudents;
    } else {
      throw TypeError('Students must be an array of strings');
    }
  }
}
