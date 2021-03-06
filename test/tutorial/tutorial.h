typedef struct test_st_s test_st_t;

extern int a;
extern double b;
extern char c;

static PyObject *func_hello(PyObject *self, PyObject *args);
static PyObject *func_ret_int(PyObject *self, PyObject *args);
static PyObject *func_ret_double(PyObject *self, PyObject *args);
static PyObject *func_ret_str(PyObject *self, PyObject *args);
static PyObject *func_many_args(PyObject *self, PyObject *args);
static PyObject *func_ret_struct(PyObject *self, PyObject *args);

struct test_st_s {
    PyObject_HEAD // Макрос объявления нового типа, объекта фиксированного размера
    int val1;
    double val2;
    char val3;
};
