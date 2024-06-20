module adder_tb ();
    localparam WIDTH = 8;
    
    logic [WIDTH-1:0] in_a;
    logic [WIDTH-1:0] in_b;
    logic [WIDTH-1:0] out_sum;
    logic out_carry;
    
    nbits_adder #(.WIDTH(WIDTH)) dut 
    (
        .a(in_a),
        .b(in_b),
        .sum(out_sum),
        .carry(out_carry)
    );

    initial begin
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
    end
endmodule