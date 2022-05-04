#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <stdlib.h>

/**
* print_python_list_info - prints some basic info about Python lists
* @p: iterator
*/

void print_python_list_info(PyObject *p)
{
	int j = 0;
	PyObject *iter;
	Py_ssize_t siz = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int)siz);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	while (j < siz)
	{
	iter = PyList_GetItem(p, j);
		printf("Element %d: %s\n", j, Py_TYPE(iter)->tp_name);
		j++;
	}
}
