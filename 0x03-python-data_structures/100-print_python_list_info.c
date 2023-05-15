#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - prints some basic info about python list
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;
    PyListObject *list = (PyListObject *)p;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);
    for (i = 0; i < size; i++)
        printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
