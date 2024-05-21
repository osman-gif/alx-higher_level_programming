#include "object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int size = PyList_GET_SIZE(op);
	printf("size: %d\n", size);
}
