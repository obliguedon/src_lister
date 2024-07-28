package calculator_pkg
    typedef enum
    {
        ADD,
        SUB
    } te_operation;

    typedef enum
    {
        VALID,
        NEGATIVE,
        OVERFLOW,
        STANDBY
    } te_out_status;
endpackage