#include "/Library/Frameworks/Python.framework/Versions/3.9/include/python3.9/Python.h"
#include <fstream>
#include <iostream>
using namespace std;

//PyBytes_AS_STRING
PyObject *mod;
static PyObject *_method_spaceout(){
    return PyObject_GetAttrString(mod,"space");
}
static PyObject *method_readfile(PyObject *self, PyObject *args){

    char* filename;

    if(!PyArg_ParseTuple(args, "s", &filename)) {
        return NULL;
    }
    string filenamestr = filename;
    string space = PyUnicode_AsUTF8(PyObject_GetAttrString(mod, "space"));

    cout << space+"/"+filenamestr << endl;
    string str;

    ifstream file (space+"/"+filenamestr);

    file.seekg (0, file.end);

    int length = file.tellg();

    file.seekg (0, file.beg);

    string strv;
    while (getline (file, strv)) {
        // Output the text from the file
        str+=("\n" + strv);
    }

    file.close();

    return PyUnicode_FromString(str.c_str());
}
static PyObject *method_writefile(PyObject *self, PyObject *args){

    char* filename;
    char* str;
    if(!PyArg_ParseTuple(args, "ss", &filename,&str)) {
        return NULL;
    }
    string filenamestr = filename;
    string space = PyUnicode_AsUTF8(PyObject_GetAttrString(mod, "space"));

    cout << space+"/"+filenamestr << endl;

    string strc = str;
    ofstream file (space+"/"+filenamestr);

    file << strc;

    file.close();

    return PyUnicode_FromString(str);
}
static PyMethodDef methods[4]= {
        {"spaceout", (PyCFunction)_method_spaceout,METH_VARARGS,"spaceget"},
        {"read", (PyCFunction)method_readfile,METH_VARARGS,"Read file text"},
        {"write", (PyCFunction)method_writefile,METH_VARARGS,"Write to file text"},
        {NULL, NULL, 0, NULL}
};
static struct PyModuleDef module = {
        PyModuleDef_HEAD_INIT, "filework", "File module", -1, methods
};
PyMODINIT_FUNC
PyInit_filework() {
    mod = PyModule_Create(&module);
    PyModule_AddObject(mod, "space", PyUnicode_FromString("/"));

    return mod;
}