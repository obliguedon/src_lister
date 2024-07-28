module adder_tb ();
    localparam WIDTH = 8;

    import calculator_pkg::*;

    logic clk;
    logic reset_n;
    logic [WIDTH-1:0] in_a;
    logic [WIDTH-1:0] in_b;
    logic [WIDTH-1:0] out_sum;
    te_out_status status;
    te_operation operation;

    top #(.BIT_WIDTH(WIDTH)) dut
    (
        .clk,
        .reset_n,
        .a(in_a),
        .b(in_b),
        .operation,
        .result(out_sum),
        .status
    );

    initial begin : clock_generation
        clk = 0;
        forever #1 clk = ~clk;
    end : clock_generation

    initial begin : power_up_reset
        reset_n = 0;
        #10;
        reset_n = 1;
    end : power_up_reset

    initial begin : the_test
        $dumpfile("dump.vcd");
        $dumpvars;
        $display("==== beggin simulation ====");

        in_a = 0;
        in_b = 0;
        #1;
        if (out_sum != (in_a + in_b)) $display("the sum is incorrect");

        in_a = 1;
        in_b = 0;
        #1;
        if (out_sum != (in_a + in_b)) $display("the sum is incorrect");

        in_a = 1;
        in_b = 1;
        #1;
        if (out_sum != (in_a + in_b)) $display("the sum is incorrect");

        in_a = 1;
        in_b = 3;
        #1;
        if (out_sum != (in_a + in_b)) $display("the sum is incorrect");

        in_a = 8;
        in_b = 16;
        #1;
        if (out_sum != (in_a + in_b)) $display("the sum is incorrect");
    end : the_test
endmodule